import pytest
from apps.quick_Sort import QuickSort
from typing import List

class Test_Quick_Sort():
    def test_quick_dummy(self):
        qs = QuickSort
        output = qs.dummy(self,"Girish")
        assert output == "Hello Girish"

    def test_quick_main_1(self):
        qs = QuickSort
        arr: List[int] = [1000, 10, 7, 8, 9, 30, 900, 1, 5, 6, 20]
        sortArr: List[int] = [1, 5, 6, 7, 8, 9, 10, 20, 30, 900, 1000]       
        currentArr = qs.main(arr)
        assert currentArr == sortArr
        