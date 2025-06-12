def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", data)
    bubble_sort(data)
    print("Sorted array:", data)