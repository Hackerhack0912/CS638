import csv
import sys



def main():
    # should use utf-8 encoding to prevent errors of decoding in python3
    # I changed the column name in tableA.csv so it matches the names of the output csv
    # then I can directly reorder the columns by their names
    inFileA = open('formattedTableA.csv', "r", encoding='utf-8')
    inFileB = open('formattedTableB.csv', "r", encoding='utf-8')
    filterFile =  open('tableFiltered.csv', "r", encoding='utf-8')
    outFile = open('tableE.csv', "w", encoding='utf-8')
        # new column ordering for output csv
    outputFields = ['id','title','authors','ISBN13','pages','publisher','publishedYear','publishedMonth','publishedDay']
    writer = csv.DictWriter(outFile, fieldnames=outputFields)
    # save result from random forest to an array
    rowCounter = 0
    # write first row which is the header
    writer.writeheader()
    for row in csv.DictReader(inFileA):
        aISBN = str(row['ISBN13'])
        writer.writerow({'id':str(rowCounter),'title':row['title'],'authors': row['authors'],'ISBN13': aISBN, 'pages': row['pages'],'publisher': row['publisher'],'publishedYear': row['publishedYear'],'publishedMonth': row['publishedMonth'],'publishedDay': row['publishedDay'] })
        rowCounter += 1

    setE = set()
    for row in csv.DictReader(filterFile):
        setE.add(str(row['rtable_id']))
    

    for row in csv.DictReader(inFileB):
        if str(row['id']) not in setE:
            bISBN = str(row['ISBN13'])
            writer.writerow({'id':str(rowCounter),'title':row['title'],'authors': row['authors'],'ISBN13': bISBN, 'pages': row['pages'],'publisher': row['publisher'],'publishedYear': row['publishedYear'],'publishedMonth': row['publishedMonth'],'publishedDay': row['publishedDay'] })
            rowCounter += 1

    inFileA.close()
    inFileB.close()
    filterFile.close()
    outFile.close()

main()
