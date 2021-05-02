#! /usr/bin/env python3
"""
BSD 3-Clause License

Copyright (c) 2021, M.Harmouch
All rights reserved.
"""
import os
import argparse

def arg_prs():
    parser = argparse.ArgumentParser(prog='distancing',
                                     description='Code distancing script.')
    parser.add_argument('--filename', '-f', dest='filename',
                        default='main.c',
                        type=str,
                        help='The path of the scipt file to be modified.')
    arg_list = vars(parser.parse_args())
    return arg_list

def main():
    arg_lst = arg_prs()
    filename = arg_lst["filename"]
    separated_content = ""
    print("[*] Before Corona: \n")
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            new_line = line.replace('{', "\n\n{")
            separated_content = separated_content + new_line + "\n"
    out_file = filename[:filename.index('.')] + '_out' + filename[filename.index('.'):] 
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(separated_content)
    print(f"\n\n[*] After Corona: \n\n{separated_content}")
    print(f"\n[*] The modified version of your file has been generated as {out_file}!\n")

if __name__ == "__main__":
    main() 