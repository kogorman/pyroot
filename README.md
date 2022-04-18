# pyroot
Extract arithmetic roots of numbers with arbitrary precision

This is an expansion of the method taught in grade-school for extracting square roots.  The expansion allows for higher-numbered roots, and allows you to specify the number of fraction digits to be developed, with no arbitrary limit.

There is a main program which prompts for function arguments, and a function extractroot(snum, sroot, fraction_digits) which accepts a string or int as the snum, a positive int as root, and an optional non-negative int as the number of fraction digits (defaults to None, meaning no fraction digits produced, and none allowed in the input).

The method develops a perfect power (think square) at each step, each of which power is the largest one no bigger than the value of the digits being considered in that step.  These get larger and larger and closer to the function argument as more digits are considered until the desired accuracy is achieved.  The base of that perfect power is the answer provided by the function.

At each step, the algorithm uses a previous perfect power developed in the previous step (0 for the first step) by using it's base, called A.  It then adds digits to the target, and tries to find a B in ((10\*\*n)*A + B) that when raised to the power required forms the best perfect power for the larger target.  B will simply be one of the 10 possible digits. 

The function returns an int if *fraction_digits* was None, and a string otherwise (even if 0 was specified).

As a program, you are prompted for the number, the root, and the limit on fraction digits (which you can skip to default to None).

Input and output are unconstrained as to length and size, aside from the limits of the computing environment's memory.  If you want the 45th root of 45 with 45 fraction digits, you can have it in a flash.  If you want 20 thousand digits of the square root of 2, you may have to wait a minute (30 seconds on my machine) but you can have it.
