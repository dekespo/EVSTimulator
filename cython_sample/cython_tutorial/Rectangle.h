#include <vector>

namespace shapes
{
	class Rectangle
	{
		public:
			int x0, y0, x1, y1;
			Rectangle();
			Rectangle(int, int, int, int);
			~Rectangle();
			int getArea();
			void getSize(int*, int*);
			std::vector<int> libVectorStuff();
			void move(int, int);
	};
}
