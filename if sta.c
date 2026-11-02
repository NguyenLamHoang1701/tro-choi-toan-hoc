#include<stdio.h>
#include<string.h>
int main(){
    
    char name[50] ="";


    printf("Enter name:");
    fgets(name,sizeof(name),stdin);
    name[strlen(name)-1]='\0';
    if(strlen(name)==0){
        printf("Nhap lai!!!");
    }
    else{
        printf("ten cua ban la %s",name);
    }



    return 0;
}