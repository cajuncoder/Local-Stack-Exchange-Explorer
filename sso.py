#TODO: Search for each word individually
#TODO: Add CLI parameter for csv file to Search
#TODO:     > Different DISPLAY_PROGRAM_CMD defaults for different OS's? (ie, w3m is not available on Windows)
#TODO: Error Checking (50%)
#TODO: Add -h --help
#TODO: Add .config (default browser or textdump -- maybe auto ask on first startup)
#TODO:     > Note: Perhaps config files are overboard and I should just let people modify the source?
#TODO: Add description of how to generate CSV files

import csv
import os
import glob

#Uncomment for raw dump
DISPLAY_PROGRAM_CMD = "cat temp.html"
#Uncomment for html displayed in terminal via w3m
DISPLAY_PROGRAM_CMD = "w3m -dump temp.html | less"
#Uncmment for html displayed in chromium
#DISPLAY_PROGRAM_CMD = "chromium temp.html &"
#filename = 'csv/python-top-1000.csv'
MAX_RESULTS = 24

csvs = glob.glob('*-csv/*.csv')
print 'Please select a csv file to search:'
for i in range(len(csvs)):
    print i, ': ', csvs[i] 
valid_input = False
option = ''
while not valid_input:
    inpt = raw_input()
    if inpt == 'q':
        exit()
    try:
        option = int(inpt)
        valid_input = True
    except ValueError:
        print('Please select a valid number!')
filename = csvs[option]
file = open(filename)
thread = list(csv.reader(file))
file.close()


def search():
    print 'Search title for:'
    query = raw_input()
    if query == 'q':
        exit()
    print 'Searching for '+query
    query_words = query.split(' ')

    #results = []
    nofresults = 0
    for i in range(1, len(thread)):
        if query == "":
            print i, ': ', thread[i][0]
            nofresults = nofresults + 1
            if nofresults > MAX_RESULTS:
                break
        else:
            matches = 0
            for w in range(0, len(query_words)):
                if query_words[w].lower() in thread[i][0].lower():
                    matches = matches + 1
                if matches == len(query_words):
                    #results.add(i)
                    nofresults = nofresults + 1
                    print i, ': ', thread[i][0]

def choose_thread():
    print 'Choose thread to view:'
    valid_input = False
    option = ''
    while not valid_input:
        try:
            inpt = raw_input()
            if inpt == '':
                search()
            if inpt == 'q':
                exit()
            else:
                option = int(inpt)
                valid_input = True
        except ValueError:
            print('Please select a valid number!')

    title = thread[option][0]
    que = thread[option][3]
    ans = thread[option][4]
    outfile = open('temp.html', 'w')
    outfile.write('________________________________________________________________________________<br>[QUESTION]: '+ title + 
            '\n' + que +
            '\n________________________________________________________________________________</br>' +
            '[ACCEPTED ANSWER]:\n' + ans)
    outfile.close()
    os.system(DISPLAY_PROGRAM_CMD)


while True:
    search()
    choose_thread()
