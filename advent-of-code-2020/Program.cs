using AoCHelper;

namespace advent_of_code_2020
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            if (args.Length > 0 && args[0] == "--all")
                Solver.SolveAll();
            else
                Solver.SolveLast();
        }
    }
}