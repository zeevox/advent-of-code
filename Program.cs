using System;
using System.Diagnostics;
using System.Linq;

namespace advent_of_code_2020
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            var watch = Stopwatch.StartNew();
            var numbers = Day1.FindTwoIntegersWithSum(Day1.Input, 2020);
            watch.Stop();
            Console.WriteLine(
                $"Day 1 Part 1 [{watch.ElapsedMilliseconds}ms]: {numbers[0]} * {numbers[1]} = {numbers.Aggregate(1, (x, y) => x * y)}");
            
            watch.Restart();
            numbers = Day1.FindTwoIntegersWithSumV2(Day1.Input, 2020);
            watch.Stop();
            Console.WriteLine(
                $"Day 1 Part 1 [{watch.ElapsedMilliseconds}ms]: {numbers[0]} * {numbers[1]} = {numbers.Aggregate(1, (x, y) => x * y)}");
            
            watch.Restart();
            numbers = Day1.FindThreeIntegersWithSum(Day1.Input, 2020);
            watch.Stop();
            Console.WriteLine(
                $"Day 1 Part 2 [{watch.ElapsedMilliseconds}ms]: {numbers[0]} * {numbers[1]} * {numbers[2]} = {numbers.Aggregate(1, (x, y) => x * y)}");
        }
    }
}