def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(7))


if __name__ == "__main__":
    main()
