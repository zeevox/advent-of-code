using System.Collections.Generic;
using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020.csharp
{
    public sealed class Day02 : BaseDay
    {
        private readonly string[] _input;

        public Day02()
        {
            _input = File.ReadAllLines(InputFilePath).ToArray();
        }

        public static int CountValidPasswords(IEnumerable<string> lines, bool newLogic = false)
        {
            var valid = 0;
            foreach (var line in lines)
            {
                var split = line.Split('-', ' ', ':');
                if (newLogic)
                {
                    var expectedChar = char.Parse(split[2]);
                    var char1 = split[4][int.Parse(split[0]) - 1];
                    var char2 = split[4][int.Parse(split[1]) - 1];
                    if ((char1 == expectedChar || char2 == expectedChar) && char1 != char2) valid += 1;
                }
                else
                {
                    var occurrences = split[4].Count(c => c == char.Parse(split[2]));
                    if (occurrences >= int.Parse(split[0]) && occurrences <= int.Parse(split[1])) valid += 1;
                }
            }

            return valid;
        }

        public override string Solve_1()
        {
            return CountValidPasswords(_input).ToString();
        }

        public override string Solve_2()
        {
            return CountValidPasswords(_input, true).ToString();
        }
    }
}