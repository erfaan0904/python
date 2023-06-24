#include "stdafx.h"
#include <iostream>
using namespace std;
int main()
{
	int n, a = 1, b = 1, c = 0, j = 2;
	cout << "--------------------------" << endl;
	cout << "Please enter a number : ";
	cin  >> n;
	cout << "--------------------------" << endl;
	cout << "1. 1" << endl;
	cout << "2. 1" << endl;
	for (int i = 1; i <= n; i++)
	{
		j = j + 1;
		c = a + b;
		if (j == (n + 1))
			break;
		else
		{
			cout << j << ". " << c << endl;
			a = b;
			b = c;
		}
	}
	cout << "--------------------------" << endl;
	return 0;
}

