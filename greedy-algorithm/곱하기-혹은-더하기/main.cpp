#include <bits/stdc++.h>

using namespace std;

string str;

int main()
{
    cin >> str;

    long long result = str[0] - '0';

    for (int i = 1; i < str.size(); i++)
    {
        int num = str[i] - '0';
        if (num <= 1 || result <= 1)
        {
            result += num;
        }
        else
        {
            result *= num;
        }
    }

    cout << result << '\n';

    return 0;
}
