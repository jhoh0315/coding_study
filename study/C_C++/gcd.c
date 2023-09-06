#include <stdio.h>

int gcd(int a, int b){
    if(!b) return a;
    return gcd(b, a%b);
}

int main(){
    int a,b,res;
    scanf("%d %d",&a, &b);
    res=gcd(a,b);
    printf("%d %d",res,a/res*b);
}