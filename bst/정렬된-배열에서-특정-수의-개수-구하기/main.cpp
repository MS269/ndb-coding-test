#include <bits/stdc++.h>

using namespace std;

int n, x;
vector<int> v;

int main()
{
    cin >> n >> x;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }

    auto lower = lower_bound(v.begin(), v.end(), x);
    auto upper = upper_bound(v.begin(), v.end(), x);

    int result = upper - lower;
    cout << (result == 0 ? -1 : result);
}
