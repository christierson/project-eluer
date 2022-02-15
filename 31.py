coins = [200, 100, 50, 20, 10, 5, 2, 1]
coins.reverse()
coins_inv = [200/coin for coin in coins]

    
def get_sum(a):
    return sum([x*y for (x, y) in zip(a, coins)])


def backtrack(a, i, val):    
    sum = get_sum(a)
    if sum > 200:
        return backtrack(a[:i-1] + [a[i] + 1, 0] + a[i+1:], i-1, val)
    elif sum == 200:
        return backtrack(a[:i-1] + [a[i] + 1, 0] + a[i+1:], i-1, val + 1)
    else:
        c = a[i]
        if c < coins_inv[i]:
            backtrack(a[:i] + [a[i] + 1] + a[i+1:], i, val)
        elif c == coins_inv[i]:
            return val
        
        
        
               
        if below_max(a, i):
            backtrack(a, i+1, val)
        else:
            c = a[i]
            a[:i] + [a[i] + 1] + a[i+1:]
            if c < coins_inv[i]:
                backtrack(a[:i] + [a[i] + 1] + a[i+1:], i+1, val)
            elif c == coins_inv[i]:
                pass
    return res
    
def next(a, i):
    n = coins_inv[i]
    if a[i == n]:
        return a[:i+1] + [a[i+1] + 1] + a[-i:]
    else:
        return a[:i] + [a[i] + 1] + a[i+1:]



def main():
    print(backtrack([0]*8, 0))


if __name__ == "__main__":
    main()




def get_possible(n):
    return list(filter(lambda c : c <= n, coins))
    #return list(filter(lambda c : c <= n, [1, 2, 5, 10, 20, 50, 100, 200]))

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

