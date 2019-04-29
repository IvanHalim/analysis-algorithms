def LastToStart(activities):
    activities = sorted(activities, key = lambda x: x[1], reverse = True)
    r = []
    r.append(activities[0][0])
    i = 0
    for m in range(1, len(activities)):
        if activities[m][2] <= activities[i][1]:
            r.insert(0, activities[m][0])
            i = m
    return r

def readfile(file):
    with open(file) as f:
        testcases = []
        for _ in range(2):
            activities = []
            n = int(next(f))
            for _ in range(n):
                a = [int(x) for x in next(f).split()]
                activities.append(a)
            testcases.append(activities)
    return testcases

def solve(testcases):
    output = []
    for test in testcases:
       output.append(LastToStart(test))
    return output

def print_output(output):
    for i in range(len(output)):
        print('Set {0}'.format(i+1))
        print('Number of activities selected = {0}'.format(len(output[i])))
        print('Activities: {0}\n'.format(' '.join(map(str, output[i]))))

if __name__ == '__main__':
    testcases = readfile('act.txt')
    output = solve(testcases)
    print_output(output)
