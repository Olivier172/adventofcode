
namespace day03
{
    public static class Part2
    {

        /// <summary>
        /// searches all adjacent numbers in the char array around the current row and col index.
        /// </summary>
        /// <param name="charArray"></param>
        /// <param name="currentRowIndex"></param>
        /// <param name="currentColIndex"></param>
        /// <param name="maxRowIndex"></param>
        /// <param name="maxColIndex"></param>
        /// <returns></returns>
        public static List<int> findAdjacentNrs(char[,] charArray, int currentRowIndex, int currentColIndex, int maxRowIndex, int maxColIndex)
        {
            List<int> adjecentNrs = new();
            //check around * for numbers
            for (int rowscan = currentRowIndex - 1; rowscan <= currentRowIndex + 1; rowscan++)
            {
                for (int colscan = currentColIndex - 1; colscan <= currentColIndex + 1; colscan++)
                {
                    // bounds check and exclude * itself from scan
                    if ((rowscan == currentRowIndex && colscan == currentColIndex) || rowscan < 0 || colscan < 0 || rowscan > maxRowIndex || colscan > maxColIndex)
                    {
                        continue;
                    }

                    // search adjacent nrs
                    if (char.IsDigit(charArray[rowscan, colscan]))
                    {
                        string adjacentNrBuffer = string.Empty;
                        int adjacentNr;
                        int startIndexNr = 0;

                        // first get start index nr
                        for (int i = colscan; i >= 0; i--)
                        {
                            if ( !char.IsDigit(charArray[rowscan, i]) )
                            {
                                startIndexNr = i + 1;
                                break;
                            }

                            // edge case: if the last position to the left is a char of the adjacent number,
                            // than this is the starting index of the adjacent number
                            if( i==0 && char.IsDigit(charArray[rowscan, i]) )
                            {
                                startIndexNr = i;
                            }
                        }

                        // get number in buffer
                        for (int i = startIndexNr; i <= maxColIndex; i++)
                        {
                            if ( char.IsDigit(charArray[rowscan, i]) )
                            {
                                adjacentNrBuffer += charArray[rowscan, i];
                            }
                            else
                            {
                                break;
                            }
                        }

                        // parse number 
                        adjacentNr = int.Parse(adjacentNrBuffer);
                        // check for doubles
                        if (!adjecentNrs.Contains(adjacentNr))
                        {
                            adjecentNrs.Add(adjacentNr);
                        }
                    }
                }
            }
            return adjecentNrs;
        }

        /// <summary>
        /// finds all gear ratios: A gear is any * symbol that is adjacent to exactly two part numbers.
        /// </summary>
        /// <param name="engineSchematic"></param>
        /// <returns></returns>
        public static List<int> findGearRatios(char[,] engineSchematic)
        {
            List<int> gearRatios = new();
            List<int> adjacentNrs;
            int amountOfRows = engineSchematic.GetLength(0);
            int amountOfColumns = engineSchematic.GetLength(1);
            
            // run through schematic
            for (int r = 0; r < amountOfRows; r++)
            {
                for (int c = 0; c < amountOfColumns; c++)
                {
                    if (engineSchematic[r, c] == '*')
                    {
                        adjacentNrs = findAdjacentNrs(engineSchematic, r, c, amountOfRows - 1, amountOfColumns - 1);
                        if(adjacentNrs.Count == 2)
                        {
                            // add gear ratio to list
                            gearRatios.Add(adjacentNrs[0] * adjacentNrs[1]);
                        }
                    }
                }
            }


                    
            return gearRatios;
        }
        
        public static void Run()
        {
            Console.WriteLine("Part 2:");
            char[,]? engineSchematic = Part1.ParseInput();
            if(engineSchematic == null )
            {
                Console.WriteLine("Something went wrong parsing input into charArray");
                return;
            }

            List<int> gearRatios = findGearRatios(engineSchematic);
            int sum = gearRatios.Sum();
            Console.WriteLine($"The sum of all the gear ratios is {sum}");



        }
    }
}
