#!/usr/bin/python3
import sys
    if __name__ == '__main__':
    args = sys.argv[:1]
    num_args = len(args)
    if num_args == 0:
    print("0 arguments")
    elif num_args == 1:
    print("1 arguments")
    else
     print(num_args, "arguments:")
        for i, arg in enumerate(args):
            print(i+1, ":", arg)
