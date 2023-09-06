//코드번호 1953

#include <stdio.h>

int d[201];

void drawstar(int n){
  printf("*");
  if(n != 1) drawstar(n-1);
}

void rere(int n){
  if(n!=1) rere(n-1);
  drawstar(n);
  printf("\n");
}

int main(){
  int a;
  scanf("%d",&a);
  rere(a);
}
