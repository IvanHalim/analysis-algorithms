import random
import time

def insertsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == '__main__':

    f = open('insertTime.txt', 'w')

    for i in range(0, 10001, 1000):
        print('%d  ' % i),
        f.write('%d ' % i)

        total = 0
        for _ in range(3):
            array = [random.randint(0, 10000) for _ in range(i)]

            start = time.clock()
            insertsort(array)
            t = time.clock() - start
            total += t

            print(', %f ' % t),
            f.write(', %f ' % t)

        average = total / 3
        print(' average %f' % average)
        f.write(', %f \n' % average)

    f.close()