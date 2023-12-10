using System;

namespace day02
{

    /*
    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
    What is the sum of the IDs of those games?
    */
    public static class Part1{

    
        /// <summary>
        /// Parses the text input file into a list of gamerecords
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static List<GameRecord> ParseInput(string fileName) {
            List<GameRecord> gameRecords = new();
            try{
                using(StreamReader reader = new StreamReader(fileName)) {
                    string? line;
                    while( !string.IsNullOrEmpty(line = reader.ReadLine()) ) {
                        // splitting line in game and draws information
                        string[] splits = line.Split(":");

                        // parsing gameID 
                        int gameID = int.Parse(splits[0].Split(" ")[1]);
                        GameRecord currentRecord = new GameRecord(gameID);

                        // parsing draws
                        foreach(string drawLine in splits[1].Split(";"))
                        {
                            Draw draw = new Draw();
                            foreach(string amountLine in drawLine.Split(","))
                            {
                                string[] strings = amountLine.Trim().Split(" ");
                                int amount = int.Parse(strings[0]);
                                string cubeColor = strings[1];
                                switch(cubeColor) {
                                    case "red":
                                        draw.AmountOfRedCubes = amount;
                                        break;
                                    case "green":
                                        draw.AmountOfGreenCubes = amount;
                                        break;
                                    case "blue":
                                        draw.AmountOfBlueCubes = amount;
                                        break;
                                }
                                
                            }
                            // add draw to game record
                            currentRecord.Draws.Add(draw);
                        }
                    
                        // debug print
                        //Console.WriteLine(currentRecord.ToString() + "\n");
                        gameRecords.Add(currentRecord);
                    }
                }
            }
            catch (Exception e){
                Console.WriteLine($"An error occured parsing input from file {fileName}: {e}");
            }

            return gameRecords;
        }

        /// <summary>
        /// Runs through the game records and checks if the game is possible given an amount of red, green and blue cubes that are in a bag.
        /// </summary>
        /// <param name="MaxAmountOfRedCubes"></param>
        /// <param name="MaxAmountOfGreenCubes"></param>
        /// <param name="MaxAmountOfBlueCubes"></param>
        /// <returns>The sum of the gameIDs of the feasable games</returns>
        public static int CheckGameRecords(int MaxAmountOfRedCubes, int MaxAmountOfGreenCubes, int MaxAmountOfBlueCubes, List<GameRecord> gameRecords )
        {
            // sum of gameIDs that are feasable
            int sum = 0;
            // Flag to represent if a game is feasible
            bool feasible = false;
            // run through all the game records
            foreach(GameRecord gr in gameRecords)
            {
                // a game is feasible until an anomaly is detected
                feasible = true;
                foreach(Draw draw in gr.Draws)
                {
                    if(draw.AmountOfRedCubes > MaxAmountOfRedCubes || draw.AmountOfGreenCubes > MaxAmountOfGreenCubes || draw.AmountOfBlueCubes > MaxAmountOfBlueCubes)
                    {
                        feasible = false;
                    }
                }

                if( feasible)
                {
                    sum += gr.GameID; 
                }
            }
            return sum;
        }

        public static void Run() {
            Console.WriteLine("Part 1:");
            // parse the input
            List<GameRecord> gameRecords = ParseInput("input.txt");
            // calculate sum of gameids of all gamerecords that are feasible for a bag that contains:
            // 12 red cubes,
            // 13 green cubes
            // 14 blue cubes.
            int sumOfGameIds = CheckGameRecords(12, 13, 14, gameRecords);
            Console.WriteLine($"The sum of all the game ids that are feasable is {sumOfGameIds}");
        }
    }

    /// <summary>
    /// Class to represent the relevant information about a game record.
    /// A list of draws reveal an amount of red, green and blue cubes are revealed.
    /// </summary>
    public class GameRecord{
    
        public int GameID {get; set;}

        public List<Draw> Draws = new();

        public GameRecord(int gameID)
        {
            GameID = gameID;
        }

        public override string ToString()
        {
            string res = $"Game with gameid {GameID}: ";
            foreach(Draw draw in Draws)
            {
                res += draw.ToString() + " ";
            }
            return res;
        }
    }

    public class Draw{
        public int AmountOfRedCubes {get; set;} = 0;

        public int AmountOfGreenCubes {get; set;} = 0;

        public int AmountOfBlueCubes {get; set;} = 0;

        public override string ToString()
        {
            return $"Draw with {AmountOfRedCubes} red cubes, {AmountOfGreenCubes} green cubes, {AmountOfBlueCubes} blue cubes.";
        }
    }

}