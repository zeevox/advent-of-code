using System;
using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020
{
    public sealed class Day01 : CustomBaseDay
    {
        private readonly int[] _input;

        public Day01()
        {
            _input = File.ReadAllLines(InputFilePath).Select(int.Parse).ToArray();
        }

        /// <summary>
        ///     Given a dataset, find the two entries that sum to a specified target sum
        /// </summary>
        /// <remarks>Initial attempt, O(n log n) complexity</remarks>
        /// <param name="input">The list of entries</param>
        /// <param name="targetSum">The desired sum</param>
        /// <returns>The two numbers or an empty array if no such numbers found</returns>
        public static int[] FindTwoIntegersWithSum(int[] input, int targetSum)
        {
            // O(n log n)
            Array.Sort(input);

            // O(n log n)
            // iterate over each number and perform adapted binary search
            foreach (var number in input)
            {
                var lower = 0;
                var upper = input.Length - 1;
                var target = targetSum - number;

                while (lower < upper)
                {
                    var midpoint = (lower + upper) / 2;
                    if (target == input[midpoint]) return new[] {number, target};

                    if (target < input[midpoint])
                        upper = midpoint - 1;
                    else if (target > input[midpoint])
                        lower = midpoint + 1;
                    else break;
                }
            }

            return new int[0];
        }

        /// <summary>
        ///     Given a dataset, find the two entries that sum to a specified target sum
        /// </summary>
        /// <remarks>
        ///     A second attempt, given that the target sum is pretty small the memory to produce a boolean array of length
        ///     2020 is not so large. We only iterate over the list twice in this solution -> O(n)
        /// </remarks>
        /// <param name="input">The list of entries</param>
        /// <param name="targetSum">The desired sum</param>
        /// <returns>The two numbers or an empty array if no such numbers found</returns>
        public static int[] FindTwoIntegersWithSumV2(int[] input, int targetSum)
        {
            var booleanArray = new bool[targetSum];

            foreach (var number in input)
                if (number < targetSum)
                    booleanArray[number] = true;

            for (var i = 0; i < targetSum; i++)
                if (booleanArray[i] && booleanArray[targetSum - i])
                    return new[] {i, targetSum - i};

            return new int[0];
        }

        /// <summary>
        ///     Given a set of numbers, find the three entries that sum to specified target sum.
        /// </summary>
        /// <remarks>As this is an extension to the <see cref="FindTwoIntegersWithSumV2" /> method it has O(n ^ 2) complexity</remarks>
        /// <param name="input">The list of entries</param>
        /// <param name="targetSum">The desired sum</param>
        /// <returns>The three numbers or an empty array if no such numbers found</returns>
        public static int[] FindThreeIntegersWithSum(int[] input, int targetSum)
        {
            foreach (var number in input)
            {
                var complements = FindTwoIntegersWithSumV2(input, targetSum - number);
                if (complements.Length <= 0) continue;
                if (number + complements[0] + complements[1] == targetSum &&
                    !(complements[0] == number || complements[1] == number))
                    return new[] {number, complements[0], complements[1]};
            }

            return new int[0];
        }

        public override string Solve_1()
        {
            return FindTwoIntegersWithSumV2(_input, 2020).Aggregate(1, (x, y) => x * y).ToString();
        }

        public override string Solve_2()
        {
            return FindThreeIntegersWithSum(_input, 2020).Aggregate(1, (x, y) => x * y).ToString();
        }
    }
}