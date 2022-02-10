def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2

        L = lst[:mid]
        R = lst[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    print("-" * 10, "Using Merge Sort", "-" * 10)
    # arr = list(map(int, input("Enter space separated integers:").split()))
    arr = [45, 2, 5, 24, 22, 42, 55, -6, 0, -76]
    print("Original list: ", arr)
    mergeSort(arr)
    print("Sorted list: ", arr)