using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using AoCHelper;

namespace advent_of_code_2020.csharp
{
    public sealed class Day04 : BaseDay
    {
        private readonly string _input;

        private static readonly string[] Parameters = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
        private static readonly string[] EyeColours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};

        public Day04()
        {
            // the passports are split over several lines and separated by empty lines
            // so reading line by line isn't very useful in this scenario
            // although reading the whole text file into memory is a bit intense too
            _input = File.ReadAllText(InputFilePath);
        }

        /// <summary>
        ///     Given a batch file, find out how many passports are valid
        /// </summary>
        /// <see href="https://adventofcode.com/2020/day/4" />
        /// <param name="partTwo">Whether to valid the passports according to rules given in part two as well</param>
        /// <returns>The number of valid passports in the batch file</returns>
        public int CountValidPasswords(bool partTwo = false)
        {
            // counter variable
            var validPassports = 0;

            // passports in the batch file are separated by an empty line, or, as the computer sees it,
            // two newline characters. remove empty passports when there's some funky newline stuff.
            var passports = _input.Split(new[] {Environment.NewLine + Environment.NewLine},
                StringSplitOptions.RemoveEmptyEntries);

            foreach (var passport in passports)
            {
                // assume that a passport is valid by default, setting this
                // bool to false if it doesn't contain all the necessary fields
                var valid = ContainsAllFields(passport);
                
                // validate all of the passport's fields if completing the second part of the challenge
                if (partTwo && !ValidateFields(passport)) valid = false;
                
                if (valid) validPassports += 1;
            }

            return validPassports;
        }

        private static bool ValidateFields(string passport)
        {
            // remove the newlines that split a passport up, replacing them with spaces
            // split the passport by spaces into field:value strings 
            var parsedPassport = passport.Replace(Environment.NewLine, " ")
                .Split(" ", StringSplitOptions.RemoveEmptyEntries);

            foreach (var entry in parsedPassport)
            {
                // split each field:value string into a two-element string array which we can use
                var kv = entry.Split(':', StringSplitOptions.RemoveEmptyEntries);

                switch (kv[0])
                {
                    case "byr":
                        if (!(int.Parse(kv[1]) >= 1920 && int.Parse(kv[1]) <= 2002)) return false;
                        break;
                    case "iyr":
                        if (!(int.Parse(kv[1]) >= 2010 && int.Parse(kv[1]) <= 2020)) return false;
                        break;
                    case "eyr":
                        if (!(int.Parse(kv[1]) >= 2020 && int.Parse(kv[1]) <= 2030)) return false;
                        break;
                    case "hgt":
                        if (kv[1].Contains("cm"))
                        {
                            var height = 0;
                            int.TryParse(kv[1].Substring(0, 3), out height);
                            if (!(height <= 193 && height >= 150)) return false;
                        }
                        else if (kv[1].Contains("in"))
                        {
                            var height = 0;
                            int.TryParse(kv[1].Substring(0, 2), out height);
                            if (!(height <= 76 && height >= 59)) return false;
                        }
                        else
                        {
                            return false;
                        }

                        break;
                    case "hcl":
                        // hex colour validation RegEx
                        if (!Regex.Match(kv[1],
                            "^#(?:[0-9a-fA-F]{3}){1,2}$").Success) return false;
                        break;
                    case "ecl":
                        if (!EyeColours.Contains(kv[1])) return false;
                        break;
                    case "pid":
                        int.TryParse(kv[1], out var pid);
                        if (kv[1].Length != 9 || pid == 0) return false;
                        break;
                }
            }

            return true;
        }

        private static bool ContainsAllFields(string passport)
        {
            return Parameters.All(param => passport.Contains(param + ":"));
        }

        public override string Solve_1()
        {
            return CountValidPasswords().ToString();
        }

        public override string Solve_2()
        {
            return CountValidPasswords(true).ToString();
        }
    }
}