#!/usr/bin/python
import sys
from fractions import Fraction as F

P = int(raw_input().strip())

assert 1 <= P <= 9999
for i in range(P):
    K, f = raw_input().split()
    fr = F(f)
    assert i + 1 == int(K)
    assert str(fr) == f     # gcd(p, q) = 1, fraction already reduced
    assert 0 <= fr.numerator <= 2147483647
    assert 0 <= fr.denominator <= 2147483647

sys.exit(42)
