def main():
    n = 2
    sum = 0
    while len(str(n))*(9**5) > n:
        ps = get_power_sum(n)
        if n == ps:
            sum += n
            print(f"{n} - {sum}")
        n += 1


def get_power_sum(n):
    sum = 0
    for k in str(n):
        #print(k)
        sum += int(k)**5
    return sum
        

if __name__ == '__main__':
    main()