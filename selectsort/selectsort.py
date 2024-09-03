def selectsort(data):
    for i in range(len(data) - 1):
        lowest = i
        for j in range(i+1,len(data)):
            if data[lowest] > data[j]:
                lowest = j
        data[lowest],data[i] = data[i],data[lowest]
    return data

print(selectsort([3,6,8,9,1]))