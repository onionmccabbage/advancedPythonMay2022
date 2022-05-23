# we will load some JSON from a local file
import json # this is part of Python

def main():
    '''load a local set of JSON data
    then iteratively print the loaded data'''
    fin = open('loading_data/todos.json', 'rt') # 'rt' will read text
    all_j = fin.read() # we now have some JSON
    # we can convert JSON to a Python structure
    all_l = json.loads(all_j) # we now have a list of dict
    print( type(all_j), type(all_l) )
    # we can iteratively work through some of our list
    for i in range(0,11):
        print(all_l[i])


if __name__ == '__main__':
    main()