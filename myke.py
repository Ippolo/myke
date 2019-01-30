#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# myke.py
#
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar
#  22 rue de Plaisance, 75014 Paris, France
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#  

from random import Random

def encode(s: str) -> str:
    """
    Permuta una stringa in una maniera che sembra casuale,
    ma in realtà è deterministica
    """
    # ordina i caratteri di s
    char_list = sorted(s)
    # il random seed è lo stesso per qualunque permutazione di s
    random = Random("".join(char_list))
    # genera una permutazione
    perm = list(range(len(s)))
    random.shuffle(perm)
    # applica la permutazione
    for i in range(len(s)):
        char_list[i] = s[perm[i]]
    # ritorna la stringa permutata
    return "".join(char_list)
    
    
def decode(s: str) -> str:
    """
    Applica ad una stringa la permutazione inversa
    della funzione encode
    """
    # ordina i caratteri di s
    char_list = sorted(s)
    # il random seed è lo stesso per qualunque permutazione di s
    random = Random("".join(char_list))
    # genera una permutazione
    perm = list(range(len(s)))
    random.shuffle(perm)
    # applica la permutazione inversa
    for i in range(len(s)):
        char_list[perm[i]] = s[i]
    # ritorna la stringa permutata
    return "".join(char_list)



def main(sys_argv):
    """
    Prova le funzioni encode e decode a scopo di test.
    Se non riceve input dalla shell chiede di inserirlo manualmente
    """
    if len(sys_argv) <= 1:
        # chiedi stringa in input
        arg = input("stringa in input: ")
    else:
        # prendi input della shell
        arg = sys_argv[1]
    # stampa codifica input
    encoded = encode(arg)
    print( "codifica:   %s" %(encoded) )
    # stampa decodifica
    decoded = decode(encoded)
    print( "decodifica: %s" %(decoded) )


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
