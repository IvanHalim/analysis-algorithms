import time
import random

def FirstFit(W, C):
    # Initialize count of bins
    n_bins = 0

    # Create an array to store remaining space in bins
    bin_rem = [C for _ in range(len(W))]

    # Place items one by one
    for i in range(len(W)):

        # Find the first bin that can accomodate W[i]
        for j in range(len(bin_rem)):
            if bin_rem[j] >= W[i]:
                bin_rem[j] -= W[i]

                # If bin index is greater than count of bins
                if j+1 > n_bins:
                    n_bins = j+1
                break
    return n_bins

def FirstFitDecreasing(W, C):
    # Sort weights in decreasing order
    Weights = sorted(W, reverse=True)
    
    # Initialize count of bins
    n_bins = 0

    # Create an array to store remaining space in bins
    bin_rem = [C for _ in range(len(Weights))]

    # Place items one by one
    for i in range(len(Weights)):

        # Find the first bin that can accomodate W[i]
        for j in range(len(bin_rem)):
            if bin_rem[j] >= Weights[i]:
                bin_rem[j] -= Weights[i]

                # If bin index is greater than count of bins
                if j+1 > n_bins:
                    n_bins = j+1
                break
    return n_bins

def BestFit(W, C):
    # Initialize count of bins
    n_bins = 0

    # Create an array to store remaining space in bins
    bin_rem = [C for _ in range(len(W))]

    # Place items one by one
    for i in range(len(W)):

        # Initialize minimum space left and index
        # of best bin
        min = C+1
        best_bin = 0

        # Find the best bin that can accomodate W[i]
        for j in range(n_bins):
            if bin_rem[j] >= W[i] and bin_rem[j] - W[i] < min:
                best_bin = j
                min = bin_rem[j] - W[i]

        # If no bin could accomodate W[i],
        # create a new bin
        if min == C+1:
            bin_rem[n_bins] -= W[i]
            n_bins += 1

        # Otherwise assign item to best bin
        else:
            bin_rem[best_bin] -= W[i]

    return n_bins

def readfile(filename):
    with open(filename) as f:
        n = int(next(f))
        testcases = []
        for _ in range(n):
            C = int(next(f))
            next(f)
            W = [int(x) for x in next(f).split()]
            testcases.append((W, C))
    return testcases

def solve(testcases):
    output = []
    for test in testcases:
        # First Fit
        start = time.clock()
        ff = FirstFit(test[0], test[1])
        ff_time = time.clock() - start

        # First Fit Decreasing
        start = time.clock()
        ffd = FirstFitDecreasing(test[0], test[1])
        ffd_time = time.clock() - start

        # Best Fit
        start = time.clock()
        bf = BestFit(test[0], test[1])
        bf_time = time.clock() - start

        output.append([(ff, ff_time), (ffd, ffd_time), (bf, bf_time)])
    return output

def print_output(output):
    for i in range(len(output)):
        print('Test Case {0} First Fit: {1}, {2}. First Fit Decreasing: {3}, {4}. Best Fit: {5}, {6}.'
              .format(i+1, output[i][0][0], output[i][0][1], output[i][1][0], output[i][1][1], output[i][2][0], output[i][2][1]))

def randomBinPack(n):
    testcases = []
    for i in range(n):
        length = (i+1) * 100
        C = random.randint(100, 200)
        W = [random.randint(1, C) for _ in range(length)]
        testcases.append((W, C))
    return testcases

def solveTime(testcases, filename, algorithm):
    with open(filename, 'w') as f:
        for test in testcases:
            times = []
            for _ in range(3):
                start = time.clock()
                result = algorithm(test[0], test[1])
                t = time.clock() - start
                times.append(t)
            average = sum(times) / 3.
            length = len(test[0])
            f.write(
                '{0},{1},{2},{3},{4},{5}\n'.format(
                    length,
                    result,
                    times[0],
                    times[1],
                    times[2],
                    average
                )
            )

if __name__ == '__main__':
    testcases = readfile('input/bin.txt')
    output = solve(testcases)
    print_output(output)
    testcases = randomBinPack(20)
    solveTime(testcases, 'times/ffTime.txt', FirstFit)
    solveTime(testcases, 'times/ffdTime.txt', FirstFitDecreasing)
    solveTime(testcases, 'times/bfTime.txt', BestFit)
