def insertsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def readfile(file):
    with open(file) as f:
        array = [[int(x) for x in line.split()] for line in f]
    return array

def writefile(file, array):
    with open(file, 'w') as f:
        f.write('\n'.join([' '.join(map(str, arr)) for arr in array]))
        f.write('\n')

if __name__ == '__main__':
    array = readfile('data.txt')
    for arr in array:
        insertsort(arr)
    writefile('insert.txt', array)