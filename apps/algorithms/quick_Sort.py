#!/usr/bin/python3

from typing import List

class QuickSort:
    
    def sort(self, arr: List[int], low: int, high: int):
        if(low < high):
            currentArrSize: int = high-low + 1
            #medianOfArr: int = median(arr, low, high, medianOfArr)
            partitionIndex: int = self.partition(arr, low, high)

            self.sort(arr, low, partitionIndex-1)
            self.sort(arr, partitionIndex+1, high)

    def partition(self, arr: List[int], low: int, high: int):
        pivot = arr[high]

        i = low-1
        for j in range(low, high):
            if(arr[j] < pivot):
                i += 1
                self.swap(arr, i, j)
        self.swap(arr, i+1, high)
        return i+1
                
    def swap(self, arr: List[int], indexLow, indexHigh):
        buff: int = arr[indexLow]
        arr[indexLow] = arr[indexHigh]
        arr[indexHigh] = buff
    
    def dummy(self, name: str) -> str:
        return "Hello " + name

    def main(arr: List[int]) -> List[int]:
        sizeOfArr: int = len(arr)
        quickSort.sort(arr, 0, sizeOfArr-1)
        return arr
      
quickSort=QuickSort()
arr: List[int] = [1000, 10, 7, 8, 9, 30, 900, 1, 5, 6, 20]
sizeOfArr: int = len(arr)
quickSort.sort(arr, 0, sizeOfArr-1)
print("Sorted array :")
print(arr)

 