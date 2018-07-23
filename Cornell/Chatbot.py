import pandas as pd
import re
file = open('Cornell Dataset/cornell movie-dialogs corpus/movie_lines.txt').readlines()

example = file[145]
print(example)

line_id = re.findall('L\d{1,10}',example)
print(line_id)

char_id  = re.findall('u\d',example)
print(char_id)

movie_id = re.findall('m\d',example)
print(movie_id)

char_name = re.findall('[A-Z][A-Z][A-Z]*',example)
print(char_name)

char_lines = re.findall('[A-Z][^\d].{1,len(char_name)+1}',example)
print(char_lines)