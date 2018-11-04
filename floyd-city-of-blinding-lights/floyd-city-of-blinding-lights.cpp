#include <vector>
#include<iostream>
#include <limits.h>

using namespace std;

#define MAXLIMIT 999999

vector<string> split_string(string);
int** shortestPath(int V, int E, vector<int> *edge_from, vector<int> *edge_to, vector<int>  *weight) {
    int i, j, k;
    int** dist = new int*[V];
    for(int i = 0; i < V; i++)
        dist[i] = new int[V];
    for (i = 0; i< V; i++)
        for (j = 0; j < V; j++)
            dist[i][j] = MAXLIMIT;
    for (i = 0; i < E; i++)
        dist[(*edge_from)[i] - 1][(*edge_to)[i] - 1] = (*weight)[i];
    for (i = 0; i < V; i++)
        dist[i][i] = 0;

    for (k = 0; k < V; k++)
        for (i = 0; i < V; i++)
            for (j = 0; j < V; j++)
                if (dist[i][j] > dist[i][k] + dist[k][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    
    return dist;
}

int main()
{
    int road_nodes;
    int road_edges;
    
    cin >> road_nodes >> road_edges;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    vector<int> road_from(road_edges);
    vector<int> road_to(road_edges);
    vector<int> road_weight(road_edges);
    
    for (int i = 0; i < road_edges; i++) {
        cin >> road_from[i] >> road_to[i] >> road_weight[i];
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    
    int **dist = shortestPath(road_nodes, road_edges,
                              &road_from, &road_to, &road_weight);
    
    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    int x,y;
    for (int q_itr = 0; q_itr < q; q_itr++) {
        cin >> x >> y;
        int d = dist[x-1][y-1];
        if (d == MAXLIMIT)
            cout<<-1<<endl;
        else
            cout<<d<<endl;
    }
    
    return 0;
}
