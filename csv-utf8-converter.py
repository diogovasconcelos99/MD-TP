import chardet

# Detect the current encoding
with open('datasets/restaurants-with-menus.csv', 'rb') as f:
    result = chardet.detect(f.read(100000))
    current_encoding = result['encoding']

# Read and write the file line by line
with open('datasets/restaurants-with-menus.csv', 'r', encoding=current_encoding, errors='replace') as infile, \
     open('datasets/restaurants-with-menus-utf8.csv', 'w', encoding='utf-8') as outfile:
    for line in infile:
        outfile.write(line)
