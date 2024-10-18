example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    for i in range(len(data)):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
              
    return data


print(bubble_sort(example_array))
             









