import json
import urllib.request
import math
import os
import re
import sys

chronam = 'https://chroniclingamerica.loc.gov'
# Enter Chronicling Ameirca search results url
results = 'https://chroniclingamerica.loc.gov/search/pages/results/?date1=1920&rows=200&searchType=basic&state=&date2=1930&proxtext=communist&y=0&x=0&dateFilterType=yearRange&page=5&sort=relevance'
#waiting to input
path_to_files = sys.argv[1]

# Count to keep track of number of files downloaded
count = 0

# Creates JSON file of search results
results_json = results + '&format=json'
#print(results_json)

def get_json(url):
    #data = urllib.urlopen(url).read()
    data = urllib.request.urlopen(results_json).read()
    output = json.loads(data)
    return output

output = get_json(results_json)

# Cycle through JSON results
for page in output['items']:

    # Create URL
    hit = str(page['id'].encode('utf-8'))
    seed = hit[2:-2] + '/ocr/'
    download_url = chronam + seed

    # Create File Name
    file_name = download_url.replace('/', '_')
    file_name = file_name[40:]

    # Download and save PDF 
   
    if urllib.request.urlretrieve(download_url, str(file_name)):
        shell_command = f"cp {file_name} {sys.argv[1]}"
        os.system(shell_command)
        os.remove(file_name)
    
    print('file saved: ' + file_name)
    count += 1
    
# Prints number of PDFs downloaded
print (str(count) + ' results downloaded')

#Remove duplicate files.

for file in os.scandir(path_to_files):
    if os.path.exists(file) > 1:
        os.remove(file)

