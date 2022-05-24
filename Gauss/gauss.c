#include <math.h>
#include <stdio.h>

#define kernel_size 3 //5
#define sigma 1.0
#define K  1

int main() {
    double gauss[kernel_size][kernel_size];
    double sum = 0;
    int i, j;

    for (i = 0; i < kernel_size; i++) 
    {
        for (j = 0; j < kernel_size; j++) 
        {
            double x = i - (kernel_size - 1) / 2.0;
            double y = j - (kernel_size - 1) / 2.0;
            gauss[i][j] = K * exp(((pow(x, 2) + pow(y, 2)) / ((2 * pow(sigma, 2)))) * (-1));
            sum = sum + gauss[i][j];
        }
    }
    for (i = 0; i < kernel_size; i++) 
    {
        for (j = 0; j < kernel_size; j++) 
        {
            gauss[i][j] = gauss[i][j] / sum;
        }
    }
    for (i = 0; i < kernel_size; i++) 
    {
        for (j = 0; j < kernel_size; j++) 
        {
            printf("%f ", gauss[i][j]);
        }
        printf("\n");
    }
    return 0;
}
