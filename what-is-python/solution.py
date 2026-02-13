"""
Problem: What is Python?
URL: https://neetcode.io/problems/python-what-is-python/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from decimal import Decimal, getcontextfrom decimal import Decimal, getcontext
""""""
The Chudnovsky formula is a "Ramanujan-type" series.1 To understand how it works,The Chudnovsky formula is a "Ramanujan-type" series.1 To understand how it works,
we have to look at it as a machine that balances three different moving parts: we have to look at it as a machine that balances three different moving parts: 
a fixed constant, a linearly growing part, and a massively shrinking part.a fixed constant, a linearly growing part, and a massively shrinking part.
The formal identity is:$$\frac{426880\sqrt{10005}}{\pi} = \sum_{k=0}^{\infty} \frac{(6k)! (545140134k + 13591409)}{(3k)! (k!)^3 (-640320)^{3k}}$$1.The formal identity is:$$\frac{426880\sqrt{10005}}{\pi} = \sum_{k=0}^{\infty} \frac{(6k)! (545140134k + 13591409)}{(3k)! (k!)^3 (-640320)^{3k}}$$1.
The "Constant" (The Scale)The number 426880 $\sqrt{10005}$ (which is C in your code)The "Constant" (The Scale)The number 426880 $\sqrt{10005}$ (which is C in your code)
acts as a scaling factor. acts as a scaling factor. 
The Chudnovsky brothers derived this using complex multiplication of elliptic curves. The Chudnovsky brothers derived this using complex multiplication of elliptic curves. 