class Sorting:
    @staticmethod
    def bubble_sort(array):
        isSorted: bool
        for i in range(len(array)):
            isSorted = True
            for j in range(1, len(array) - i):
                if array[j] < array[j - 1]:
                    isSorted = False
                    Sorting.__swap(j, j - 1, array)
            if isSorted:
                return

    @staticmethod
    def selection_sort(array):
        for i in range(len(array)):
            min_index = i
            for j in range(i, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            Sorting.__swap(min_index, i, array)

    @staticmethod
    def insertion_sort(array):
        for i in range(len(array)):
            current = array[i]
            j = i - 1
            while j >= 0 and array[j] > current:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = current

    @staticmethod
    def merge_sort(array):
        if len(array) < 2:
            return
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:len(array)]

        Sorting.merge_sort(left)
        Sorting.merge_sort(right)

        Sorting.__merge(left=left, right=right, array=array)

    @staticmethod
    def quick_sort(array):
        Sorting.__quick_sort(array=array,start=0, end=len(array) - 1)

    @staticmethod
    def __quick_sort(array, start, end):
        if start > end:
            return
        boundary = Sorting.__partition(array=array, start=start, end=end)

        Sorting.__quick_sort(array=array, start=start, end=boundary - 1)
        Sorting.__quick_sort(array=array, start=boundary + 1, end=end)


    @staticmethod
    def __partition(array, start, end):
        pivot = array[end]
        boundary = start - 1
        for i in range(start, end + 1):
            if array[i] <= pivot:
                boundary += 1
                Sorting.__swap(first=boundary, second=i, array=array)
        return boundary



    @staticmethod
    def __merge(left, right, array):
        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
                c += 1
            else:
                array[c] = right[b]
                b += 1
                c += 1

        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1

    @staticmethod
    def __swap(first: int, second: int, array: list):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp
