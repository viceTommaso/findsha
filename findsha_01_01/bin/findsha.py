# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "01.01"

import sys
import hashlib


boold = False


def allsha(t_word, t_sha):
    """
    select a SHA to process it and process it
    :param t_word:
    :param t_sha:
    :return: sha
    """
    if len(t_sha) == 40:
        sha1 = hashlib.sha1(t_word.encode()).hexdigest()
        if boold:
            print(sha1)
        return sha1
    if len(t_sha) == 56:
        sha224 = hashlib.sha224(t_word.encode()).hexdigest()
        if boold:
            print(sha224)
        return sha224
    if len(t_sha) == 64:
        sha256 = hashlib.sha256(t_word.encode()).hexdigest()
        if boold:
            print(sha256)
        return sha256
    if len(t_sha) == 96:
        sha384 = hashlib.sha384(t_word.encode()).hexdigest()
        if boold:
            print(sha384)
        return sha384
    if len(t_sha) == 128:
        sha512 = hashlib.sha512(t_word.encode()).hexdigest()
        if boold:
            print(sha512)
        return sha512


def password(t_letters, t_sha):
    """
    creates a word (max 8 letters) and ends when it finds the corresponding SHA
    :return: 0
    """
    for a in t_letters:
        for b in t_letters:
            for c in t_letters:
                for d in t_letters:
                    for e in t_letters:
                        for f in t_letters:
                            for g in t_letters:
                                for h in t_letters:
                                    trypas = a + b + c + d + e + f + g + h
                                    if boold:
                                        print(trypas)
                                    findsha = allsha(trypas, t_sha)
                                    if t_sha == findsha:
                                        print("password:  " + trypas)
                                        return 0


def main():
    """
    main
    :return: none
    """
    letters = ["", "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J",
               "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u",
               "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               ".", " "]

    try:
        if len(sys.argv) < 2:
            sha = input("sha:  ")
        else:
            sha = sys.argv[-1]

        print("processing...")
        password(letters, sha)

    except IndentationError:
        if boold:
            print("error")


if __name__ == "__main__":
    if boold:
        print("Start")

    main()

    if boold:
        print("Stop")
