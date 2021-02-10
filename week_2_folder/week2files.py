import csv

# A. def print_file_content(file) that can print content of a csv file to the console

def print_file_content(file):
    with open(file, 'r') as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            print(row)
        
print_file_content('myfile.csv')

# B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file

import csv
def write_list_to_file(output_file, *lst):
    with open(output_file, 'a') as file_obj:
        for item in lst:
            file_obj.write(item)
               
        
write_list_to_file('myfile.csv', "nyt", "nyt", "nyt")

# C.def read_csv(input_file) that take a csv file and read each row into a list
import csv
myList = [];
def read_csv(input_file):
    with open(input_file, 'r') as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            myList.append(line.rstrip())


read_csv('myfile.csv')
print(myList)

#Add a functionality so that the file can be called from cli with 2 arguments
# an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.

import csv
import sys
import argparse
def write_list_to_file_cli(output_file, *lst):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
    parser.add_argument('--file')
    parser.add_argument('--lst', required=True)
    args = parser.parse_args()
    if args.output:
        print('Det her er hjælpe teksten')
    if args.file:
        with open(args.file, 'a') as file_obj:
            lst = args.lst
            for item in lst:
                file_obj.write(item)
    else: 
        print(lst)            
        
if __name__ == '__main__':
    write_list_to_file_cli(*sys.argv[1:])        






