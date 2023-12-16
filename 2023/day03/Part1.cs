
using System.Collections;

namespace day03
{
    public static class Part1
    {
        
        public static char[,]? ParseInput(string fileName="input.txt")
        {
            char[,]? engineSchematic;
            try
            {
                using (StreamReader reader = new StreamReader(fileName))
                {
                    int AmountOfRows=0, AmountOfColumns=0;
                    
                    // read entire input
                    string input = reader.ReadToEnd();

                    // extract lines
                    string[] lines = input.Split('\n');
                    

                    // determine size of array
                    AmountOfRows = lines.Length;
                    if (string.IsNullOrEmpty(lines[lines.Length - 1]))
                    {
                        AmountOfRows--; // dont count empty last row
                    }
                    AmountOfColumns = lines[0].Length;

                    // create array
                    engineSchematic = new char[AmountOfRows, AmountOfColumns];

                    // get values from input
                    for(int r=0; r < AmountOfRows; r++)
                    {
                        for(int c = 0; c < AmountOfColumns; c++)
                        {
                            engineSchematic[r,c] = lines[r][c];
                        }
                    }
                    return engineSchematic;
                }
            }
            catch (Exception e) 
            {
                Console.WriteLine($"An error occured parsing input from file {fileName} : {e}");
            }

            return null;
        }

        public static void PrintCharArray(char[,] charArray)
        {
            for(int r=0; r < charArray.GetLength(0); r++)
            {
                for (int c = 0; c < charArray.GetLength(1); c++)
                {
                    Console.Write(charArray[r,c]);
                }
                Console.WriteLine();
            }
        }

        /// <summary>
        /// checks adjency of a number in the charArray to a symbol anywhere around it (vertical horizontal and diagonal)
        /// </summary>
        /// <param name="charArray"></param>
        /// <param name="lastRowIndex"></param>
        /// <param name="lastColIndex"></param>
        /// <param name="length"></param>
        /// <param name="maxRowIndex"></param>
        /// <param name="maxColIndex"></param>
        /// <returns></returns>
        public static bool checkAdjency(char[,] charArray, int lastRowIndex, int lastColIndex, int length, int maxRowIndex, int maxColIndex)
        {
            // last index of the number in the char array
            int startColIndex = lastColIndex - (length - 1);
            int endColIndex = lastColIndex;
            // column index to go through charArray with
            int c = 0;

            // check 1 character left of number chars
            c = startColIndex - 1;
            if ( c > 0 )
            {
                if (charArray[lastRowIndex, c] != '.')
                {
                    return true; // found an adjacent symbol :)
                }
            }

            // check 1 character right of number chars
            c = endColIndex + 1;
            if (c < maxColIndex)
            {
                if (charArray[lastRowIndex, c] != '.')
                {
                    return true; // found an adjacent symbol :)
                }
            }

            // check above and under the char positions of the number and diagnol positions to the positions of the number  
            for (c = startColIndex -1; c <= endColIndex + 1; c++)
            {
                // out of bounds
                if(c < 0 || c > maxColIndex)
                {
                    continue;
                }

                // check above 
                int rowAbove = lastRowIndex - 1;
                if(rowAbove > 0 ) // bounds check
                {
                    if (charArray[rowAbove, c] != '.')
                    {
                        return true; // found an adjacent symbol :)
                    }
                }
                
                // check below
                int rowBelow = lastRowIndex + 1;
                if(rowBelow < maxRowIndex) // bounds check
                {
                    if (charArray[rowBelow, c] != '.')
                    {
                        return true; // found an adjacent symbol :)
                    }
                }

            }
            return false; // no adjacent symbol found :(
        }

        /// <summary>
        /// finds all the part nrs. A partnr is a number in the charArray with at least one symbol adjacent to it.
        /// </summary>
        /// <param name="engineSchematic"></param>
        /// <returns></returns>
        public static List<int> GetPartNrs(char[,] engineSchematic)
        {
            List<int> partNrs = new();
            string nrBuffer = string.Empty;
            int currentNumber;
            int amountOfRows = engineSchematic.GetLength(0);
            int amountOfColumns = engineSchematic.GetLength(1);

            // run through schematic
            for (int r = 0; r < amountOfRows; r++)
            {
                for (int c = 0; c < amountOfColumns; c++)
                {
                    char currentChar = engineSchematic[r,c];
                    char nextChar = '.';
                    if (c+1 < amountOfColumns)
                    {
                        nextChar = engineSchematic[r, c+1];
                    }
                    
                    if (char.IsDigit(currentChar) )
                    {
                        nrBuffer += currentChar;
                        if (!char.IsDigit(nextChar) ){
                            // parse current number
                            currentNumber = int.Parse(nrBuffer);

                            //check adjency
                            if(checkAdjency(engineSchematic, r, c, nrBuffer.Length, amountOfRows-1, amountOfColumns-1))
                            {
                                // if the number is adjacent to a symbol, it counts as a partNr
                                partNrs.Add(currentNumber); // yes found one :)
                            }

                            // empty buffer
                            nrBuffer = string.Empty;
                        }
                    }
                }
            }
            return partNrs;
        }

        public static void Run()
        {
            char[,]? engineSchematic = ParseInput();
            if(engineSchematic == null)
            {
                Console.WriteLine("Something went wrong getting engine schematic into a 2d array");
                return;
            }

            // debug print
            //PrintCharArray(engineSchematic);

            List<int> partNrs = GetPartNrs(engineSchematic);
            int sum = partNrs.Sum();
            Console.WriteLine("Part 1:");
            Console.WriteLine($" The sum of all part numbers is {sum} ");
        }
    }
}
