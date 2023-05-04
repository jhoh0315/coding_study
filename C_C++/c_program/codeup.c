//코드번호 1902

#include <stdio.h>

int rere(int n){
  printf("%d\n",n);
  if(n>1) rere(n-1);
}

int main(){
  int n;
  scanf("%d",&n);
  rere(n);
}