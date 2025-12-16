
namespace day05
{
    public static class Part2
    {
        public static List<SeedRange> ParseInput(List<Map> maps, string fileName = "input.txt")
        {
            List<SeedRange> seedRanges = new();
            using (StreamReader reader = new StreamReader(fileName))
            {
                // extract seed ranges
                long[] seedRangePairs = reader.ReadLine()!
                    .Split(":")[1]
                    .Split(" ", StringSplitOptions.RemoveEmptyEntries)
                    .Select(long.Parse)
                    .ToArray();
                for(int i = 0; i < seedRangePairs.Length; i+=2)
                {
                    SeedRange currentSeedRange = new SeedRange()
                    {
                        SeedRangeStart = seedRangePairs[i],
                        SeedRangeLength = seedRangePairs[i+1]
                    };
                    seedRanges.Add(currentSeedRange);
                }

                // extract maps
                Map currentMap;
                string[] mapStrings = reader.ReadToEnd().Split("\n\n", StringSplitOptions.RemoveEmptyEntries);
                foreach(string mapString in mapStrings) 
                {
                    string[] parts = mapString.Split(":");
                    currentMap = new Map(parts[0].Trim());
                    string[] rangeStrings = parts[1].Split("\n", StringSplitOptions.RemoveEmptyEntries);
                    foreach(string rangeString in rangeStrings)
                    {
                        long[] rangeParams = rangeString.Split(" ", StringSplitOptions.RemoveEmptyEntries)
                        .Select(long.Parse)
                        .ToArray();
                        MapRange mr = new MapRange()
                        {
                            DestinationRangeStart = rangeParams[0],
                            SourceRangeStart = rangeParams[1],
                            Length = rangeParams[2]
                        };
                        currentMap.mapRanges.Add(mr);
                    }
                    maps.Add(currentMap);
                    
                }

            }
            return seedRanges;
        }
        
        public static void Run()
        {
            List<Map> maps = new();
            Console.WriteLine("Part 2: ");

            List<SeedRange> seedRanges = ParseInput(maps, "input.txt");

            foreach(SeedRange sr in seedRanges)
            {
                Console.WriteLine($"start {sr.SeedRangeLength} len {sr.SeedRangeLength}");
            }

            List<SeedRange> destRanges = new();
            foreach (Map map in maps)
            {
                destRanges = map.MapSourceRangesToDestinationRanges(seedRanges);
            }



            long lowestLocationNr = destRanges[0].SeedRangeStart;

            foreach (SeedRange sr in destRanges)
            {
                if(sr.SeedRangeStart < lowestLocationNr)
                {
                    lowestLocationNr = sr.SeedRangeStart;
                }
            }
 
            Console.WriteLine($"The lowest location number is {lowestLocationNr}");
        }

        public class Map
        {
            public string MapName { get; set; } = string.Empty;

            public List<MapRange> mapRanges { get; set; } = new();

            public Map(string mapName)
            {
                MapName = mapName;
            }

            public long MapSourceToDestination(long sourceValue)
            {
                foreach(MapRange mr in mapRanges)
                {
                    if(mr.IsInRange(sourceValue))
                    {
                        return mr.MapSourceToDestination(sourceValue);
                    }
                }

                return sourceValue;
            }

            public List<SeedRange> MapSourceRangesToDestinationRanges(List<SeedRange> seedRanges)
            {
                List<SeedRange> DestinationRanges = new();
                foreach(SeedRange seedRange in seedRanges)
                {
                    foreach (MapRange mr in mapRanges)
                    {
                        
                        // check if source range fits completly in maprange
                        if ( (mr.SourceRangeStart < seedRange.SeedRangeStart) && (seedRange.SeedRangeStart + seedRange.SeedRangeLength-1) < (mr.SourceRangeStart+ mr.Length))
                        {
                            // transform only seedrangestart and add to destination ranges
                            SeedRange destRange = new SeedRange()
                            {
                                SeedRangeStart = mr.MapSourceToDestination(seedRange.SeedRangeStart),
                                SeedRangeLength = seedRange.SeedRangeLength
                            };
                            DestinationRanges.Add(destRange);
                            break;
                        }
                        // partial fit  from start of seedrange to end of map range
                        if ((seedRange.SeedRangeStart < (mr.SourceRangeStart + mr.Length)) && (seedRange.SeedRangeStart > mr.SourceRangeStart))
                        {
                            // transform only seedrangestart and add to destination ranges
                            long lengthOfFit = ((mr.SourceRangeStart + mr.Length) - seedRange.SeedRangeLength); // end_mr - sr_start
                            SeedRange destRange = new SeedRange()
                            {
                                SeedRangeStart = mr.MapSourceToDestination(seedRange.SeedRangeStart),
                                SeedRangeLength = lengthOfFit
                            };
                            DestinationRanges.Add(destRange);
                            // update seedrange to excluded fitted part:
                            seedRange.SeedRangeStart -= lengthOfFit;
                            seedRange.SeedRangeLength -= lengthOfFit;
                            
                        }
                        // partial fit from start of map range to seed range end
                        if ((seedRange.SeedRangeStart + seedRange.SeedRangeLength-1 > mr.SourceRangeStart) && ((seedRange.SeedRangeStart + seedRange.SeedRangeLength -1  < mr.SourceRangeStart + mr.Length)))
                        {
                            // transform only seedrangestart and add to destination ranges
                            long lengthOfFit = seedRange.SeedRangeStart + seedRange.SeedRangeLength - 1 - mr.SourceRangeStart ;// end_sr - start_mr
                            SeedRange destRange = new SeedRange()
                            {
                                SeedRangeStart = mr.MapSourceToDestination(mr.SourceRangeStart),
                                SeedRangeLength = lengthOfFit
                            };
                            DestinationRanges.Add(destRange);
                            // update seedrange to excluded fitted part: (start remians the same, only part at the end removed)
                            seedRange.SeedRangeLength -= lengthOfFit;
                        }

                    }
                    // unfitted part remains to same to dest
                    DestinationRanges.Add(seedRange);
                  
                }
                return DestinationRanges;
            }


        }

        public class MapRange
        {
            public long DestinationRangeStart { get; set; }

            public long SourceRangeStart { get; set; }

            public long Length { get; set; }

            public bool IsInRange(long sourceValue)
            {
                return ((SourceRangeStart <= sourceValue) && (sourceValue < SourceRangeStart + Length));
            }

            public long MapSourceToDestination(long sourceValue)
            {
                return sourceValue + (DestinationRangeStart - SourceRangeStart);
            }
        }

        public record SeedRange
        {
            public long SeedRangeStart { get; set; }

            public long SeedRangeLength { get; set; }
        }
    }
}
