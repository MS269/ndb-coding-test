#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> currencies;

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        currencies.push_back(x);
    }

    vector<int> dp(m + 1, 10001);

    dp[0] = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = currencies[i]; j <= m; j++)
        {
            if (dp[j - currencies[i]] != 10001)
            {
                dp[j] = min(dp[j], dp[j - currencies[i]] + 1);
            }
        }
    }

    if (dp[m] == 10001)
    {
        cout << -1 << '\n';
    }
    else
    {
        cout << dp[m] << '\n';
    }
}
