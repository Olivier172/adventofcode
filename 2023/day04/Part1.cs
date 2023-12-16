
namespace day04
{
    public static class Part1
    {
        public static List<ScratchCard> ParseInput(string fileName="input.txt")
        {
            List<ScratchCard> cards = new();
            try
            {
                using (StreamReader reader = new StreamReader(fileName))
                {
                    string? line;
                    while( (line = reader.ReadLine()) != null)
                    {
                        ScratchCard currentCard;
                        string[] splits = line.Split(':');

                        // extract card id
                        string[] firstPartElements = splits[0].Split(" ");
                        int cardId = int.Parse(firstPartElements[firstPartElements.Length -1]);
                        currentCard = new ScratchCard(cardId);

                        // extract numbers 
                        string[] secondPartElements = splits[1].Split(" | ");

                        // extract winning numbers
                        foreach(string nrString in secondPartElements[0].Split(" "))
                        {
                            if (string.IsNullOrEmpty(nrString))
                            {
                                continue;
                            }
                            else
                            {
                                int currentNumber = int.Parse(nrString);
                                currentCard.WinningNumbers.Add(currentNumber);
                            }
                        }

                        // extract your numbers
                        foreach (string nrString in secondPartElements[1].Split(" "))
                        {
                            if (string.IsNullOrEmpty(nrString))
                            {
                                continue;
                            }
                            else
                            {
                                int currentNumber = int.Parse(nrString);
                                currentCard.YourNumbers.Add(currentNumber);
                            }
                        }


                        // add scratch card to list
                        cards.Add(currentCard);
                        
                    }

                }
            }
            catch(Exception e)
            {
                Console.WriteLine($"An error occured parsing the input file {fileName} : {e}");
            }
            return cards;
        }

        /// <summary>
        /// calculates the score of every card in the pile.
        /// </summary>
        /// <param name="cards">The pile of cards :)</param>
        /// <returns></returns>
        public static List<int> CalculateScratchCardScores(List<ScratchCard> cards)
        {
            List<int> scores = new();
            foreach(ScratchCard card in cards)
            {
                int currentCardScore = 0;
                foreach(int number in card.YourNumbers)
                {
                    if (card.WinningNumbers.Contains(number))
                    {
                        if(currentCardScore == 0)
                        {
                            currentCardScore = 1; // first match of your number with a winning number
                        }
                        else
                        {
                            currentCardScore *= 2; // every match after the first one doubles the score of the current card
                        }
                        
                    }
                }
                scores.Add(currentCardScore);
            }
            return scores;
        }
        
        public static void Run()
        {
            Console.WriteLine("Part 1 :");
            List<ScratchCard> cards = ParseInput();

            // debug print
            //foreach(ScratchCard card in cards)
            //{
            //    Console.WriteLine(card);
            //}

            List<int> scores = CalculateScratchCardScores(cards);
            int sum = scores.Sum();
            Console.WriteLine($"The total amount of points for all scratchcards in the pile is {sum}");
        }
    }

    public class ScratchCard
    {
        public int CardId { get; set; }

        public List<int> WinningNumbers { get; set; } = new();

        public List<int> YourNumbers { get; set; } = new();

        public ScratchCard(int id)
        {
            CardId = id;
        }

        public override string ToString()
        {
            string res = $"Card {CardId,3}:";
            foreach(int nr in WinningNumbers)
            {
                res += nr.ToString().PadLeft(3);
            }
            res += " |";
            foreach(int nr in YourNumbers)
            {
                res += nr.ToString().PadLeft(3);
            }

            return res;
        }
    }
}
