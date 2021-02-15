import os
import argparse

parser = argparse.ArgumentParser(description='File Manager 2.0')

def get_file_names(folderpath, out='output.txt'):
    dirs = os.listdir(folderpath)
    with open(out, 'w') as file_object:
        for element in dirs:
            file_object.write(str(element) + '\n')

def get_all_file_names(folderpath, out='output.txt'):
    with open(out, 'w') as file_object:
        for root, dirs, files in os.walk(folderpath):
            for item in files:
                file_object.write(str(item) + '\n')
                
def print_line_one(file_names):
    for file in file_names:
        with open(file) as file_object:
            print(file_object.readline())

def print_emails(file_names):
    for file in file_names:
        with open(file) as file_object:
            for line in file_object:
                if '@' in line:
                    print(line)

def write_headlines(md_files, out='output.txt'):
    for file in md_files:
        with open(file) as file_object:
            with open(out, 'w') as output_file:
                for line in file_object:
                    if line[0] == '#':
                        output_file.write(str(line) + '\n')