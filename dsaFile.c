#include <iostream>
using namespace std;

int findMax(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int arr[] = {12, 34, 45, 9, 8, 76, 23};
    int size = sizeof(arr) / sizeof(arr[0]);
    int maximum = findMax(arr, size);

    cout << "The maximum element in the array is: " << maximum << endl;

    return 0;
}
