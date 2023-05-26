import math
from random import randrange

"""This function factorizes n given in param
"""
def get_factor(n, limit=1000):
    for a in range(n):
        a = randrange(n)
        print(f'\nSearching for a = {a}')
        for k in range(2, limit, 2):
            if pow(a, k, n) == 1:
                if a % 2 == 0:
                    q = pow(a, k//2, n)
                    p = math.gcd(q-1, n)
                    if p > 1:
                        q = pow(a, k//2, n)
                        p = math.gcd(q+1, n)
                        if p > 1:
                            print(f"\nFound: ({a}, {k})\n")
                            return (a, k), (p, n//p)
    print("\nOops!!!!! the number can't be factorized\n\n")
    return (-1, -1), (0, 0)

def main():
    n = int(input("Enter the value of n: "))
    a_k, p_q = get_factor(n) 
    print('\n\n\nR E S U L T\n\n')
    if a_k == (-1, -1):
        print("\tOops!!!!! the number can't be factorized\n\n")
    else:
        print(f"\tP: {p_q[0]}, Q: {p_q[1]}\n\n")

if __name__ == '__main__':
    main()