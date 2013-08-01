#! /usr/bin/env python3

import sys

def main(args):
    return len(args) - 1

if __name__ == '__main__':
    print(main(sys.argv))
