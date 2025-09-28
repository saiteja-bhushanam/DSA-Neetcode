arr =  [1,2,4,6]


def productExceptSelf(arr):
    out_array = []
    for i in range(len(arr)):
        prod_ = 1
        for j in range(len(arr)):
            if i != j:
                prod_*=arr[j]
        out_array.append(prod_)
            
    return out_array

print(productExceptSelf(arr))