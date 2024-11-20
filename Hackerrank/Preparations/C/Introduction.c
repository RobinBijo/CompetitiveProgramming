// PROGRAM 1 - Hello World! in C
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
    printf("Hello, World! \n");
    printf("%s",s);
    
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
//-------------------------------------------------------------------------------
//PROGRAM 2 - Playing With Characters
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char s[100];
    char sen[100];
    scanf("%c\n",&ch);
    scanf("%s\n",&s);    
    scanf("%[^\n]%*c",&sen);
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s\n",sen);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
//-------------------------------------------------------------------------------
//PROGRAM 3 - Sum and Difference of Two Numbers
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int m;int n;
    float k; float l;
    scanf("%d %d",&m,&n);
    scanf("%f %f",&k,&l);
    int Iadd = m+n;
    int Isub = m-n;
    float fadd = k+l;
    float fsub = k-l;
    printf("%d %d\n",Iadd,Isub);
    printf("%0.1f %0.1f",fadd,fsub);// Rounding off to one decimal point
	
    
    return 0;
}
//--------------------------------------------------------------------------------
//PROGRAM 4 - Functions in C
#include <stdio.h>
int max_of_four(int a, int b, int c, int d){
    if (a>b && a>c && a>d){
        return a;
    }
    else if (b>c && b>d){
        return b;
    }
    else if (c>d){
        return c;
    }
    else{
        return d;
    }
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
