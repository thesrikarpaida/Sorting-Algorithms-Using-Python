def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


if __name__ == '__main__':
    print("-" * 10, "Using Bubble Sort", "-" * 10)
    # arr = list(map(int, input("Enter space separated integers:").split()))
    arr = [45, 2, 5, 24, 22, 42, 55, -6, 0, -76]
    print("Original list: ", arr)
    bubbleSort(arr)
    print("Sorted list: ", arr)
