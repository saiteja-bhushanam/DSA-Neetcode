def three_sum(numbers, target):
    numbers.sort()
    for i in range(len(numbers)-2):
        start = i + 1
        end = len(numbers) - 1
        a = []
        while start < end:
            current_sum = numbers[i] + numbers[start] + numbers[end]
            if current_sum == target:
                a.append((numbers[i], numbers[start], numbers[end]))
            elif current_sum < target:
                start += 1
            else:
                end -= 1
    return a

print(three_sum([1,2,3,4,5,6,7,8,9], 15))