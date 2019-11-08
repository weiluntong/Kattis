#!/usr/bin/env python3

# Had a little too much fun with this one. I knew the order the pieces would come in, and I knew how many of each piece I needed
# So I superfit a polynomial to give me the amount I needed for each piece:
# print(*(round((5 - (137/20)*(key+1) + (25/8)*((key+1)**2) - (1/6)*((key+1)**3) - (1/8)*((key+1)**4) + (1/60)*((key+1)**5))-val) for key, val in enumerate(map(int, input().split()))))

# Here's a more competitive programming way to do it that doesn't take as much time to figure out the fifth degree polynomial
print(*(map(lambda need,have: need-int(have), [1,1,2,2,2,8], input().split())))