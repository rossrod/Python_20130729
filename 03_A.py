#! /usr/bin/env python3.3

def FV(principal, rate, term):
    '''
    Calculates the future value given the principle, rate, term.
    '''
    return principal * (1 + rate) ** term

def main(value):
    for year in range(1, 11):
        print(
            '{:3d} {:7.2f} {:7.2f} {:7.2f}'.format(
                year,
                FV(value, 0.03, year),
                FV(value, 0.05, year),
                FV(value, 0.07, year),
            )
        )

if __name__ == '__main__':
    main(100)
