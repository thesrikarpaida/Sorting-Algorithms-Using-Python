def selectionSort(lst):
    for i in range(len(lst)):
        m = i
        for j in range(i+1, len(lst)):
            if lst[m] > lst[j]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]


if __name__ == '__main__':
    print("-" * 10, "Using Selection Sort", "-" * 10)
    # arr = list(map(int, input("Enter space separated integers:").split()))
    arr = [45, 2, 5, 24, 22, 42, 55, -6, 0, -76]
    print("Original list: ", arr)
    selectionSort(arr)
    print("Sorted list: ", arr)
