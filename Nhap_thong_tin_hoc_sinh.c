#include<stdio.h>
#include<string.h>
int main(){



int age = 0;
char name[100]="";
char classroom[10]="";

printf("Nhap o tuoi o day ");
scanf(" %d", &age);

getchar();// xoa ky tu xuong dong

printf("Nhap ten: ");
fgets(name,sizeof(name),stdin);
//fgets(name,100,stdin);
name[strlen(name)-1]='\0';

printf("Nhap ten lop hoc: ");
fgets(classroom,sizeof(classroom),stdin);  
//fgets(classroom,10,stdin);  
//------- THONG TIN HOC SINH------------
printf(" Thong tin hoc  sinh \n");
printf("Ho va ten: %s ",name);
printf("Hoc sinh lop %s \n",classroom);
printf("Tuoi :%d \n", age);
    


    return 0;
}