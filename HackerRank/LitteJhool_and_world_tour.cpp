#include<iostream>

using namespace std;
#define ulint unsigned int
#define uint unsigned int
#define usint unsigned short int

class Input
{
public:
usint cases;
ulint *m;
uint *n;
ulint **values;
usint out;

void parseinput();
int check();
void initialize(bool *, ulint);
usint deduce(bool *, ulint, ulint, ulint, bool *, uint);
~Input();
};


Input::~Input()
{
	delete m,n;
	delete [] values;
}

void Input::parseinput()
{
	cin>>cases;
	m = new ulint[cases];
	n = new uint[cases];
	values = new ulint*[cases];
	for(int i=0;i<cases;i++)
	{
		cin>>m[i];
		cin>>n[i];
		values[i] = new ulint[n[i]*2];		
		for(int j=0;j<n[i]*2;j++)
		{
			cin>>values[i][j];
		}
	}
}


void Input::initialize(bool *a, ulint size)
{
	for(int i=0; i<size; i++)
	{
		a[i] = 0;
	}
}

void mapinrange(bool *map, ulint index, int *first, usint *possibilities)
{	
	if(!map[index])
	{
		if(-1 == *first)
			*first = index;
		*possibilities += 1;
	}
}



usint Input::deduce(bool *map, ulint lim, ulint m, ulint n, bool *track, uint k)
{
	usint possibilities = 0;
	int first = -1;
	int i,j;
	if(m<n)
	{
		for(i=0;i+m<=n;i++)
		{
			mapinrange(map, i+m, &first, &possibilities);
			if(possibilities>1)
				return 0;
		}
	}
	else
	{
		for(i=0;i+m<lim;i++)
		{
			mapinrange(map, i+m, &first, &possibilities);
			if(possibilities>1)
				return 0;
		}
		for(j=0;j<=n;i++)
		{
			mapinrange(map, j++, &first, &possibilities);
			if(possibilities>1)
				return 0;
		}
	}
	if(1 == possibilities)
	{
		map[first] = 1;
		track[k] = 1;
		return 0;
	}
	else if(0 == possibilities)
		return 1;
	else	return 0;
}


int Input::check()
{
	out = 0;
	for(int i=0; i<cases; i++)
	{
		bool *map = new bool[m[i]];
		bool firstpass = 0;
		bool *trackcase = new bool[n[i]];
		initialize(map,m[i]);
		initialize(trackcase,n[i]);
		for(int j=0; j<n[i]; j++)
		{
			for(int k=0; k<n[i]*2 && !out; k+=2)
			{
				if(values[i][k]>=m[i] || values[i][k+1]>=m[i])
				{
					out = 1;
					break;
				}
				else if(values[i][k] == values[i][k+1])
				{
					map[values[i][k]] = 1;
					firstpass = 1;
				}
				else if(!trackcase[k/2])
				{
					if(deduce(map, m[i], values[i][k], values[i][k+1], trackcase, k/2))
					{
						out = 1;
						break;
					}
				}
			}
		if(!j && !firstpass)
			break;
		}
		if(!out)
			cout<<"YES\n";
		else	cout<<"NO\n";
		delete[] map;
		out = 0;
	}
}
		

main()
{
Input inp;
inp.parseinput();
inp.check();
}
