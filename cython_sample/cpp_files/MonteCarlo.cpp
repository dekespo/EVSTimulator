#include "MonteCarlo.h"

using namespace monteCarlo_NS;

MonteCarlo::MonteCarlo()
{
	MonteCarlo(1000);
}

MonteCarlo::MonteCarlo(int value)
{
	srand(time(NULL));
	_sampleNo = value;
	generateSample();
}

MonteCarlo::~MonteCarlo() { }

void MonteCarlo::generateSample()
{
	for(int i = 0; i < _sampleNo; i++)
	{
		_sampleVector.push_back(rand() % 100 + 1);
	}
}

void MonteCarlo::calculate()
{
	double sum = 0;
	for(std::vector<int>::iterator it = _sampleVector.begin(); it != _sampleVector.end(); ++it)
	{
		sum += *it;
	}
	_result = sum / _sampleNo;
}

double MonteCarlo::getResult()
{
	return _result;
}
