using System;
using System.IO;
using AoCHelper;

namespace advent_of_code_2020.csharp
{
    public sealed class Day05 : BaseDay
    {
        private readonly string[] _input;
        
        public Day05()
        {
            _input = File.ReadAllLines(InputFilePath);
        }

        public int GetSeatId(bool partTwo = false)
        {
            var max = 0;
            
            bool[] array = null;
            if (partTwo)
            {
                array = new bool[128 * 8];
            }

            foreach (var line in _input)
            {
                var row = Convert.ToInt32(line.Substring(0, 7).Replace("B", "1").Replace("F", "0"), 2);
                var col = Convert.ToInt32(line.Substring(7).Replace("R", "1").Replace("L", "0"), 2);
               
                var id = row * 8 + col;

                if (partTwo) array[id] = true;
                
                Console.WriteLine($"{line} -> {col}:{row} -> {id}");

                if (id <= max) continue;
                max = id;
            }

            if (!partTwo) return max;
            
            for (var i = 1; i < array.Length - 1; i++)
            {
                if (array[i - 1] && array[i + 1] && !array[i]) return i;
            }

            return 0;
        }

        public override string Solve_1()
        {
            return GetSeatId().ToString();
        }

        public override string Solve_2()
        {
            return GetSeatId(true).ToString();
        }
    }
}