#!/usr/bin/env python3
# Compute unlimited-length arithmetic roots of numbers

# Last Modified: Sun Apr 17 09:07:24 PDT 2022

# pyroot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# pyroot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nautilus-dropbox.  If not, see <http://www.gnu.org/licenses/>.
#

from numpy.polynomial import polynomial as P
import numpy as np

def extractroot(snum, sroot, fraction_digits=None):
    '''extract any integer root from a number, with arbitrary precision.  The number may be an int
    or a string, and such a string may contain a decimal point.  If fraction_digits is specified
    at all, the number must be a string, and the result will be a string; otherwise, the result
    will be an int.'''
    # Avoid disturbing global variables by mistake
    r = num = root = guess = A = B = rem = None
    if fraction_digits is None:
        pass
    elif isinstance(fraction_digits,int):
        if fraction_digits < 0:
            raise ValueError(f'Fraction digits must be non-negative, but was {fraction_digits}')
    else:
        raise ValueError(f'If present, fraction digits must be an int, but was {type(fraction_digits)}')

    root = int(sroot)
    if str(root) != str(sroot) or root<2:
        raise ValueError("Root should be an integer >= 2 but input was " + snum)

    if isinstance(snum, int):
        iint = int(snum)
        fint = ""

    elif isinstance(snum, str):
        found = snum.find('.')
        if found >= 0:
            if fraction_digits is None:
                raise ValueError(f'Decimal point is not legal with no fraction digts specified: {snum}')
            iint=snum[:found]
            fint=snum[found+1:]
        else:
            iint = snum
            fint = ""

        try:
            foo = int(iint)
            if fint != "":
                foo = int(fint)
        except :
            print(f'iint is {iint}')
            print(f'fint is {fint}')
            raise ValueError(f'Number is not a valid literal: {snum}')
    else:
        raise ValueError("argument must be an int or string, but is",type(snum))

    if fraction_digits is None:
        fint = ""
    else:
        flen = fraction_digits * root
        fint = fint[:flen]
        if len(fint) < flen:
            fint += "0"*(flen - len(fint))
    snum = iint+fint

    # chop the input into chunks
    chunks=()
    while len(snum):
        chunks = (int(snum[-root:]),) + chunks
        snum = snum[0:-root]

    # Prep for the first chunk
    remainder = 0
    A = 0

    while len(chunks) > 0:
        #print()
        B=None
        rem=None
        #print("A is ",A)
        #print("remainder was", remainder)
        remainder = remainder * 10**root + chunks[0]
        #print("Remainder (our target) is", remainder)
        chunks = chunks[1:]
        for guess in 0,1,2,3,4,5,6,7,8,9:
            summands = P.polypow(np.array([guess,10*A],dtype=object),root)[:root]
            subtrahend = sum(summands)
            #print("Summands:",summands)
            #print("Subtrahend:", subtrahend, type(subtrahend))
            if subtrahend <= remainder:
                B = guess
                rem = remainder - subtrahend
            else:
                break
        remainder = rem
        A = A * 10 + B
        #print("A is ",A)

    if fraction_digits is None:
        return A
        
    astr = str(A)
    if fraction_digits == 0:
        return astr
    return astr[:-fraction_digits] + '.' + astr[-fraction_digits:]

if __name__ == '__main__':
    print("Hi there root watchers")
    arg = input("Give me an integer: ")
    root= input("What root am I extracting: ")
    f=input("How many fraction digits: ")
    if f == "":
        f = None
    else:
        f = int(f)


    print("Answer is",extractroot(arg,root,f))


