import os
import csv
import numpy as np
#reference for kmeans usage: http://codereview.stackexchange.com/questions/52029/k-means-clustering-in-python
POSTALCODE_USERCATEGORY_CSV_FILEPREFIX = 'yelp_usercategorymatrix_'
CSV_FILESUFFIX = '.csv'
#
# collect list of all postal code csv files with userCategory tables
#
def getPostalCodeUserCategoryCSVs():
    result = {}
    for file in os.listdir('.'):
        if file.startswith(POSTALCODE_USERCATEGORY_CSV_FILEPREFIX) and file.endswith(CSV_FILESUFFIX):
            postalCode = file[len(POSTALCODE_USERCATEGORY_CSV_FILEPREFIX):(-1*len(CSV_FILESUFFIX))]
            result[postalCode] = './{0}'.format(file)
    return result
#
# load csvFilename
# into np array as a matrix
#
def loadMatrix(csvFilename):
    rowData = None
    with open(csvFilename, 'r') as csvf:
        rowData = list(csv.reader(csvf))
    csvf.closed
    matrixRowCount = len(rowData) - 1
    matrixColumnCount = len(rowData[0]) - 1

    result = np.zeros((matrixRowCount, matrixColumnCount), dtype='i4')
    matrixRowIndex = 0
    rowCount = 0
    userIdRowIndex = {}
    for row in rowData:
        rowCount += 1
        if 1 == rowCount:
            continue
        userIdRowIndex[row[0]] = matrixRowIndex
        matrixColIndex = 0
        colCount = 0
        for col in row:
            colCount += 1
            if 1 == colCount:
                continue
            result[matrixRowIndex][matrixColIndex] = int(col)
            matrixColIndex += 1
        matrixRowIndex += 1
    return result

postalCodeUserCategoryCSVMap = getPostalCodeUserCategoryCSVs()

samplePostalCode = '89109'
sampleFile = postalCodeUserCategoryCSVMap[samplePostalCode]

sampleMatrix = loadMatrix(sampleFile)

print(sampleMatrix)
