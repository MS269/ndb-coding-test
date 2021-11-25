#include <bits/stdc++.h>

using namespace std;

int testCase, n, m;
int dp[20][20];

int main()
{
    cin >> testCase;
    for (int tc = 0; tc < testCase; tc++)
    {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> dp[i][j];
            }
        }

        for (int j = 1; j < m; j++)
        {
            for (int i = 0; i < n; i++)
            {
                int leftUp = 0, leftDown = 0, left = 0;

                if (i != 0)
                {
                    leftUp = dp[i - 1][j - 1];
                }

                if (i != n - 1)
                {
                    leftDown = dp[i + 1][j - 1];
                }

                left = dp[i][j - 1];

                dp[i][j] += max(leftUp, max(leftDown, left));
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++)
        {
            result = max(result, dp[i][m - 1]);
        }
        cout << result << '\n';
    }
}
