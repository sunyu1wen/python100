def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    for fruit in fruits:
        print(fruit.title())
    print()

    fruits2 = fruits[1:4]
    print(fruits2)

    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # poor out in lawrange
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()