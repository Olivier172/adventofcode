using System;

namespace day02
{
    public static class Part2
    {

        public static int CalculateSumOfPowers(List<GameRecord> gameRecords)
        {
            // sum of all the powers of each gamerecord
            int sumOfPowers = 0;
            // Minimum amounts of red, green and blue 
            int MinAmountOfRedCubes;
            int MinAmountOfGreenCubes;
            int MinAmountOfBlueCubes;

            foreach(GameRecord gr in gameRecords)
            {
                // reset min amounts
                MinAmountOfRedCubes = 0;
                MinAmountOfGreenCubes = 0;
                MinAmountOfBlueCubes = 0;
                foreach (Draw draw in gr.Draws)
                {
                    if(draw.AmountOfRedCubes > MinAmountOfRedCubes)
                    {
                        MinAmountOfRedCubes = draw.AmountOfRedCubes;
                    }
                    if (draw.AmountOfGreenCubes > MinAmountOfGreenCubes)
                    {
                        MinAmountOfGreenCubes = draw.AmountOfGreenCubes;
                    }
                    if (draw.AmountOfBlueCubes > MinAmountOfBlueCubes)
                    {
                        MinAmountOfBlueCubes = draw.AmountOfBlueCubes;
                    }

                }
                // determine the power of this game by multiplying the minimum amount of red, green and blue cubes that need to be
                // in the bag to make this game feasable
                int power = MinAmountOfRedCubes * MinAmountOfGreenCubes * MinAmountOfBlueCubes;
                // debug print
                //Console.WriteLine($"power of draw is {power} = {MinAmountOfRedCubes} red cubes * {MinAmountOfGreenCubes} green cubes * {MinAmountOfBlueCubes} blue cubes");
                sumOfPowers += power;
            } 
            return sumOfPowers;
        }

        public static void Run()
        {
            Console.WriteLine("Part 2:");
            List<GameRecord> gameRecords = Part1.ParseInput("input.txt");

            int sumOfPowers = CalculateSumOfPowers(gameRecords);
            Console.WriteLine($"The sum of power of all the games is {sumOfPowers}");
        }
    }
}
