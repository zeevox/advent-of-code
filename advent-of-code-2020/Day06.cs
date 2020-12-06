using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020
{
    public sealed class Day06 : BaseDay
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
            {
                if (partTwo)
                {
                    var splitGroup = group.Split(Environment.NewLine, StringSplitOptions.RemoveEmptyEntries);
                    Console.WriteLine($"{String.Join(", ", splitGroup)}");
                    var uniqueQs = splitGroup[0].ToCharArray().AsEnumerable();
                    foreach (var person in splitGroup)
                    {
                        uniqueQs = uniqueQs.Intersect(person.ToCharArray());
                    }

                    Console.WriteLine($"{String.Join(", ", uniqueQs)} -> {uniqueQs.Count()}");

                    count += uniqueQs.Count();

                    // var splitGroup = group.Split(Environment.NewLine);
                    // splitGroup.Select(s => s.ToCharArray()).Aggregate(splitGroup[0].ToCharArray().AsEnumerable(),
                    //     (a, chars) => a.Intersect(chars), a => a);
                    // Console.WriteLine(String.Join(", ", splitGroup.ToArray()));
                    // splitGroup.Select(s => s.Split()).Aggregate(splitGroup[0].Split().AsEnumerable(),
                    //     (a, words) => a.Intersect(words), a => a);
                    // var questions = new List<char>();
                    // foreach (var repeatedString in splitGroup)
                    // {
                    //     questions.AddRange(repeatedString.ToCharArray());
                    // }
                    //
                    // Console.WriteLine(String.Join(", ", questions.ToArray()));
                    //count += questions.Distinct().Count();
                }
                else
                {
                    count += group.Replace(Environment.NewLine, "").Distinct().Count();

                }
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