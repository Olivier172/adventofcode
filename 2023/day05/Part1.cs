
namespace day05
{
    public static class Part1
    {
        
        /// <summary>
        /// returns the list of seeds and extracts the maps from the input file
        /// </summary>
        /// <param name="maps"></param>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static List<long> ParseInput(List<Map> maps, string fileName="input.txt")
        {
            List<long> seeds = new List<long>();

            using (StreamReader reader = new StreamReader(fileName))
            {
                string input = reader.ReadToEnd();
                // split seeds and maps
                string[] parts = input.Split("\n\n");

                // extract seeds
                seeds = parts[0].Split(":")[1]
                    .Split(" ", StringSplitOptions.RemoveEmptyEntries)
                    .Select(long.Parse)
                    .ToList();
    
                //extract maps
                for(int i = 1; i < parts.Length; i++)
                {
                    string[] mapElements = parts[i].Split(":");
                    Map currentMap = new Map(mapElements[0].Trim()); // 0 => mapname
                    string[] ranges = mapElements[1].Split("\n", StringSplitOptions.RemoveEmptyEntries);
                    foreach(string range in ranges)
                    {
                        string[] values = range.Split(" ");
                        long destinationRangeStart = long.Parse(values[0]);
                        long sourceRangeStart = long.Parse(values[1]);
                        long length = long.Parse(values[2]);
                        currentMap.mapRanges.Add(new MapRange()
                        {
                            RangeStart = sourceRangeStart,
                            RangeEnd = sourceRangeStart + (length - 1),
                            Offset = destinationRangeStart - sourceRangeStart
                        });
                    }
                    maps.Add(currentMap);
                   

                }
            }
 
            return seeds;
        }

        public static List<long> CalculateSeedToLocationNrs(List<long> seeds, List<Map> maps)
        {
            List<long> locations = new();
            foreach (long seed in seeds)
            {
                long curValue = seed;
                // calulcate destination value of the current source value by taking it through all the maps
                foreach (Map map in maps)
                {
                    // mapping source to destination value
                    curValue = map.MapSourceToDestination(curValue);
                }
                locations.Add(curValue);
            }
            
            return locations;
        }
        
        public static void Run()
        {
            List<Map> maps = new();
            Console.WriteLine("Part 1: ");

            List<long> seeds = ParseInput(maps);

            if(seeds.Count == 0)
            {
                return;
            }

            // debug print
            //Console.WriteLine("Seeds: ");
            //foreach(long seed in seeds)
            //{
            //    Console.WriteLine(seed);
            //}
            //Console.WriteLine();

            List<long> locationNrs = CalculateSeedToLocationNrs(seeds, maps);

            long lowestLocationNr = locationNrs.Min();
            Console.WriteLine($"The lowest location number is {lowestLocationNr}");
        }

        public class Map
        {
            public string MapName { get; set; } = string.Empty;

            public List<MapRange> mapRanges { get; set; } = new();

            public Map(string name)
            {
                MapName = name;
            }

            public long MapSourceToDestination(long sourceValue)
            {

                // check if source value is in a range to have a custom mapping with an offset
                foreach (MapRange mapRange in mapRanges)
                {
                    if (mapRange.InRange(sourceValue))
                    {
                        return mapRange.MapSourceToDestintation(sourceValue);
                    }
                }

                return sourceValue; // if source value is not in range of a translation range than it is the number itself
            }
        }

        public class MapRange
        {
            public long RangeStart { get; set; }

            public long RangeEnd { get; set; }

            // the offset to go from source space to destination space
            public long Offset { get; set; }

            /// <summary>
            /// tests if the source value is in range for this translation
            /// </summary>
            /// <param name="sourceValue"></param>
            /// <returns></returns>
            public bool InRange(long sourceValue)
            {
                return ((RangeStart <= sourceValue) && (sourceValue <= RangeEnd));
            }
            public long MapSourceToDestintation(long sourceValue)
            {
                return sourceValue + Offset;
            }
        }

    }

    
}
