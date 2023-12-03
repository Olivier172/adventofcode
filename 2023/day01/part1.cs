using System;

public static class Part1 {

    /// <summary>
    /// Reads the input file and retriefs the calibration number from every line.
    /// This is done by finding the first and last digit and combing those two into an integer.
    /// These numbers are saved in a list and then returned.
    /// </summary>
    /// <param name="fileName"></param>
    /// <returns>A List of numbers based on the first and last digit of every line.</returns>
    public static List<int> ParseInput(string fileName="input.txt") {
        List<int> calibrations = new();
        try {
            using(StreamReader reader = new StreamReader(fileName)) {
               string? line ;
               // read lines from file until we reach an empty line or null
               while( !string.IsNullOrEmpty( line = reader.ReadLine() )) {
                    char? firstDigit = null;
                    char? lastDigit = null;
                    foreach(char c in line){
                        if(char.IsDigit(c)) {
                            // last digit is the is overwritten every time we find a digit in the line
                            lastDigit = c;
                            // first digit is only set the first time we find a digit in the line
                            if(firstDigit == null){
                                firstDigit = c; 
                            }
                        }
                    }
                    // parse number
                    if(firstDigit != null && lastDigit != null){
                        int calibration;
                        bool succes = int.TryParse( $"{firstDigit}{lastDigit}", out calibration);
                        if(succes) {
                            // add to list of calibrations to return
                            calibrations.Add(calibration);
                        }
                        else{
                            Console.WriteLine($"Problem parsing number with first digit {firstDigit} and last digit {lastDigit}");
                        }
                    }
                    else{
                        System.Console.WriteLine("!First or last digit is null");
                    }
                    
     
               } 
            }
        }
        catch (Exception e) {
            Console.WriteLine($"file {fileName} could not be read: {e.Message}");
        }
        return calibrations;
        
    }

    public static void Run() {
        Console.WriteLine("Part1 : ");
        List<int> calibrations = ParseInput();
        int sum = calibrations.Sum();
        Console.WriteLine($"The sum of all the calibration values is {sum}\n");
    }
}