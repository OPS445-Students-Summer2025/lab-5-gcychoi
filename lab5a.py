#!/usr/bin/env python3

# Name: lab5a.py
# Author: Chung Yin Choi
# Author ID: cychoi
# Date Created: 2025/06/09

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')               # Open file
    read_data = f.read()                    # Read from file
    f.close()                               # Close file
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    read_data = f.read() 
    #new_list = read_data.split('\n')
    new_list = read_data.splitlines()
    #i = 0 
    #while i < len(new_list):
    #    if new_list[i] == "":
    #        new_list.pop(i)
    #    i = i + 1  
    f.close()
    return new_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))



