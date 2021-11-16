#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> arr;

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    sort(arr.begin(), arr.end());

    int result = 0;
    int cnt = 0;

    for (int i = 0; i < n; i++)
    {
        cnt += 1;

        if (cnt >= arr[i])
        {
            result += 1;
            cnt = 0;
        }
    }

    cout << result << '\n';

    return 0;
}
