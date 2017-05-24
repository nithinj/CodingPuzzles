#include <iostream>
#include <set>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <utility>

#define ulong unsigned long
#define uint unsigned int

using namespace std;

map <uint, vector<uint> > adj;
map <uint, int> visited;
ulong subgraph_size = 0;

void dfs(uint node) {
    ulong i;
    visited[node] = 1;
    subgraph_size++;
    for (i=0; i<adj[node].size(); i++) {
        if (!visited[adj[node][i]])
            dfs(adj[node][i]);
    }
}


int main() {
    ulong queries;
    ulong cities, roads, clib, croad;
    uint u, v;
    ulong i,j;
    vector<uint> vec;
    map <uint, vector<uint> >::iterator it;
    ulong cost;
    vector<ulong> result;
    ulong graph_total;
    //	start_time = time(0);
    cin>>queries;
    for (i = 0; i < queries; i++) {
        cin >> cities >> roads >> clib >> croad;
        for (j = 0; j < roads; j++) {
            cin >> u >> v;
            if (clib <= croad || roads == 0)
                continue;
            if (adj.find(u) == adj.end()) {
                vec.push_back(v);
                adj[u] = vec;
                vec.clear();
                visited[u] = 0;
            } else
                adj[u].push_back(v);
            if (adj.find(v) == adj.end()) {
                vec.push_back(u);
                adj[v] = vec;
                vec.clear();
                visited[v] = 0;
            } else
                adj[v].push_back(u);
        }
        cost = 0;
        graph_total = 0;
        if (clib <= croad || roads == 0)
            cost = cities*clib;
        else {
            for (it=adj.begin(); it!=adj.end(); it++) {
                if(!visited[it->first]) {
                    dfs(it->first);
                    cost += (subgraph_size-1)*croad + clib;
                    graph_total += subgraph_size;
                }
                subgraph_size = 0;
            }
        cost += (cities - graph_total) * clib;
        }
        result.push_back(cost);
        adj.clear();
        visited.clear();
    }
    for (i=0; i<result.size(); i++)
        cout<<result[i] <<"\n";
}
