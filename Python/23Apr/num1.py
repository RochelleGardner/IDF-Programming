#! /usr/bin/env python3

def main():
    i = 1
    a = 2
    b = 0
    for i in range(1,5):
        b = a * i
        print(a, ' times ', i, ' = ', b)
        i = i + 1
main()