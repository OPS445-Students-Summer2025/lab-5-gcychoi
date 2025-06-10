#!/usr/bin/env python3

# Name: lab5b.py
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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    read_list = read_file_list(file_name_read)

    f = open(file_name_write, 'w')
    line_no = 1    
    for line in read_list:
        f.write(str(line_no) + ':' + line +'\n')
        line_no = line_no + 1
    f.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))




