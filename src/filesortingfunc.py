#findindex: function to find the index of the coloumn that match string
def findindex(datalist,keyword):       #datalist will be the first row of the data table, keyword will be the column name
    index = -1
    for i in range(len(datalist)):
        if keyword in datalist[i]:
            index = i
            break          
    return index

#read csv file seperated and extract the column match keyword string containing all certified case
def gencolumn(filename,keyword):
    filename.seek(0)                     #go to beginning of the file
    readtemp = filename.readline()
    columnname = readtemp.split(';')
    statusindex = findindex(columnname,'STATUS')           #find the index for visa status
    keywordindex = findindex(columnname,keyword)           #find the index for keyword
    data_certified = []                                    #this is the list to store all value of keyword column that are certified
    count = 0
    while 1:
        readtemp = filename.readline()

        if (readtemp == ""):
           break

        datatemp = readtemp.split(';')

        if datatemp[statusindex] == 'CERTIFIED':               #only include the certified case
            data_certified.append(datatemp[keywordindex])        
            count+=1
        

    return data_certified


#catdata is a class for storing categorized data, with catdata.n as the name and catdata.c as the count 
class catdata(object):
    def __init__(self,v_name,v_count):
        self.n = v_name           # name of the cateogry       
        self.c = v_count          # count for how many time it appeared
        
    
    

#catogrize data and count the number of time it appears in datalist

def categorize(datalist):
    datalength = len(datalist)
    catlist=[]                              #make list storing [catecory name , number of count and fraction of total, percentage] 
    catlist.append([datalist[0],0,0])
    catlist_tp = zip(*catlist)              # transpose of catlist , catlist_tp[0] is used for a dictionary for selecting name column
    for i in range(len(datalist)):
        catname = datalist[i]
        nameindex = findindex(catlist_tp[0],catname)      #search if the category name already exist, if yes, return index number, else return -1
        if nameindex!=-1:                                 #when category name already exsist, find the index count 
            catlist[nameindex][1]+=1
            catlist[nameindex][2]+=1.0/datalength
        else:                                             #when cateogry is new, create it and count
            catlist.append([catname,1,1.0/datalength])  
            catlist_tp = zip(*catlist)                     #update column dictionary
       
    return catlist



#sorting function using merge algorithom
def merge_sort(datalist):                        #this function is used to divide datalist half-half till the number of unit in a list is twp 
    if len(datalist)<2:
        return(datalist)
        
    else:
        middlerange = len(datalist)//2
        left = merge_sort(datalist[:middlerange])
        right = merge_sort(datalist[middlerange:])
        return merge(left,right)


def merge(left, right):                          #this function is used to merge two sorted list in a sorted way
    result = []
    i=0
    j=0
    while i < len(left) and j < len(right):
       if left[i][1] > right[j][1]:
           result.append(left[i])
           i+=1
       elif(left[i][1] < right[j][1]):
           result.append(right[j])
           j+=1
       else:
           if(left[i][0].strip('"') < right[j][0].strip('"')):
               result.append(left[i])
               i+=1
           else:
               result.append(right[j])
               j+=1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    

# pick the first tpnm of datalist
def picktop(datalist,tpnum):
    if len(datalist) > tpnum:
        datalist_top = datalist[:tpnum]
    else:
        datalist_top = datalist
    
    return datalist_top
                                           