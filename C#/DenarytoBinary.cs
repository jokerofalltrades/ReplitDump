using System;

public class Program
{
  public static void Main()
  {
    string Binary = "";
    Console.WriteLine("Enter a number");
    long Denary = Convert.ToInt64(Console.ReadLine());
    int v = 0;
    while (Math.Pow(2,v) < Denary)
    {
      v++;
    }
    while (Denary != 0 || v>=0)
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
    Console.WriteLine("Your number is {0} in binary!",Binary);
  }
}
