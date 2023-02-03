#include <stdio.h>
#include <stdlib.h>
int main()
{
    int* x;
    x = (int*)malloc(4*sizeof(int));
     *x = 34;
    print("the value is: %d\n", *x);
    int* y = x;
    print("before update: %d\n", *y);
    *x = 20;
    print("After update: %d\n ", *y);
    free(x);
    x = NULL;
    y = NULL;
    print("After freeing: %d\n",*y);

    return 0;
}