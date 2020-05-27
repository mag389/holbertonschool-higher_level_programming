#!/usr/bin/python3
""" counting queens """


if __name__ == "__main__":
    from sys import argv
    if len(argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        int(argv[1])
    except Exception as e:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    queens_placed = n
    answer = [[0, 0] for i in range(0, n)]
    print(answer)
