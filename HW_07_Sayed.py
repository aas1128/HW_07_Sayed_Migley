import os
import csv 
import numpy as np

def readValidationData():
    folder_path = os.path.dirname(os.path.realpath(__file__)) + '/Test_Data/'
    allAttributes = []
    attributeData = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file != "Validation_Data_for_Students.csv":
                filepath = os.path.join(root, file)
                if "csv" in filepath:
                    with open(filepath, mode='r') as csvFile:
                        reader = csv.DictReader(csvFile, delimiter=',')
                        for row in reader:
                            for object in row:
                                if object not in allAttributes:
                                    allAttributes.append(object)
                                    attributeData[object] = []
                            for attribute in allAttributes:
                                temp = attributeData.get(attribute)
                                if row[attribute] is not None:
                                    temp.append(row[attribute])
                                    attributeData[attribute] = temp
    print("here", allAttributes)
    return allAttributes, attributeData

def computeCovMatrix(allAttributes, attributeData):
    newAttrData = []
    for attr in allAttributes:
        if attr != "ID":
            newAttrData.append(attributeData.get(attr))
    newNumAttrData = []
    for i in newAttrData:
        tempRow = []
        for j in i:
            tempRow.append(float(j))
        newNumAttrData.append(tempRow)
    matrix = np.array(newNumAttrData)  # called X
    print("this is the matrix")
    print(matrix)
    # Mean-center and normalize each column (attribute)
    # Old cross correlation was computing for each data point rather than each attribute
    # Corrected cross correlation matrix
    covariance_matrix = np.cov(matrix)
    
    row, cols = covariance_matrix.shape
    print("covariance matrix has ", row, " rows")
    print("covariance matrix has ", cols, " cols\n")

    return (covariance_matrix)
def main():
    #(A)
    allAttributes, attributeData = readValidationData() #Read in the file data

    #(B)
    cov_matrix = computeCovMatrix(allAttributes,attributeData) # Compute Covariance Matrix
    print("This is the covariance matrix")
    for row in cov_matrix:
        np.set_printoptions(precision=2, suppress=True, linewidth=200)
        print(row)
    
    print("\n\n\n")

    #(C)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    print("these are the eigenVectors")
    print(eigenvectors)
    cov_matrix = abs(cov_matrix)
    max = 0
    for row in eigenvectors:
        for element in row:
            if element > max:
                max = element
    print(max )


main()