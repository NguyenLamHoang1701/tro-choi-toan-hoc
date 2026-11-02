#include<stdio.h>
#include<string.h>
int main(){
    char item[50] ="";
    printf(" What do yu want to buy: ");
    fgets(item,sizeof(item),stdin);
    item[strlen(item)-1]='\0';

    float price=0.0f;
    printf("What is the price for each?: ");
    scanf("%f",&price);

    int count =0;
    printf("How many would u buy:");
    scanf("%d",&count);

    float total = price * count;
    char currency='$';
    printf("u have bought %d %s\n",count,item);
    item[strlen(item)-1]='\0';
    printf("The total is %c%.2f",currency,total);



    return 0;
}