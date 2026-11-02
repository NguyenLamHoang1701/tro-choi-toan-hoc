/*#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>

int main() {
    double r =0.0;
    printf("nhap ban kinh: ");
    scanf("%lf",&r);
    double s=0.0;
    double sa =0.0;
    double v=0.0;
    
    printf("area = %.2lf\n",M_PI*pow(r,2));
    printf(" square area = %.2lf \n",M_PI*4*pow(r,2));
    printf("volume = %.2lf \n",M_PI*4/3*pow(r,3));    
    
    
    return 0;
}

*/

#include<stdio.h>
#include<math.h>

int main(){
    double p=0.0;
    double r=0.0;
    int y=0;
    int pt =0;
    printf("nhap tien von: ");
    scanf("%lf",&p);
    printf(":nhap  tien lai theo rate : ");
    scanf("%lf",&r);
    printf("nhap so  nam:");
    scanf("%d",&y);
    printf("Nhap   so lan  tinh lai moi nam:");
    scanf("%d",&pt);

    printf("tfddy %.2lf",p*pow((1+r/100),y*pt));


}
