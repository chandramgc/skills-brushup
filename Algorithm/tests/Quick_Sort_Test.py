import pytest
from apps.Quick_Sort import QuickSort

class Quick_Sort_Test:
    def test_quick(self):
        qs = QuickSort
        output = qs.dummy("Girish")
        assert output == "Hello Girish"