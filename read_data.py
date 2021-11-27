import pandas as pandas
import re 
my_file= open('words.txt')
words = my_file.readlines()

REPLACE_BY_SPACE_RE = re.compile('[\n\"\'/(){}\[\]\|@,;#]')
words = re.sub(REPLACE_BY_SPACE_RE, ' ', words)
words = re.sub(' +', ' ', words)
words = words.lower()