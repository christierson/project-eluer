def main():
    n = 1
    step = 2
    sum = 1
    while True:
        for i in range(4):
            n += step
            sum += n
            print(n)
        step += 2
        if step > 1000:
            break
    print(sum)





if __name__ == '__main__':
    main()