#!/usr/bin/env python3

import sys
import random


def get_art(path, spec=None):
    with open(path, "r") as f:
        # return read_lines(f.readlines())
        all = f.read()
        spl = all.split("BREAK\n")
        if spec is None:
            targ = random.choice(spl).split("\n")
        else:
            targ = spl[spec].split("\n")
        # print((targ))
        out = []
        for line in targ:
            out.append(line)
        return read_lines(out)


def read_lines(source):
    lines = []
    max = 0
    for line in source:
        line = line.strip("\n")
        lines.append(line)
        # n = len(line.strip(".,-_"))
        n = len(line.strip())
        if n > max:
            max = n
    return lines, max


def read_all():
    return sys.stdin.read()


def pretty_out(art, inp, art_max, inp_max):
    diff = abs(art_max - inp_max)
    winner = max(art_max, inp_max)
    inp_pad = 0
    art_pad = 0
    if art_max > inp_max:
        inp_pad = diff // 2
    elif art_max < inp_max:
        art_pad = diff // 2

    j = 0
    m = len(art)
    for i in art:
        print(" " * art_pad, end="")
        print(i)
    print("-" * winner)
    for i in inp:
        print(" " * inp_pad, end="")
        if len(i) < inp_max:
            diff = abs(len(i) - inp_max)
            print(" " * (diff // 2), end="")
        print(i)


def main():
    in_lines, in_max = read_lines(sys.stdin)
    art_lines, art_max = get_art("art")
    pretty_out(art_lines, in_lines, art_max, in_max)


if __name__ == "__main__":
    main()
