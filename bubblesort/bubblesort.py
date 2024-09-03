# # data_list = [9,1,7,5]

def bubblesort(data):
    for i in range(len(data)-1):
        swap = True
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                swap= True
        if swap == False:
            break
    return data
print(bubblesort([9,1,7,5]))