#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>
#include <cstdlib>

using namespace std;

int count_points(double x, double y, const vector<pair<int,int>> &cows) {
    int q1 = 0, q2 = 0, q3 = 0, q4 = 0;
    for (const auto &c : cows) {
        if (c.first > x && c.second > y)
            q1++;
        else if (c.first < x && c.second > y)
            q2++;
        else if (c.first < x && c.second < y)
            q3++;
        else
            q4++;
    }
    return max({q1, q2, q3, q4});
}

int count_points_x(double x, const vector<pair<int,int>> &cows) {
    int q1 = 0, q2 = 0;
    for (const auto &c : cows) {
        if (c.first > x)
            q1++;
        else
            q2++;
    }
    return abs(q1 - q2);
}

int count_points_y(double y, const vector<pair<int,int>> &cows) {
    int q1 = 0, q3 = 0;
    for (const auto &c : cows) {
        if (c.second > y)
            q1++;
        else
            q3++;
    }
    return abs(q1 - q3);
}

int solve(int N, const vector<pair<int,int>> &cows) {
    vector<int> x_vals, y_vals;
    x_vals.reserve(N);
    y_vals.reserve(N);
    for (int i = 0; i < N; i++) {
        x_vals.push_back(cows[i].first);
        y_vals.push_back(cows[i].second);
    }
    
    sort(x_vals.begin(), x_vals.end());
    sort(y_vals.begin(), y_vals.end());

    // Store candidate midpoints by comparing adjacent values.
    // Each pair: <index in sorted order, difference count>
    vector<pair<int,int>> x_res, y_res;
    for (int i = 1; i < N; i++) {
        double xMid = ((double)x_vals[i] - x_vals[i - 1]) / 2.0 + x_vals[i - 1];
        x_res.push_back({i, count_points_x(xMid, cows)});
    }
    for (int i = 1; i < N; i++) {
        double yMid = ((double)y_vals[i] - y_vals[i - 1]) / 2.0 + y_vals[i - 1];
        y_res.push_back({i, count_points_y(yMid, cows)});
    }
    
    // Sort candidates by their count difference
    sort(x_res.begin(), x_res.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
        return a.second < b.second;
    });
    sort(y_res.begin(), y_res.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
        return a.second < b.second;
    });
    
    int xCount = min(700, (int)x_res.size());
    int yCount = min(700, (int)y_res.size());
    
    vector<int> x_final(xCount), y_final(yCount);
    for (int i = 0; i < xCount; i++) {
        int index = x_res[i].first;
        x_final[i] = x_vals[index];
    }
    for (int i = 0; i < yCount; i++) {
        int index = y_res[i].first;
        y_final[i] = y_vals[index];
    }
    
    sort(x_final.begin(), x_final.end());
    sort(y_final.begin(), y_final.end());
    
    int result = numeric_limits<int>::max();
    // Try all pairs of adjacent candidate midpoints to find the optimal balance.
    for (int i = 1; i < (int)x_final.size(); i++) {
        double xMid = ((double)x_final[i] - x_final[i - 1]) / 2.0 + x_final[i - 1];
        for (int j = 1; j < (int)y_final.size(); j++) {
            double yMid = ((double)y_final[j] - y_final[j - 1]) / 2.0 + y_final[j - 1];
            int cur = count_points(xMid, yMid, cows);
            result = min(result, cur);
        }
    }
    
    return result;
}

int main() {
    ifstream fin("balancing.in");
    ofstream fout("balancing.out");
    
    int N;
    fin >> N;
    vector<pair<int,int>> cows(N);
    for (int i = 0; i < N; i++) {
        fin >> cows[i].first >> cows[i].second;
    }
    fin.close();
    
    int result = solve(N, cows);
    
    fout << result << "\n";
    fout.close();
    return 0;
}
