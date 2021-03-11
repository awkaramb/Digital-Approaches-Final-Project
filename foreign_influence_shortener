import sys
import os
import re

#Shorten all instances of "foreign influence" into one token.

for file in os.scandir('/Users/amazinganthony/digital_approaches/newspapers_foreigninfluence'):
    with open(file.path, 'r+', encoding='utf-8', errors='ignore') as input_file:
        text = input_file.read()
        if 'foreign influence' in str(text).lower():
            input_file.seek(0)
            text = re.sub(r'foreign influence', 'foreigninfluence', text, re.IGNORECASE)
            input_file.write(text)
            input_file.truncate()
            continue
        elif 'foreign influence' not in str(text).lower():
            os.remove(file.path)
    
print('Finished shortening all instances of "foreign influence" in files.')
