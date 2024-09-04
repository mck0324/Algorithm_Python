def qsort(data):
    if len(data) <= 1:
        return data
    
    left,right = list(),list()
    pivot = data[0]

    for i in range(1,len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot] + qsort(right)

print(qsort([14,12,1,5,34]))

# 파이덴틱
def qdsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [ item for item in data[1:] if pivot > item ]
    right = [ item for item in data[1:] if pivot <= item ]

    return qdsort(left) + [pivot] + qdsort(right)

print(qdsort([14,12,1,5,34]))