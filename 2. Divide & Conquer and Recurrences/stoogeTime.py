import random
import time

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


if __name__ == '__main__':

    f = open('stoogeTime.txt', 'w')

    for i in range(0, 1001, 100):
        print('%d  ' % i),
        f.write('%d ' % i)

        total = 0
        for _ in range(3):
            array = [random.randint(0, 10000) for _ in range(i)]

            start = time.clock()
            stoogesort(array, 0, len(array)-1)
            t = time.clock() - start
            total += t

            print(', %f ' % t),
            f.write(', %f ' % t)

        average = total / 3
        print(' average %f' % average)
        f.write(', %f \n' % average)

    f.close()