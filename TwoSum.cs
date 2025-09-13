using System;
using System.Collections.Generic;

public class TwoSum : IProblem
{
    public string Name => "Two Sum";

    public void Run()
    {
        Console.WriteLine("Running Two Sum problem...");

        int[] nums = { 2, 7, 11, 15 };
        int target = 9;

        var result = FindTwoSum(nums, target);
        if (result.Length == 2)
        {
            Console.WriteLine($"Indices found: {result[0]}, {result[1]}");
        }
        else
        {
            Console.WriteLine("No two sum solution found.");
        }
    }

    // ✅ FIX: Method without extra braces
    public static int[] FindTwoSum(int[] nums, int target)
    {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];
            if (map.ContainsKey(complement))
            {
                return new int[] { map[complement], i };
            }
            if (!map.ContainsKey(nums[i]))
            {
                map[nums[i]] = i;
            }
        }

        return new int[] { };
    }
}
