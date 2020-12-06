using System;
using System.IO;
using System.Linq;
using AoCHelper;

namespace advent_of_code_2020.csharp
{
    public sealed class Day01 : BaseDay
    {
        public static readonly int[] Input =
        {
            1652, 1998, 1677, 1855, 1955, 1875, 1993, 1860, 1752, 1936, 1816, 1924, 1872, 2000, 1967, 1882, 1737, 1801,
            1832, 1985, 1933, 1911, 1894, 1384, 1871, 1607, 1858, 1950, 222, 1931, 1635, 1960, 1909, 1884, 1921, 1959,
            1981, 1920, 1684, 1734, 1490, 1632, 1935, 1982, 217, 1874, 1646, 1943, 986, 1509, 1899, 1834, 1908, 1769,
            1989, 1977, 1436, 1973, 1974, 1941, 1624, 2006, 1867, 843, 2003, 1838, 1904, 1892, 1972, 1957, 1890, 1540,
            1578, 1845, 1912, 1947, 1847, 1841, 1793, 2005, 1716, 1852, 1865, 1532, 1800, 1949, 1898, 1698, 1806, 1840,
            1833, 1915, 479, 1963, 1923, 1567, 1849, 1536, 1741, 1818, 1934, 1952, 1805, 1868, 1808, 955, 1954, 1712,
            1797, 1472, 1807, 1673, 1601, 1883, 1869, 1969, 1886, 1491, 1572, 2010, 1796, 1870, 1946, 1938, 1813, 1825,
            1944, 129, 1856, 1827, 1939, 1642, 1542, 745, 1836, 1810, 529, 1822, 1917, 486, 1953, 2008, 1991, 1628,
            1937, 1987, 1837, 1820, 1922, 1850, 1893, 1942, 1928, 1990, 1589, 1970, 1986, 1925, 1902, 2009, 1565, 1610,
            1857, 1889, 1901, 1790, 1880, 1999, 1964, 1948, 1824, 1877, 1916, 1978, 1839, 1659, 1846, 323, 1387, 1926,
            1958, 1914, 1906, 178, 1979, 1994, 2004, 1862, 1704, 1903, 1997, 1876, 1992, 1864, 1932, 1918, 1962, 1802,
            1278, 1861
        };

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