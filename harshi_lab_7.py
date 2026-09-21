#  MAX HEAP

# def insert(heap, value):
#     heap.append(value)

#     i = len(heap) - 1

#     while i > 0:
#         parent = (i - 1) // 2

#         if heap[parent] < heap[i]:
#             heap[parent], heap[i] = heap[i], heap[parent]
#             i = parent
#         else:
#             break


# def delete_max(heap):
#     if len(heap) == 0:
#         return None

#     maximum = heap[0]

#     last = heap.pop()

#     if len(heap) > 0:
#         heap[0] = last

#         i = 0

#         while True:
#             left = 2 * i + 1
#             right = 2 * i + 2

#             largest = i

#             if left < len(heap) and heap[left] > heap[largest]:
#                 largest = left

#             if right < len(heap) and heap[right] > heap[largest]:
#                 largest = right

#             if largest != i:
#                 heap[i], heap[largest] = heap[largest], heap[i]
#                 i = largest
#             else:
#                 break

#     return maximum


# # Priority Queue

# heap = []

# insert(heap, 29)
# insert(heap, 11)
# insert(heap, 38)
# insert(heap, 19)

# print("Max Heap:", heap)

# print("Highest Priority:", delete_max(heap))

# print("Priority Queue:", heap)


# # Heap Sort

# arr = [2, 12, 33, 5, 1]

# heap = []

# for x in arr:
#     insert(heap, x)

# sorted_arr = []

# while len(heap) > 0:
#     sorted_arr.append(delete_max(heap))

# sorted_arr.reverse()

# print("Original Array:", arr)
# print("Sorted Array:", sorted_arr)

# Problem 2: Rearrange Array to Maximize Adjacent Sum Difference

def rearrange_array(arr):

    arr.sort()

    result = []

    left = 0
    right = len(arr) - 1

    while left <= right:

        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])

        left += 1
        right -= 1

    return result


def calculate_sum(arr):

    total = 0

    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])

    return total



arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

result = rearrange_array(arr)

total = calculate_sum(result)

print("Original Array:", arr) 
print("Rearranged Array:", result)
print("Sum of Differences:", total)

# Q3:Smallest subarray with sum greater than array 
# Q3: Smallest Subarray with Sum Greater Than Target

def smallest_subarray(arr, target):

    n = len(arr)

    left = 0
    current_sum = 0

    min_length = n + 1

    for right in range(n):

        current_sum += arr[right]

        while current_sum > target:

            window_length = right - left + 1

            min_length = min(min_length, window_length)

            current_sum -= arr[left]
            left += 1

    if min_length == n + 1:
        return -1

    return min_length

arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
target = int(input("Enter target: "))
answer = smallest_subarray(arr, target)

print("Array:", arr)
print("Target:", target)
print("Smallest Subarray Length:", answer)