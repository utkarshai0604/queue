#include <iostream> 
#include<bits/stdc++.h>
# program in c++ wwont run here but logic  is important
using namespace std;

bool fn(int a[][10],int i,int j,int n)
{
    
    for(int k=0;k<j;k++)
    { if(a[i][k]==1)
    return false; }
    
     for(int k=0;k<i;k++)
    { if(a[k][j]==1)
    return false; }
    
   for(int k=0;k<n;k++)
   {
    for(int l=0;l<n;l++)
    {
       
           if(a[k][l]==1 && (k+l==j+i || k-l==i-j))
           return false;
    }
       
   }
   return true;
}

vector<string> v;

void queen(int a[][10],int i,string s,int n)
{
    if(i>n-1)
    return;
    
    for(int j=0;j<n;j++)
    {
        if(fn(a,i,j,n))
        {
        a[i][j]=1;
        if(i<n-1)
        queen(a,i+1,s+to_string(j+1)+" ",n);
        
        if(i==n-1 )
        {
        s+=to_string(j+1)+" ] ";
        v.push_back(s);
        }
        a[i][j]=0;
        }
        
        
    }
    return;
}
int main() {
	int n,x;
	int a[10][10];
	cin>>n;
	for(int i=0;i<n;i++)
	{
	v.clear();
	cin>>x;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        a[i][j]=0;
    }
    queen(a,0,"[",x);
    if(v.size()==0)
    cout<<"-1";
    else
    {
    for(int i=0;i<v.size();i++)
    cout<<v[i];
    }
    cout<<endl;
	}
	return 0;
}