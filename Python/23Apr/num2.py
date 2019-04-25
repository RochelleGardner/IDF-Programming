#! /usr/bin/env python3

def main():
    i = 1
    sq = 0
    for i in range(1, 11):
        sq = i * i
        print(sq, " ", end = '')
        i = i + 1
main()