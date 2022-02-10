def partition(start, end, lst):
    p = start
    pivot = lst[p]

    while start < end:

        while start < len(lst) and lst[start] <= pivot:
            start += 1

        while lst[end] > pivot:
            end -= 1

        if start < end:
            lst[start], lst[end] = lst[end], lst[start]

    lst[p], lst[end] = lst[end], lst[p]
    return end


def quickSort(start, end, lst):
    if start < end:
        p = partition(start, end, lst)

        quickSort(start, p - 1, lst)
        quickSort(p + 1, end, lst)


if __name__ == '__main__':
    print("-" * 10, "Using Quick Sort", "-" * 10)
    # arr = list(map(int, input("Enter space separated integers:").split()))
    arr = [45, 2, 5, 24, 22, 42, 55, -6, 0, -76]
    print("Original list: ", arr)
    quickSort(0, len(arr) - 1, arr)
    print("Sorted list: ", arr)