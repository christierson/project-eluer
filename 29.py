def main():
    collection = set({})
    for a in range(2, 101):
        for b in range(2, 101):
            collection.add(a**b)
    print(len(collection))
        




if __name__ == '__main__':
    main()