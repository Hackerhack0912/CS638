import csv
import sys



def main():
    # should use utf-8 encoding to prevent errors of decoding in python3
    # I changed the column name in tableA.csv so it matches the names of the output csv
    # then I can directly reorder the columns by their names
    inFile = open('tableC.csv', "r", encoding='utf-8')
    filterFile =  open('result.txt', "r") 
    outFile = open('tableFiltered.csv', "w", encoding='utf-8')
        # new column ordering for output csv
    outputFields = ['_id','ltable_id','rtable_id','ltable_title','ltable_authors','ltable_publisher','ltable_ISBN13','ltable_publishedYear','ltable_publishedMonth','ltable_pages','rtable_title','rtable_authors','rtable_publisher','rtable_ISBN13','rtable_publishedYear','rtable_publishedMonth','rtable_pages']
    writer = csv.DictWriter(outFile, fieldnames=outputFields)
    # save result from random forest to an array
    results = []
    for line in filterFile:
        #get time from file
        line = line.split()
        if line[0] == '1':
            results.append(1)
        else:
            results.append(0)
        
    print(len(results))

    counter = 0
    # write first row which is the header
    writer.writeheader()
    for row in csv.DictReader(inFile):
        lPages = row['ltable_pages']
        rPages = row['rtable_pages']
        lYear = row['ltable_publishedYear']
        rYear = row['rtable_publishedYear']
        lMonth = row['ltable_publishedMonth']
        rMonth = row['rtable_publishedMonth']
        
        if not lPages:
            continue
        if not rPages:
            continue
        if not lYear:
            continue
        if not rYear:
            continue
        if not lMonth:
            continue
        if not rMonth:
            continue
        if results[counter] == 1:
            lISBN = str(row['ltable_ISBN13'])
            rISBN = str(row['rtable_ISBN13'])
            writer.writerow({'_id':row['_id'],'ltable_id':row['ltable_id'],'rtable_id':row['rtable_id'],'ltable_title': row['ltable_title'],'ltable_authors': row['ltable_authors'],'ltable_publisher': row['ltable_publisher'],'ltable_ISBN13': lISBN,'ltable_publishedYear': row['ltable_publishedYear'],'ltable_publishedMonth': row['ltable_publishedMonth'],'ltable_pages': row['ltable_pages'],'rtable_title': row['rtable_title'],'rtable_authors': row['rtable_authors'],'rtable_publisher': row['rtable_publisher'],'rtable_ISBN13': rISBN,'rtable_publishedYear': row['rtable_publishedYear'],'rtable_publishedMonth': row['rtable_publishedMonth'],'rtable_pages': row['rtable_pages']})
        counter += 1

    inFile.close()
    filterFile.close()
    outFile.close()

main()
