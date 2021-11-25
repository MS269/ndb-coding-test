#include <bits/stdc++.h>

using namespace std;

int dp[100];
int n;
vector<int> foods;

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        foods.push_back(x);
    }

    dp[0] = foods[0];
    dp[1] = max(foods[0], foods[1]);
    for (int i = 2; i < n; i++)
    {
        dp[i] = max(dp[i - 1], dp[i - 2] + foods[i]);
    }

    cout << dp[n - 1] << '\n';
}
