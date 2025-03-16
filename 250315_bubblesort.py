def bubble_sort(arr):
    n = len(arr)
    nah = 0
    for i in range(n):
        swapped = False
        for j in range(n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if i == 0 and not swapped:
            return 1
        if not swapped:
            return 0
    return 0
            
arr = list(map(int, input("数値をスペースで区切って入力: ").split()))
result = bubble_sort(arr)

if result == 0:
    print("ソート後　：", arr)
if result == 1:
    print("既にソートが完了しています")