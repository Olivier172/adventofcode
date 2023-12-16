

namespace day04
{
    public static class Part2
    {

        public static List<int> CalculateNrOfCards (List<ScratchCard> cards)
        {
            List<int> nrOfCards = new()
            {
                0 // element at index 0 doesnt match a card id...
            };
            // you start with one of each card
            for (int i=0; i<cards.Count; i++)
            {
                nrOfCards.Add(1);
            }

            foreach (ScratchCard card in cards)
            {
                int currentCardIndex = card.CardId;
                int cardsWon = 0;
                foreach (int number in card.YourNumbers)
                {
                    if (card.WinningNumbers.Contains(number))
                    {
                        cardsWon++;
                    }
                }

                // every copy of the current card wins an amount of copies of the next cards depending on how many nrs it got right
                int amountOfCopiesWon = 1 * nrOfCards[currentCardIndex];
                for (int i = 1; i <= cardsWon; i++)
                {
                    nrOfCards[currentCardIndex + i ] += amountOfCopiesWon;
                }

            }
            return nrOfCards;
        }

        public static void Run()
        {
            Console.WriteLine("Part 2:");
            List<ScratchCard> cards = Part1.ParseInput();

            List<int> nrOfCards = CalculateNrOfCards(cards);
            int sum = nrOfCards.Sum();
            Console.WriteLine($"The amount of cards in total is {sum}");
        }
    }

}
