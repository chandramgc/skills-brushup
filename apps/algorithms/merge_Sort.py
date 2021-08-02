from typing import List

class Merge_Sort:
    def mergesort(self, arr: List[int]):
        if(len(arr) > 1):      
            middle: int=  len(arr)//2
            # print(middle)
            leftArray: List[int] = arr[:middle]
            rightArray: List[int] = arr[middle:]
            self.mergesort(leftArray)
            self.mergesort(rightArray)
            self.merge(arr, leftArray,rightArray)

    def merge(self, arr: List[int], leftArray: List[int], rightArray: List[int]):
        leftArrayIndex: int = 0
        rightArrayIndex: int = 0
        mergeSortIndex: int = 0

        while(leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray)):
            # print("mergeSortIndex: "+ str(mergeSortIndex) +",leftArray[leftArrayIndex]: "+ str(leftArray[leftArrayIndex]) +",rightArray[rightArrayIndex]: "+ str(rightArray[rightArrayIndex]))
            
            if(leftArray[leftArrayIndex] < rightArray[rightArrayIndex]):
                arr[mergeSortIndex] = leftArray[leftArrayIndex]
                leftArrayIndex += 1
            else:
                arr[mergeSortIndex] = rightArray[rightArrayIndex]
                rightArrayIndex += 1
            mergeSortIndex += 1
        
        while(rightArrayIndex < len(rightArray)):
            # print("rightArrayIndex: "+ str(mergeSortIndex) +",rightArray[rightArrayIndex]: "+ str(rightArray[rightArrayIndex])+",arr[mergeSortIndex]: "+ str(arr[mergeSortIndex]))
       
            arr[mergeSortIndex] = rightArray[rightArrayIndex]
            rightArrayIndex += 1
            mergeSortIndex += 1

        while(leftArrayIndex < len(leftArray)):
            # print("leftArrayIndex: "+ str(mergeSortIndex) +",leftArray[leftArrayIndex]: "+ str(leftArray[leftArrayIndex])+",arr[mergeSortIndex]: "+ str(arr[mergeSortIndex]))
       
            arr[mergeSortIndex] = leftArray[leftArrayIndex]
            leftArrayIndex += 1
            mergeSortIndex += 1

    

mergesort = Merge_Sort()
arr: List[int] = [1000, 10, 7, 8, 9, 30, 900, 1, 5, 6, 20]
mergesort.mergesort(arr)
print("Sorted array :")
print(arr)
