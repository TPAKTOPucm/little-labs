using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace quickSort {
	internal class SafonovDM {
		public int Value { get; set; }
		public SafonovDM Next { get; set; }
		public SafonovDM Previous { get; set; }

		public SafonovDM(int value) {
			Value = value;
		}
	}
}
