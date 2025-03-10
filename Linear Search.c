#include<stdio.h>
int Linearsearch(int arr[],int n,int x)
{
    for(int i=0; i<n; i++)
        if( arr[i]==x )
        return i;
    
    return -1;
}
int main(void){
    int arr[] = {12,32,65,1,48,94};
    int x = 12;
    int n = sizeof(arr)/sizeof(arr[0]);
    int result = Linearsearch(arr,n,x);
    (result ==-1)
    ? printf("Elememt is not present in arrey.")
    : printf("Element is presenet at index %d",result);
    return 0;
}

// #include <stdio.h>

// int search(int arr[], int N, int x)
// {
//     for (int i = 0; i < N; i++)
//         if (arr[i] == x)
//             return i;
//     return -1;
// }

// // Driver code
// int main(void)
// {
//     int arr[] = { 2, 3, 4, 10, 40 };
//     int x = 10;
//     int N = sizeof(arr) / sizeof(arr[0]);

//     // Function call
//     int result = search(arr, N, x);
//     (result == -1)
//         ? printf("Element is not present in array")
//         : printf("Element is present at index %d", result);
//     return 0;
// }