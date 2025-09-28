nums = [1,2,2,3,3,3] 
k = 2

Output= [2,3]


def k_most(arr,k):
    dict_ = {}
    out_array = []
    for i in arr:
        if str(i) in dict_:
            dict_[str(i)]+=1
        else:
            dict_[str(i)] = 1
    print(dict_)

    for i in dict_:
        if dict_[i] >= k:
            out_array.append(int(i))
    return out_array

print(k_most(nums,k))