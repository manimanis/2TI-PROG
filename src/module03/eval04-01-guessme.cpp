#include <iostream>

using namespace std;

int main()
{
    int n1, n2, u1, d1, u2, d2, score;
    srand(time(NULL));
    cout << "Choisir un nbre [10, 99] ? ";
    cin >> n1;
    u1 = n1 % 10;
    d1 = n1 / 10;
    n2 = rand() % 90 + 10;
    u2 = n2 % 10;
    d2 = n2 / 10;
    if (n1 == n2)
    {
        score = 200;
    }
    else if (u1 == d2 && d1 == u2)
    {
        score = 100;
    }
    else if (u1 == d2 || d1 == u2 || u1 == u2 || d1 == d2)
    {
        score = 50;
    }
    else 
    {
        score = 0;
    }
    cout << "L'ordinateur a choisi : " << n2 << endl;
    cout << "Score : " << score << endl;
    system("pause");
    return 0;
}