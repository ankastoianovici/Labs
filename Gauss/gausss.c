#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MAX_WIDTH 512
#define MAX_HEIGHT 512
#define PADDING MAX_WIDTH*15

#define kernel_size 3 //7
#define sigma 1.0
#define K  1


void Gauss(unsigned char* in, unsigned char* out, int width, int height);

void main(){
    
   	FILE* inputImage  = fopen("intel/lena_512x512_luma.raw", "rb");
	FILE* outputImage = fopen("output_Blur_512x512_luma.raw", "wb");
    
	const int width = MAX_WIDTH;
	const int height = MAX_HEIGHT;

   	unsigned char* inputBuffer  = (unsigned char*)malloc(sizeof(unsigned char) * width * height + PADDING);
	unsigned char* outputBuffer = (unsigned char*)malloc(sizeof(unsigned char) * width * height + PADDING);
    
    
    unsigned int bytesLoaded = fread(inputBuffer, 1, width * height, inputImage);

   
    if(bytesLoaded!=width * height) {
        if(feof(inputImage)){
	        printf("EOF!"\n");
	    }
        if(ferror(inputImage)){
            printf("Eroare\n");
        }
        /*printf("Could not read from stream enough bytes.\n");
            printf("Expected %u, loaded %u bytes\n", width*height, bytesLoaded);
            exit(1);*/
    }
    
    int i,j;
    for(i=0; i<width; i++)
        for(j=0; j<15; j++)
            *(inputBuffer + (height+j)*width + i) = *(inputBuffer + (height-1)*width + i);
 
    Gauss(inputBuffer,outputBuffer,width,height);
   
    fwrite(outputBuffer, 1, sizeof(unsigned char) * width * height, outputImage);
	fclose(outputImage);
	
    free(inputBuffer);
	free(outputBuffer);
    fclose(inputImage);
}
void Gauss(unsigned char* in, unsigned char* out, int width, int height)
 {
    double gauss[kernel_size][kernel_size];
    double sum = 0;
    int i, j;
    for (i = 0; i < kernel_size; i++) 
    {
        for (j = 0; j < kernel_size; j++) 
        {
            double x = i - (kernel_size - 1) / 2.0;
            double y = j - (kernel_size - 1) / 2.0;
            gauss[i][j] = K * double exp(double ((double pow(double x, 2) + double pow(double y, 2)) / ((2 * double pow(double sigma, 2)))) * (-1)); //problema la exponentiala in linux
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
    return ;
