
from datetime import datetime
import re
import csv
import sys

def main():
    
    
    formatBarnes()
    formatGoodReads()


def formatDate(s):
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)

def formatBarnes():
    # should use utf-8 encoding to prevent errors of decoding in python3
    # I changed the column name in tableA.csv so it matches the names of the output csv
    # then I can directly reorder the columns by their names
    with open('tableA.csv', "r", encoding='utf-8') as inFile, open('formattedTableA.csv', "w", encoding='utf-8') as outFile:
        # new column ordering for output csv
        fieldnames = ['id', 'title', 'authors','ISBN13','pages','publisher','publishedYear','publishedMonth','publishedDay']
        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
        # write first row which is the header
        writer.writeheader()
        for row in csv.DictReader(inFile):
            writer.writerow(row)

    inFile.close()
    outFile.close()


def formatGoodReads():
    
    with open('tableB.csv', "r", encoding='utf-8') as inFile, open('formattedTableB.csv', "w", encoding='utf-8') as outFile:
        fieldnames = ['id', 'title', 'authors','ISBN13','pages','publisher','publishedYear','publishedMonth','publishedDay']
        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
        # write first row which is the header
        writer.writeheader()
    
        for row in csv.DictReader(inFile):
            #process date
            date = row['date']
            spaces = date.count(' ')
            length = len(date)
            if(spaces >= 2):
                # case when year, month, day are presented
                # cases like 'October 1st 1993'
                date = datetime.strptime(formatDate(date), '%B %d %Y')
                year = date.year
                month = date.month
                day = date.day
            elif(spaces == 1):
                # cases like 'January 1990'
                date = datetime.strptime(date, '%B %Y')
                year = date.year
                month = date.month
                day = ''
            elif (length == 4):
                # cases like '2009'
                # case when we only have 4 digits year
                date = datetime.strptime(date, '%Y')
                year = date.year
                month = ''
                day = ''
            else:
                # empty case
                # error case when no date is presented
                year = ''
                month = ''
                day = ''
            
            writer.writerow({'id': row['id'], 'title': row['title'], 'authors': row['authors'], 'ISBN13': row['ISBN13'], 'pages': row['pages'], 'publisher': row['publisher'], 'publishedYear': year, 'publishedMonth': month, 'publishedDay': day})

    inFile.close()
    outFile.close()

main()
