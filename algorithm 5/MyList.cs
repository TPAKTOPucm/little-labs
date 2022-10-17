using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace quickSort {
	internal class MyList {
		private SafonovDM firstElement;
		private SafonovDM lastElement;
		public int Length {get; private set;}
		private SafonovDM GetElement(int index) {
			SafonovDM tmp = firstElement;
			for (int i = 0; i < index; i++) {
				tmp = tmp.Next;
			}
			return tmp;
		}
		public void Add(int value, int index = 0) {
			if (Length == 0) {
				firstElement = new SafonovDM(value);
				lastElement = firstElement;
				firstElement.Next = firstElement;
				lastElement.Previous = firstElement;
			} else {
				var tmp = GetElement(index);
				tmp.Previous.Next = new SafonovDM(value);
				tmp.Previous.Next.Previous = tmp.Previous;
				tmp.Previous.Next.Next = tmp;
				tmp.Previous = tmp.Previous.Next;
				if (index == 0)
					firstElement = firstElement.Previous;
				lastElement = firstElement.Previous;
			}
			Length++;
		}
		public int Get(int index) {
			return GetElement(index).Value;
		}
		public void Delete(int index) {
			var tmp = GetElement(index);
			tmp.Next.Previous = tmp.Previous;
			tmp.Previous.Next = tmp.Next;
			Length--;
		}
		public override string ToString() {
			string toReturn = "";
			SafonovDM tmp = firstElement;
			for (int i = 0; i < Length; i++)
			{
				toReturn += tmp.Value+" ";
				tmp = tmp.Next;
			}
			return toReturn;
		}
		public void Add(MyList list)
		{
			if(list.Length == 0)
				return;
			if (Length == 0) {
				firstElement = list.firstElement;
				lastElement = list.lastElement;
				Length = list.Length;
			} else {
				lastElement.Next = list.firstElement;
				firstElement.Previous = list.lastElement;
				list.lastElement.Next = firstElement;
				list.firstElement.Previous = lastElement;
				Length += list.Length;
			}
		}
		public MyList Sort()
		{
			if (Length < 2)
				return this;
			MyList min = new MyList();
			MyList max = new MyList();
			MyList eq = new MyList();
			SafonovDM tmp = firstElement;
			int value = tmp.Value;
			for (int i = 0; i < Length; i++) {
				if(tmp.Value == value) 
					eq.Add(tmp.Value);
				else if (tmp.Value > value)
					max.Add(tmp.Value);
				else
					min.Add(tmp.Value);
				tmp = tmp.Next;
			}
			min = min.Sort();
			max = max.Sort();
			min.Add(eq);
			min.Add(max);
			return min;
		}
	}
}
