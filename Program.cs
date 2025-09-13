using System;
using System.Linq;
using System.Reflection;

class Program
{
    static void Main()
    {
        // Reflection: Find all classes implementing IProblem
        var problems = Assembly.GetExecutingAssembly()
            .GetTypes()
            .Where(t => typeof(IProblem).IsAssignableFrom(t) && !t.IsInterface)
            .Select(t => (IProblem)Activator.CreateInstance(t))
            .ToList();

        Console.WriteLine("Choose a problem to run:");
        for (int i = 0; i < problems.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {problems[i].Name}");
        }

        Console.Write("Enter choice: ");
        string choice = Console.ReadLine();

        if (int.TryParse(choice, out int index) && index > 0 && index <= problems.Count)
        {
            Console.WriteLine($"\n--- Running {problems[index - 1].Name} ---\n");
            problems[index - 1].Run();
        }
        else
        {
            Console.WriteLine("Invalid choice.");
        }
    }
}
