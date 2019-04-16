import random
import time

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

if __name__ == '__main__':

    f = open('mergeTime.txt', 'w')

    for i in range(0, 1001, 100):
        print('%d  ' % i),
        f.write('%d ' % i)

        total = 0
        for _ in range(3):
            array = [random.randint(0, 10000) for _ in range(i)]

            start = time.clock()
            mergesort(array)
            t = time.clock() - start
            total += t

            print(', %f ' % t),
            f.write(', %f ' % t)

        average = total / 3
        print(' average %f' % average)
        f.write(', %f \n' % average)

    f.close()
