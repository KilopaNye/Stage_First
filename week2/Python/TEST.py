import random
#產生1000000筆隨機亂數
nums = []
for i in range(0, 1000001):
    nums.append(i)
random.shuffle(nums)

#進行Bubble Sort排序
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
        
bubbleSort(nums)
print(nums)