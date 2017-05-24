#include<iostream>
#include<vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

class point;
int rows, cols, minval;
vector<vector<int> > cache;

class point {
public:
	int left, right, score;
	point(int l, int r) {
		left = l;
		right = r;
		score = 0;
	}
};

point* find_dest(int rows, int cols, vector<vector<char> > table) {
	int i, j;
	for (i = 0; i < rows; i++)
		for (j = 0; j < cols; j++)
			if (table[i][j] == '*')
				return (new point(i, j));
	return NULL;
}

void path_traversal(point p, int thresh, int changes, char move,
		vector<vector<char> > table) {
	if (thresh >= 0 && changes < minval) {
		if (move != 'F' && table[p.left][p.right] != '*')
			table[p.left][p.right] = move;
		switch (move) {
		case 'U':
			p.left--;
			break;
		case 'D':
			p.left++;
			break;
		case 'L':
			p.right--;
			break;
		case 'R':
			p.right++;
		}
		if (table[p.left][p.right] == '*' && minval > changes) {
			minval = changes;
			return;
		}
		if (cache[p.left][p.right] > changes)
			cache[p.left][p.right] = changes;
		else
			return;
		if (p.left > 0) {
			if (table[p.left][p.right] == 'U')
				path_traversal(p, thresh - 1, changes, 'U', table);
			else
				path_traversal(p, thresh - 1, changes + 1, 'U', table);
		}
		if (p.left < rows - 1) {
			if (table[p.left][p.right] == 'D')
				path_traversal(p, thresh - 1, changes, 'D', table);
			else
				path_traversal(p, thresh - 1, changes + 1, 'D', table);
		}
		if (p.right > 0) {
			if (table[p.left][p.right] == 'L')
				path_traversal(p, thresh - 1, changes, 'L', table);
			else
				path_traversal(p, thresh - 1, changes + 1, 'L', table);
		}
		if (p.right < cols - 1) {
			if (table[p.left][p.right] == 'R')
				path_traversal(p, thresh - 1, changes, 'R', table);
			else
				path_traversal(p, thresh - 1, changes + 1, 'R', table);
		}
	}
}

int main() {
	int k, i, j, step;
	vector<vector<char> > table;
	cin >> rows >> cols >> k;
	char *str = new char[cols];
	for (i = 0; i < rows; i++) {
		table.push_back(vector<char>());
		cache.push_back(vector<int>());
		cin >> str;
		for (j = 0; j < cols; j++) {
			cache[i].push_back(k);
			table[i].push_back(str[j]);
		}
	}
	minval = k+1;
	path_traversal(point(0,0), k, 0, 'F', table);
	if (minval > k)
		cout<<"-1";
	else
		cout<<minval;
	return 0;
}
