using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace quickSort
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            MyList list = new MyList();
            int mode = 1;
            while (mode != 0)
            {
                Console.WriteLine("Выберите: 1-вставить в начало, 2-вывести элемент, 3-удалить элемент, 4-добавить элемент, 5-вывести массив, 6-отсортировать массив, 0-выйти");
                mode = int.Parse(Console.ReadLine());
                try
                {
                    if (mode == 1)
                        list.Add(int.Parse(Console.ReadLine()));
                    else if (mode == 2)
                        Console.WriteLine(list.Get(int.Parse(Console.ReadLine())));
                    else if (mode == 3)
                        list.Delete(int.Parse(Console.ReadLine()));
                    else if (mode == 4)
                    {
                        Console.WriteLine("Введите индекс и значение");
                        list.Add(int.Parse(Console.ReadLine()), int.Parse(Console.ReadLine()));
                    }
                    else if (mode == 5)
                        Console.WriteLine(list);
                    else if (mode == 6){
		list = list.Sort();
		Console.WriteLine(list.GetCount());
	        }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.StackTrace);
                }
            }
        }
    }
}