#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    vector<int> c(N), t(N);

    for (int i = 0; i < N; i++) {
        cin >> c[i];
    }

    for (int i = 0; i < N; i++) {
        cin >> t[i];
    }

    vector<pair<int, int>> farms;
    for (int i = 0; i < N; i++) {
        farms.push_back({c[i], t[i]});
    }

    sort(farms.begin(), farms.end());

    for (int i = 0; i < Q; i++) {
        int V, S;
        cin >> V >> S;

        int count = 0;
        for (int j = 0; j < N; j++) {
            if (farms[j].second <= S && farms[j].first >= S && count < V) {
                count++;
            }
        }

        if (count >= V) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
