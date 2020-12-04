using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using AoCHelper;

namespace advent_of_code_2020
{
    public sealed class Day04 : BaseDay
    {
        private readonly string _input;
        
        public Day04()
        {
            _input = File.ReadAllText(InputFilePath);
        }

        public int CountValidPasswords(bool newlogic = false)
        {
            int validPassports = 0;
            string[] passports = _input.Split(new[] { Environment.NewLine + Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);
            Console.WriteLine("passports: [{0}]", string.Join(", ", passports));
            foreach (var passport in passports)
            {
                bool valid = true;
                if (newlogic)
                {
                    bool wasRight = valid;
                    var newpassport = passport.Replace(Environment.NewLine, " ").Split(" ", StringSplitOptions.RemoveEmptyEntries);
                    
                    foreach (var entry in newpassport)
                    {
                        var kv = entry.Split(':', StringSplitOptions.RemoveEmptyEntries);
                        //Console.WriteLine("kv [{0}]", string.Join(", ", kv));
                        
                        switch (kv[0])
                        {
                            case "byr":
                                if (!(int.Parse(kv[1]) >= 1920 && int.Parse(kv[1]) <= 2002)) valid = false;
                                break;
                            case "iyr":
                                if (!(int.Parse(kv[1]) >= 2010 && int.Parse(kv[1]) <= 2020)) valid = false;
                                break;
                            case "eyr":
                                if (!(int.Parse(kv[1]) >= 2020 && int.Parse(kv[1]) <= 2030)) valid = false;
                                break;
                            case "hgt":
                                if (kv[1].Contains("cm"))
                                {
                                    int height = 0;
                                    int.TryParse(kv[1].Substring(0, 3), out height);
                                    if (!(height <= 193 && height >= 150)) valid = false;
                                }
                                else if (kv[1].Contains("in"))
                                {
                                    int height = 0;
                                    int.TryParse(kv[1].Substring(0, 2), out height);
                                    if (!(height <= 76 && height >= 59)) valid = false;
                                }
                                else
                                {
                                    valid = false;
                                }

                                break;
                            case "hcl":
                                if (!Regex.Match(kv[1],
                                        "^#(?:[0-9a-fA-F]{3}){1,2}$").Success) valid = false;
                                break;
                            case "ecl":
                                var validEcl = new[]
                                    {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
                                if (!validEcl.Contains(kv[1])) valid = false;
                                break;
                            case "pid":
                                int pid = 0;
                                int.TryParse(kv[1], out pid);
                                if (kv[1].Length != 9 || pid == 0) valid = false;
                                break;
                        }

                        if (wasRight && !valid)
                        {
                            Console.WriteLine("=== NEW PASSPORT ===");
                            Console.WriteLine("passport [{0}]", string.Join(", ", newpassport));
                            Console.WriteLine($"invalid {kv[0]}:{kv[1]}");
                        }

                        wasRight = valid;
                    }
                    
                    
                }
                
                string[] parameters = new string[] {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
                foreach (var param in parameters)
                {
                    if (!passport.Contains(param + ":"))
                    {
                        Console.WriteLine($"missing {param}");
                        valid = false;
                    }
                }
                Console.WriteLine(valid ? "VALID :)" : "INVALID!!");

                if (valid) validPassports += 1;
            }

            return validPassports;
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