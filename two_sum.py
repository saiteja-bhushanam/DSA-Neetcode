arr = [3,4,5,6,4]
target = 7

# def two_sum(arr):
#     arr.sort()
#     start = 0
#     end = len(arr) - 1
#     position_list = []
#     while start < end :
#         if arr[start]+arr[end] == target:
#             position_list.append([start,end])
#         elif arr[start]+arr[end] < target:
#             start+=1
#         else:
#             end-=1
#     return position_list

# print(two_sum(arr))

def two_sum_hashmap(arr):
    hash_map = {}
    for i in range(len(arr)):
        if target - arr[i] in hash_map:
            return [i,has]
        else:
            hash_map[i]=0
    return False

print(two_sum_hashmap(arr))