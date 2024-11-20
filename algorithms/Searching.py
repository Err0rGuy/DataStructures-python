class Searching:
    @staticmethod
    def linear_search(array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1

    @staticmethod
    def binary_search(array, target):
        return Searching.__binary_search(array=array, target=target, left=0, right=len(array))

    @staticmethod
    def __binary_search(array, target, left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        if target == array[middle]:
            return middle

        elif target < array[middle]:
           return Searching.__binary_search(array=array, target=target, left=left, right=middle - 1)

        return Searching.__binary_search(array=array, target=target, left=middle + 1, right=right)

    @staticmethod
    def ternary_search(array, target):
        return Searching.__ternary_search(array=array, target=target, left=0, right=len(array) - 1)

    @staticmethod
    def __ternary_search(array, target, left, right):
        if left > right:
            return -1
        part_size = (right - left) // 3
        middle1 = left + part_size
        middle2 = right - part_size
        if target == array[middle1]:
            return middle1
        elif target == array[middle2]:
            return middle2

        elif target < array[middle1]:
            return Searching.__ternary_search(array, target, left, middle1 - 1)

        elif target > array[middle2]:
            return Searching.__ternary_search(array, target, middle2 + 1, right)

        return Searching.__ternary_search(array, target, middle1 + 1, middle2 - 1)

