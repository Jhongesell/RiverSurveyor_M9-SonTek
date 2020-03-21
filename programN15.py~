import pandas as pd
 
def main():
    
    # List of lists
    students = [ ['jack', 34, 'Sydeny'] ,
                 ['Riti', 30, 'Delhi' ] ,
                 ['Aadi', 16, 'New York'] ]
    
    print("****Create a Dataframe from list of lists *****")
    
    # Creating a dataframe object from listoftuples
    dfObj = pd.DataFrame(students)
    
    print("Dataframe : " , dfObj, sep='\n')
    
    # List of Tuples
    students = [ ('jack', 34, 'Sydeny') ,
                 ('Riti', 30, 'Delhi' ) ,
                 ('Aadi', 16, 'New York') ]
    
    print("****Create a Dataframe from list of tuple *****")
    
    # Creating a dataframe object from listoftuples
    dfObj = pd.DataFrame(students)
    
    print("Dataframe : " , dfObj, sep='\n')
    
    
    print("****Create a Dataframe from list of tuple, also set column names and indexes *****")
    
    #Convert list of tuples to dataframe and set column names and indexes
    dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])
    
    print("Dataframe : " , dfObj, sep='\n')
    
    print("****Create dataframe from list of tuples and skip certain columns*********")
    
    # Create datafrae from student list but skip column 'Age' i.e. only with 2 columns
    dfObj = pd.DataFrame.from_records(students, exclude=['Age'], columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])
    
    print("Dataframe : " , dfObj, sep='\n')
    
    print("***Create dataframe from multiple lists***")
    
    listOfNames =  ['jack', 'Riti', 'Aadi']
    listOfAge   =  [34, 30, 16]
    listOfCity  =  ['Sydney', 'Delhi', 'New york']
    
    # Create a zipped list of tuples from above lists
    zippedList =  list(zip(listOfNames, listOfAge, listOfCity))
    
    print("zippedList = " , zippedList)
    
    # Create a dataframe from zipped list
    dfObj = pd.DataFrame(zippedList, columns = ['Name' , 'Age', 'City'], index=['a', 'b', 'c'])
 
    print("Dataframe : " , dfObj, sep='\n')
    
if __name__ == '__main__':
    main()
