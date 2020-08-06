import sys
import numpy as np

#Sample code for creating sorted suffix array
#RNAFile1 = [1,'Array1',[-2,0,-343,-2,0,0]]
#RNAFile2 = [2,'Array2',[0,0,343,0,0,-3,999]]
#RNAFile3 = [3,'Array3',[1,0,-43,0,0,0,99,-2,0,0]]
#RNAFile4 = [4,'Array4',[1,0,-43,0,0,0,0,0]]

#Original RNA Sequence Array
rnaArrays = [[1,'RNAFile1',[-2,0,-343,-2,0,0]], [2,'RNAFile2',[0,0,343,0,0,-3,999]], 
             [3,'RNAFile3',[1,0,-43,0,0,0,99,-2,0,0]], [4,'RNAFile4',[1,0,-43,0,0,0,0,0]]]

print(f"Original Arrays: {rnaArrays}")
len_rnaArrays = len(rnaArrays)
print(f"\nOriginal array length: {len_rnaArrays}")

print("\nSuffix of each rnafile data in rnaArray: \n")
for i in range(len_rnaArrays):
    len_data = len(rnaArrays[i][2])
    for k in range(len_data):
        print(f"{k}  {rnaArrays[i][2][k:]}")
    print("\n")

RNA_NmpyArray = np.array(rnaArrays)
print(RNA_NmpyArray.size)
print(RNA_NmpyArray.itemsize)
print("RNA_NumpyArray Size = %d bytes" % (RNA_NmpyArray.size * RNA_NmpyArray.itemsize))

# Creating Unsorted suffix array from Original rnaArrays
USSArrays = []
MaxIndx = 0
for i in range(len_rnaArrays):
    datalen = len(rnaArrays[i][2])
    if MaxIndx < datalen :
        MaxIndx = datalen
    for j in range(datalen):
        USSArrays.append([i,j]) 

print(f"\nUnsorted Suffix Array: {USSArrays}")
len_USSArrays = len(USSArrays)
print(f"Unsorted Suffix Array length: {len_USSArrays}")

#Initial sorting on basis of substring position value
USSArrays.sort(key = lambda row: (row[1]), reverse = True) 

print(f"\nUnsorted Suffix Array after first sorting on substring position value: {USSArrays}")
len_USSArrays = len(USSArrays)
print(f"Unsorted Suffix Array length: {len_USSArrays}")


# Creating final sorted suffix array from Unsorted suffix array
SSArrays = []
init = 0
for k in reversed(range(MaxIndx)):
    temp = []
    for l in range(init,len_USSArrays):
        if k == USSArrays[l][1]:
            temp.append([USSArrays[l][0],USSArrays[l][1],rnaArrays[USSArrays[l][0]][2][k:]])
        else :
            init = l
            break
    temp.sort(key = lambda row: (row[2]))
    print(f"\nfor {k} index sorted suffix array will be:")
    print(temp)
    
    len_temp = len(temp)
    for n in range(len_temp):
        SSArrays.append([temp[n][0], temp[n][1]])
    del temp

print(f"\nFinal Sorted Suffix Array: {SSArrays}")
len_SSArrays = len(SSArrays)
print(f"Sorted Suffix Array length: {len_SSArrays}")
print("\nSize of Sorted Suffix Array:")
SS_NmpyArray = np.array(SSArrays)
print(SS_NmpyArray.size)
print(SS_NmpyArray.itemsize)
print("RNA_NumpyArray Size = %d bytes" % (SS_NmpyArray.size * SS_NmpyArray.itemsize))
