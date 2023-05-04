//코드번호 1901

#include <stdio.h>

int rere(int n){
  if(n>1) rere(n-1);
  printf("%d\n",n);
}

int main(){
  int n;
  scanf("%d",&n);
  rere(n);
}