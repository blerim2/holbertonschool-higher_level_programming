#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    max_length = len(sys.argv) - 1
    arg_sum = 0
    for i in range(1, max_length + 1):
        arg_sum += int(sys.argv[i])
    print(arg_sum)
