#include <iostream>
#include <vector>
#include <conio.h>
#include <cstring>
#include <fstream>
using namespace std;
int a[10][15]{};
vector <pair<int,int> > v;
int show[14][6][10]{};
int oper[14]{};
long long int c = 0;
ofstream c2("可能的解(含不同方向).txt");
void sh(int mov){
    for (int j=1;j<=5;j++){
        for (int k=1;k<=9;k++){
            if (a[j][k]==1)
                show[mov][j][k] = 1;
            else
            	if (a[j][k]==2)
           		 	show[mov][j][k] = 2;
           		else
            		show[mov][j][k] = 0;
        }
    }
}
void dfs(int y,int x,int mov){
	a[y][x] = 2;//沒東西了 (0:沒格子，1:有東西 
    v.push_back({y,x});
    sh(mov);
    if (v.size()==14){
    	//if (!(c%1000)){//輸出 
	    	c2 << c+1 << ':' << endl;
	    	for (int j=1;j<=5;j++){
				for (int i=0;i<7;i++){
	    			for (int k=1;k<=9;k++){
	    				if (show[i][j][k]==1)
	    					c2 << 'O';
	    				else
	    					if (show[i][j][k]==2)
	    						c2 << 'X';
	    					else 
	    						c2 << ' ';
					}
					c2 << "  ";
				}
				c2 << endl;
			}
			c2 << endl;
			for (int j=1;j<=5;j++){
				for (int i=7;i<14;i++){
	    			for (int k=1;k<=9;k++){
	    				if (show[i][j][k]==1)
	    					c2 << 'O';
	    				else
	    					if (show[i][j][k]==2)
	    						c2 << 'X';
	    					else 
	    						c2 << ' ';
					}
					c2 << "  ";
				}
				c2 << endl;
			}
			c2 << endl;
		//	getch();
		//}
        c ++;
        a[y][x] = true;
        v.pop_back();
        return;
    }
    for (int i=0;i<v.size();i++){
        int bufy = v[i].first, bufx = v[i].second ;
        if (bufy-2>=1&&bufx-2>=1)
            if (a[bufy-1][bufx-1]==1){//up left  1
                if (a[bufy-2][bufx-2]==1){
                    a[bufy-2][bufx-2] = 2;
                    a[bufy][bufx] = true;
                    v.erase(v.begin()+i);
                    v.push_back({bufy-2,bufx-2});
                    oper[mov] = 1;
                    dfs(bufy-1,bufx-1,mov+1);
                    a[bufy][bufx] = 2;
                    a[bufy-2][bufx-2] = true;
                    v.pop_back();
                    v.insert(v.begin()+i,{bufy,bufx});
                }
        }
        if (a[bufy+1][bufx+1]==1){//down right 2
            if (a[bufy+2][bufx+2]==1){
                a[bufy+2][bufx+2] = 2;
                a[bufy][bufx] = true;
                v.erase(v.begin()+i);
                v.push_back({bufy+2,bufx+2});
                oper[mov] = 2;
                dfs(bufy+1,bufx+1,mov+1);
                a[bufy][bufx] = 2;
                a[bufy+2][bufx+2] = true;
                v.pop_back();
                v.insert(v.begin()+i,{bufy,bufx});
            }
        }
        if (bufx>=1)
            if (a[bufy+1][bufx-1]==1){//down left 3
                if (a[bufy+2][bufx-2]==1){
                    a[bufy+2][bufx-2] = 2;
                    a[bufy][bufx] = true;
                    v.erase(v.begin()+i);
                    v.push_back({bufy+2,bufx-2});
                    oper[mov] = 3;
                    dfs(bufy+1,bufx-1,mov+1);
                    a[bufy][bufx] = 2;
                    a[bufy+2][bufx-2] = true;
                    v.pop_back();
                    v.insert(v.begin()+i,{bufy,bufx});
                }
            }
        if (bufy-2>=1)
            if (a[bufy-1][bufx+1]==1){//up right 4
                if (a[bufy-2][bufx+2]==1){
                    a[bufy-2][bufx+2] = 2;
                    a[bufy][bufx] = true;
                    v.erase(v.begin()+i);
                    v.push_back({bufy-2,bufx+2});
                    oper[mov] = 4;
                    dfs(bufy-1,bufx+1,mov+1);
                    a[bufy][bufx] = 2;
                    a[bufy-2][bufx+2] = true;
                    v.pop_back();
                    v.insert(v.begin()+i,{bufy,bufx});
                }
            }
        //left and right
        if (bufx+4<=9)
            if (a[bufy][bufx+2]==1){//right 5
                if (a[bufy][bufx+4]==1){
                    a[bufy][bufx+4] = 2;
                    a[bufy][bufx] = true;
                    v.erase(v.begin()+i);
                    v.push_back({bufy,bufx+4});
                    oper[mov] = 5;
                    dfs(bufy,bufx+2,mov+1);
                    a[bufy][bufx] = 2;
                    a[bufy][bufx+4] = true;
                    v.pop_back();
                    v.insert(v.begin()+i,{bufy,bufx});
                }
            }
        if (bufx-4>=1)
            if (a[bufy][bufx-2]==1){//left 6
                if (a[bufy][bufx-4]==1){
                    a[bufy][bufx-4] = 2;
                    a[bufy][bufx] = true;
                    v.erase(v.begin()+i);
                    v.push_back({bufy,bufx-4});
                    oper[mov] = 6;
                    dfs(bufy,bufx-2,mov+1);
                    a[bufy][bufx] = 2;
                    a[bufy][bufx-4] = true;
                    v.pop_back();
                    v.insert(v.begin()+i,{bufy,bufx});
                }
            }
    }
    a[y][x] = true;
    v.pop_back();
}
int main(){
    a[1][5] = true;
    a[2][4] = true;
    a[2][6] = true;
    a[3][3] = true;
    a[3][5] = true;
    a[3][7] = true;
    for (int i=4;i<=5;i++){
        if (!(i%2)){
            for (int j=2;j<=9;j+=2){
                a[i][j] = true;
            }
        }else
            for (int j=1;j<=9;j+=2){
                a[i][j] = true;
            }
    }
    v.clear();
   // dfs(1,5,0);//第1排第1個
   // dfs(2,4,0);//第2排第1個
    //dfs(2,6,0);//第2排第2個
    //dfs(3,3,0);//第3排第1個
    dfs(3,5,0);//第3排第3個
    /*dfs(3,7,0);//以此類推.......
    dfs(4,2,0);
    dfs(4,4,0);
    dfs(4,6,0);
    dfs(4,8,0);
    dfs(5,1,0);
    dfs(5,3,0);
    dfs(5,5,0);
    dfs(5,7,0);
    dfs(5,9,0);*/
    cout << c << endl;
    c2.close();
    return 0;
}
