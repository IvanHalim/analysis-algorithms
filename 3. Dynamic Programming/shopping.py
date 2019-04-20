def Knapsack(price, weights, cap):
    n = len(price)
    r = [[0 for _ in range(cap + 1)] for _ in range(n + 1)] 
  
    # Build table r[][] in bottom up manner 
    for i in range(n + 1): 
        for j in range(cap + 1):
            if i == 0 or j == 0: 
                r[i][j] = 0
            elif weights[i - 1] <= j: 
                r[i][j] = max(price[i - 1] + r[i - 1][j - weights[i - 1]],  r[i - 1][j]) 
            else: 
                r[i][j] = r[i - 1][j] 

    # Stores the result of Knapsack
    res = r[n][cap]

    items = [] # list to store the items
    w = cap
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
            
        # Either the result comes from the top (K[i-1][w]) or
        # from (val[i-1] + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter one, it means the
        # item is included.
        if res == r[i - 1][w]:
            continue
        else:
            items.insert(0, i)
            res -= price[i - 1] 
            w -= weights[i - 1]
    
    return items, r[n][cap]

def readfile(file):
    with open(file) as f:
        T = int(next(f))
        testcases = []
        for i in range(T):
            N = int(next(f))
            price = []
            weights = []
            for _ in range(N):
                p, w = [int(x) for x in next(f).split()]
                price.append(p)
                weights.append(w)
            F = int(next(f))
            family = []
            for _ in range(F):
                family.append(int(next(f)))
            testcases.append([price, weights, family])
    return testcases

def solve(testcases):
    output = []
    for t in testcases:
        sum = 0
        family = []
        for cap in t[2]:
            items, res = Knapsack(t[0], t[1], cap)
            sum += res
            family.append(items)
        output.append([sum, family])
    return output

def writefile(file, output):
    with open(file, 'w') as f:
        for i in range(len(output)):
            f.write('Test Case %s\n' % str(i+1))
            f.write('Total Price %s\n' % str(output[i][0]))
            f.write('Member Items:\n')
            for j in range(len(output[i][1])):
                f.write('%s: ' % str(j+1))
                f.write(' '.join(map(str, output[i][1][j])))
                f.write('\n')
            f.write('\n')

if __name__ == '__main__':
    testcases = readfile('shopping.txt')
    output = solve(testcases)
    writefile('results.txt', output)
