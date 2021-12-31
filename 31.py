coins = [200, 100, 50, 20, 10, 5, 2, 1]

def main():
    backtrack([0]*8)

def backtrack(a, res):
    sum = get_sum(a)
    if sum > 200:
        return []
    elif sum == 200:
        return [a]
    else:
        for i, coin in enumerate coins:



def next(a, i):
    

def backuptrack(n, c, d):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        for i in get_possible(n):
            c += backtrack(n-i, c, d+1)
        
        print(d)
        return c

def get_sum(a):
    return sum([x*y for (x, y) in zip(a, coins)])



def get_possible(n):
    return list(filter(lambda c : c <= n, coins))
    #return list(filter(lambda c : c <= n, [1, 2, 5, 10, 20, 50, 100, 200]))



if __name__ == "__main__":
    main()
