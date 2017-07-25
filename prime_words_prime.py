# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:08:12 2017

@author: swamy
"""
import sympy
from num2words import num2words

numbers = [int(i) for i in input("Input:\n").split()]

primes = [int(i) for i in sympy.primerange(numbers[0],numbers[1])]
prime_word_prime = 0
for i in primes:
    if sympy.isprime(len(num2words(i))):
        prime_word_prime += 1
print(prime_word_prime)

