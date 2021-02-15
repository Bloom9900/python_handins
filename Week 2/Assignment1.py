import csv
import argparse

parser = argparse.ArgumentParser(description='File Manager')

parser.add_argument('path', type=str, help='Path to csv file')
parser.add_argument('-f' , '--file_name', type=str)
args = parser.parse_args()
path = args.path
input_file = args.file_name

my_data_list = ['This', 'is', 'my', 'test', 'data']

# A. def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()

    print(contents)

# B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
def write_list_to_file(output_file, *strings):
    with open(output_file, 'w') as file_object:
        for element in strings:
            file_object.write(str(element) + '\n')

# C. def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    retVal = []
    with open(input_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            retVal.append(str(reader.line_num))

    print(retVal)
