# StackSearchOffline (sso)
# Created by Luke Samuel Dupont, 01/29/2018
# Contributors:

# Purpose:
# View StackExchange / StackOverflow questions and answers offline without having
# to download the entire stackoverflow dump files! This is meant to be a simple
# csv searcher / viewer for csv files created for specific StackOverflow / 
# StackExchange tags: ie, 'top 1000 python questions sorted by view count',
# and search them offline. This takes very little hard disk space, is quicker than
# searching online, and doesn't require internet access.

# Notes:
# This is meant to be an extremely simple, portable CLI program.
# This program is open-source. Contributions are welcome!

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

csvs = glob.glob('csv/*.csv')
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
    for i in range(0, len(thread)):
        matches = 0
        for w in range(0, len(query_words)):
            if query_words[w].lower() in thread[i][0].lower():
                matches = matches + 1
            if matches == len(query_words):
                #results.add(i)
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
