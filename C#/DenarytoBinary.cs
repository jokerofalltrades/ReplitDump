using System;

public class Program
{
  public static void Main()
  {
    string Binary = "";
    Console.WriteLine("Enter a number");
    long Denary = Convert.ToInt64(Console.ReadLine());
    int v = (int)Math.Log(Denary, 2);
    while (v>=0)
    {
      if (Math.Pow(2,v) < Denary+1)
      {
        Denary -= Convert.ToInt64(Math.Pow(2,v));
        Binary += "1";
      }
      else
      {
        Binary += "0";
      }
      v -= 1;
    }
    if (Denary == 0)
    {
      Binary = "0";
    }
    Console.WriteLine("Your number is {0} in binary!",Binary);
  }
}
