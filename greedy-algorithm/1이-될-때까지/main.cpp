#include <bits/stdc++.h>

using namespace std;

int n, k;
int result;

int main()
{
    cin >> n >> k;

    while (true)
    {
        int target = (n / k) * k;
        result += (n - target);
        n = target;

        if (n < k)
        {
            break;
        }

        n /= k;
        result += 1;
    }

    result += (n - 1);
    cout << result << '\n';
}
