//
//  walking_the_approximate_longest_path.cpp
//  walking_the_approximate_longest_path
//
//  Created by Nithin Johnson on 10/29/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <set>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <utility>
#include <algorithm>

#define ulong unsigned long
#define uint unsigned int

using namespace std;

map <uint, vector<uint> > adj;
map <uint, int> visited;
ulong subgraph_size = 0;
vector<uint> current_path;
size_t *min_list;
map <size_t, vector<uint> > size_map;
ulong cities, roads;
map <uint, vector<uint> >::iterator it;

void dfs(uint node) {
    ulong i;
    uint next_node = adj.begin()->first;
    visited[node] = 1;
    subgraph_size++;
    current_path.push_back(node);
    size_t min_size = ~0;
    for (i=0; i<adj[node].size(); i++) {
        if ((adj[adj[node][i]].size() < min_size) && !visited[adj[node][i]]) {
            next_node = adj[node][i];
            min_size = adj[adj[node][i]].size();
        }
    }
    if (!visited[next_node])
        dfs(next_node);
}

void re_initialize_visited() {
    for (it=adj.begin(); it!=adj.end(); ++it)
        visited[it->first] = 0;
}


int main() {
    uint u, v;
    ulong i,j;
    ulong result = 0;
    vector<uint> result_path;
    size_t size = 0;
    
    cin >> cities >> roads;
    for (i = 0; i < roads; i++) {
        cin >> u >> v;
        adj[u].push_back(v);
        visited[u] = 0;
        adj[v].push_back(u);
        visited[v] = 0;
    }
    
    subgraph_size = 0;
    min_list = new size_t[cities];
    i=0;
    
    // we need to sort the value based on (it->second).size in order to convince hacker rank !!
    for (it=adj.begin(); it!=adj.end(); ++it) {
        size = (it->second).size();
        min_list[i++] = size;
        size_map[size].push_back(it->first);
    }
    
    sort(min_list, min_list + cities);
    
    for(i=0; i<cities; i++) {
        for (j=0; j<size_map[min_list[i]].size(); j++) {
            dfs(size_map[min_list[i]][j]);
            if (result < subgraph_size) {
                result = subgraph_size;
                result_path = current_path;
            }
            if (result == cities) {
                cout<<result <<"\n";
                for (i = 0; i < result_path.size(); i++)
                    cout<<result_path[i]<<" ";
                delete[] min_list;
                return 0;
            }
            
            subgraph_size = 0;
            current_path.clear();
            re_initialize_visited();
        }
    }
    
    cout<<result <<"\n";
    for (i=0; i<result_path.size(); i++)
        cout<<result_path[i]<<" ";
    delete[] min_list;
}

