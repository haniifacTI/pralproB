""" Arin diberikan tugas oleh gurunya untuk membuat program pembalik array menggunakan rekursif, dikarenakan
dia kesusahan saat mengerjakan tugasnya, bantulah Arin untuk membuat program tersebut. """

# array = [1,2,3,4,5] => [5,4,3,2,1]

def reverseArray(arr,arrLen,temp=[]):
    #Base Case
    if arrLen == -1:
        return temp
    #Rekursif
    else:
        temp.append(arr[arrLen])
        return reverseArray(arr,arrLen-1,temp)

arr = [7,11,22,31,100] #[100,31,22,11,7]
print(reverseArray(arr,len(arr)-1))