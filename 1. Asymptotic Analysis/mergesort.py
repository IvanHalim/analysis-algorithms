def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
        mergesort(arr)
    writefile('merge.txt', array)