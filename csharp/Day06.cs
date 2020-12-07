using System;
using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020
{
    public sealed class Day06 : CustomBaseDay
    {
        private readonly string[] _input;

        public Day06()
        {
            _input = File.ReadAllText(InputFilePath).Split(new[] {Environment.NewLine + Environment.NewLine},
                StringSplitOptions.RemoveEmptyEntries);
        }

        public int Solve(bool partTwo)
        {
            var count = 0;
            foreach (var group in _input)
                if (partTwo)
                {
                    var splitGroup = group.Split(Environment.NewLine, StringSplitOptions.RemoveEmptyEntries);
                    count += splitGroup.Aggregate(splitGroup[0].ToCharArray().AsEnumerable(),
                        (current, person) => current.Intersect(person.ToCharArray())).Count();
                }
                else
                {
                    count += group.Replace(Environment.NewLine, "").Distinct().Count();
                }

            return count;
        }

        public override string Solve_1()
        {
            return Solve(false).ToString();
        }

        public override string Solve_2()
        {
            return Solve(true).ToString();
        }
    }
}