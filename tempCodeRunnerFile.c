
#include <stdio.h>


void binarySearch(int arr[], int low, int high, int x){
int mid;
    while (low <= high) {
        mid = low + (high - low) / 2;

      
        if (arr[mid] == x){
           printf("THe index is%d\n",mid);
           return ;}

      
        else if (arr[mid] < x){
            low = mid + 1;

       printf("1\n");}
        else{
            high = mid - 1;
    printf("2\n");

   
        }
        
}

}


int main()
{
    int arr[] = {2,3,4,10,40 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x =40;
    binarySearch(arr, 0, n - 1, x);
    // (result == -1) ? printf("Element is not present"
    //                         " in array")
    //                : printf("Element is present at "
    //                         "index %d",
    //                         result);
    return 0;
}

// #include<stdio.h>
// int binarysearch(int arr[],int high, int low, int x){
//     while(low <= high){
//         int mid = low + (high-low)/2;
//         if(arr[mid]==x)
//         return mid;
//         if(arr[mid]<x)
//         low = mid + 1;
//         else
//         high = mid - 1;
//     }
//     return -1;
// }
// int main(void){
//     int arr[] = {2,6,8,9,4};
//     int n = sizeof(arr)/sizeof(arr[0]);
//     int x = 9;
//     int result = binarysearch(arr,0,n-1,x);
//     (result==-1)
//         ? printf("Element is not found.")
//         : printf("Element at index:%d",result);
//     return 0;
//     }