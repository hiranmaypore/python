#include<stdio.h>
void swap(int *p1, int *p2){
    int temp;
    temp= *p1;
    *p1 = *p2;
    *p2 = temp;
}
int partition(int arr[],int low, int high){
    int pivot = arr[high];
    int i = (low-1);
    for(int j=low;j<=high;j++){
       if(arr[j]<pivot){
         i++;
        swap(&arr[i],&arr[j]);
       }
    }
    swap(&arr[i+1],&arr[high]);
    return i+1;
}
void quicksort(int arr[],int low,int high){
    if(low<high){
    int pi = partition(arr,low,high);
    quicksort(arr,low,pi-1);
    quicksort(arr,pi+1,high);
    }
}
int main(){
    int arr[]={45,62,15,30,49};
    int n = sizeof(arr)/sizeof(arr[0]);
    quicksort(arr,0,n-1);
    for(int i=0; i<n ; i++){
    printf("%d ",arr[i]);
    }
    return 0;
}
