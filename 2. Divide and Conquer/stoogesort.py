def stoogesort(arr, l, h): 
    if l >= h: 
        return
   
    # If first element is smaller 
    # than last, swap them 
    if arr[l] > arr[h]: 
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
   
    # If there are more than 2 elements in 
    # the array 
    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3) 
   
        # Recursively sort first 2 / 3 elements 
        stoogesort(arr, l, (h-t)) 
   
        # Recursively sort last 2 / 3 elements 
        stoogesort(arr, l + t, (h)) 
   
        # Recursively sort first 2 / 3 elements 
        # again to confirm 
        stoogesort(arr, l, (h-t)) 


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
        stoogesort(arr, 0, len(arr)-1)
    writefile('stooge.out', array)