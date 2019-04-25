#! /usr/bin/env python3

import random 

def main():
  lottery = []
  for i in range(7):
    x = random.randint(0,9)
    lottery.append(x)

  for j in (lottery):
    print(j, end="")
  print()
main()