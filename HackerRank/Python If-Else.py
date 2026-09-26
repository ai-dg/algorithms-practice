#!/bin/python3


import math
import os
import random
import re
import sys

def n_condition(n : int):
    if n % 2 == 0:
        print("Weird")
    if n % 2 != 0:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    n_condition(n)