#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "Dobrodošli v igri FizzBuzz!"

izbor = int(raw_input("Izberi številko med 1 in 100: "))

for x in range(1, izbor+1):
    if x % 3 == 0 and x % 5 == 0:
        print "Fizzbuzz"
    elif x % 3 == 0:
        print "Fizz"
    elif x % 5 == 0:
        print "Buzz"
    else:
        print x