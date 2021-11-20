#include <bits/stdc++.h>

using namespace std;

string str;
vector<char> result;
int value = 0;

int main()
{
    cin >> str;

    for (int i = 0; i < str.size(); i++)
    {
        if (isalpha(str[i]))
        {
            result.push_back(str[i]);
        }
        else
        {
            value += str[i] - '0';
        }
    }

    sort(result.begin(), result.end());

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i];
    }
    if (value != 0)
    {
        cout << value;
    }
    cout << '\n';
}
