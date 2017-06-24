#ifndef MONTECARLO
#define MONTECARLO

#include <ctime>
#include <cstdlib>
#include <vector>
#include <iterator>

namespace monteCarlo_NS
{
	class MonteCarlo
	{
		private:
			int _sampleNo;
			std::vector<int> _sampleVector;
			double _result;
			void generateSample();
		public:
			MonteCarlo();
			MonteCarlo(int);
			~MonteCarlo();
			void calculate();
			double getResult();
	};
}

#endif
