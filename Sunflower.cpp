#include <iostream>
#include <graphics.h>
#include <cmath>
using namespace std;

int n = 0;
int c = 4;

int draw();

int main()
{
    initwindow(400, 400, "Sunflower", 400, 150);
    draw();
    getch();
    closegraph();
    return 0;
}

int draw()
{
    if(n==1000) return 0;
    float a = n * 137.5; // * (180/3.1415);
    float r = c * sqrt(n);
    int x = (int) ( r * cos(a) + 200 );
    int y = (int) ( r * sin(a) + 200 );
    setcolor(n);
    circle(x, y, 4);
    n++;
    delay(5);
    draw();
}
