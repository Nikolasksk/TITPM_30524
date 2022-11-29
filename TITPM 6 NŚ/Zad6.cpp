#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;
string slownik[100];
int wiersze;
void readfile(string nazwa_pliku)
{
    string linia;
    ifstream plik(nazwa_pliku);›
    if( plik.good() == true )
    {
        while( !plik.eof() )
        {
            getline( plik, linia );
            wiersze++;
        }
        plik.close();
    }
    fstream file(nazwa_pliku, ios::in | ios::out);
     for(int i=0;i<wiersze;i++)
    {
            file>>slownik[i];
    }
}
struct ijk
{
    int i;
    int j;
    char m;
};
int main()
{
     readfile("slownik.txt");
     cout<<"Slownik"<<endl;
     for (int i = 0; i < wiersze-1; i++) {
            cout<<slownik[i]<<endl;
     }
     ijk kodzik[wiersze-2];
     cout<<"Ciąg: ";
     for(int i=0;i<wiersze-1;i++)
     {
         cin>>kodzik[i].i>>kodzik[i].j>>kodzik[i].m;
     }
     string wynik="";
     for(int i=0;i<wiersze-1;i++)
     {
         for(int j=kodzik[i].i;j<(kodzik[i].i+kodzik[i].j);j++)
         {
             wynik+=slownik[i][j];
         }
         wynik+=kodzik[i].m;
     }
     cout <<"Wynik: " << wynik;
    return 0;
}
