from math import pow
from time import time


class Sorter:
    def measure_time(func):
        def wrapper(self, items, *args):

            start = time()
            sorted_arr = func(self, items)
            end = time()

            result_time = round(end - start, 5)

            return result_time, sorted_arr

        return wrapper

    @measure_time
    def bubble_sort(self, items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items

    @measure_time
    def insertion_sort(self, items):
        for i in range(1, len(items)):
            j = i
            while j > 0 and items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]
                j -= 1
        return items

    @measure_time
    def selection_sort(self, items):
        for i in range(len(items)):
            min_index = i
            for j in range(i + 1, len(items)):
                if items[j] < items[min_index]:
                    min_index = j
            items[i], items[min_index] = items[min_index], items[i]
        return items

    # merge sort without recursion
    @measure_time
    def merge_sort(self, items):
        if len(items) <= 1:
            return items

        middle = len(items) // 2
        left = items[:middle]
        right = items[middle:]

        left_index = 0
        right_index = 0
        result = []

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]

        return result

    @measure_time
    def quick_sort(self, nums):
        import random

        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in nums:
                if n < q:
                    s_nums.append(n)
                elif n > q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return (
                list(self.quick_sort(s_nums))
                + list(e_nums)
                + list(self.quick_sort(m_nums))
            )

    def get_timings(self, items):
        return {
            "Bubble sort": self.bubble_sort(items)[0],
            "Insertion sort": self.insertion_sort(items)[0],
            "Selection sort": self.selection_sort(items)[0],
            "Merge sort": self.merge_sort(items)[0],
            "Quick sort": self.quick_sort(items, 0, len(items))[0],
        }
