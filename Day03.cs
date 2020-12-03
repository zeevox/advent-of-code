using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020
{
    public sealed class Day03 : BaseDay
    {
        private readonly string[] _input;

        public Day03()
        {
            _input = File.ReadAllLines(InputFilePath).ToArray();
        }

        public long CountTrees(int xAcross, int yDown)
        {
            long x = 0;
            long y = 0;
            long trees = 0;
            do
            {
                if (_input[y][(int) x % _input[y].Length] == '#') trees += 1;

                y += yDown;
                x += xAcross;
            } while (y < _input.Length);

            return trees;
        }

        public override string Solve_1()
        {
            return CountTrees(3, 1).ToString();
        }

        public override string Solve_2()
        {
            return (CountTrees(1, 1) * CountTrees(3, 1) * CountTrees(5, 1) * CountTrees(7, 1) * CountTrees(1, 2))
                .ToString();
        }
    }
}