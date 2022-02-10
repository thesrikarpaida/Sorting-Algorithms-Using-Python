def insertionSort(lst):
    for i in range(len(lst) - 1):
        m = i + 1
        for j in range(i + 1):
            if lst[m] < lst[i - j]:
                lst[m], lst[i - j] = lst[i - j], lst[m]
                m = i - j


if __name__ == '__main__':
    print("-" * 10, "Using Insertion Sort", "-" * 10)
    # arr = list(map(int, input("Enter space separated integers:").split()))
    arr = [45, 2, 5, 24, 22, 42, 55, -6, 0, -76]
    print("Original list: ", arr)
    insertionSort(arr)
    print("Sorted list: ", arr)
