#!/usr/bin/python

import sys, getopt
from os import path
from os.path import basename

# count in both directions for target instances
def count(input_list, target, cur_pos):

    count = 1
    size = len(input_list)

    pos = cur_pos + 1

    while pos < size and input_list[pos] == target:
        count += 1
        pos += 1

    pos = cur_pos - 1

    while pos > -1 and input_list[pos] == target:
        count += 1
        pos -= 1

    return count

def find_and_count(input_list, target, upper, lower):

    # list is sorted we can use bisection to find the target
    while lower < upper:

        cur_pos = ( lower + upper ) // 2
        cur_vale =  input_list[cur_pos]

        if cur_vale == target:
            return count(input_list, target, cur_pos)
        if cur_vale < target:
            lower = cur_pos + 1
        elif cur_vale > target:
            upper = cur_pos            

    return 0

def main(argv):

    #get command line input or return usage
    input = ''
    target = None
    err_output = basename(path.abspath(sys.modules['__main__'].__file__)) \
    + ' -i <input sequence Ex: "5, 7, 7, 8, 8, 10" -t 8>'

    try:
        opts, args = getopt.getopt(argv,"hi:t:v",["help", "ifile="])
    except getopt.GetoptError:
        print(err_output)
        sys.exit(2)

    if len(sys.argv) < 2:
        print(err_output)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(err_output)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input = arg
        elif opt in ("-t", "--target"):
            target = int(arg)

    #if not all populated exit
    if input == '' or target is None:
        print(err_output)
        sys.exit(2)
    
    # read into a list convert to int and sort (validation beyond scope)
    input_list = input.replace(" ", "").split(",")
    input_list_int = list(map(int, input_list))
    input_list_int.sort()
    
    print("\nsorted list: ", input_list_int, " target: ", target)
    count = find_and_count(input_list_int, target, len(input_list), 0)
    print("count: ", count)
    
if __name__ == "__main__":
   main(sys.argv[1:])
