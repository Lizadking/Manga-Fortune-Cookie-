import pandas as pd
import random

from pandas.core.frame import DataFrame
from pandas.tseries.offsets import DateOffset

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#print(manga_base.loc[(manga_base[cols[5]]== 'Action') | (manga_base[cols[6]] == 'Action') | (manga_base[cols[7]]== 'Action')]) 

def print_dataframe(dataframe):
    """
    Function: print_dataframe(dataframe)
    Pre-Condition: A instantiated dataframe 
    Return: A printed Dataframe 
    Misc: 
    """
    
    return print(dataframe)

def generate_rand_manga(dataframe,max_row_count):
    """
    Function: generate_rand_manga(dataframe,max_row_count)
    Pre-Condition: A instantiated dataframe, a maxium row count for database 
    Return: A dataframe randomly selected 
    Misc: 
    """
    
    rand_manga_index = random.randint(0,max_row_count)
    return print(dataframe.iloc[rand_manga_index])

def sorted_genre_cols(dataframe):
    """
    Function: sorted_genre_cols(dataframe)
    Pre-Condition: A instantiated dataframe
    Return: A list of genres 
    Misc: This function generates a list of all the genres in the dataframe 
    """
    
    found_cols = []
    testing_col = list(dataframe.columns.values)

    #get gnere column locations 
    for i in range(len(testing_col)):
        if "Genre" in testing_col[i]:
            found_cols.append(i)

    #create empty data frame
    temp_dataframe = pd.DataFrame()
    temp_dataframe['Genre'] = ""

    unsorted_genre_list= []

    for found_col_index in found_cols:

        for index,row in dataframe.iterrows():
            #filter our genre list and apppend to genre_list 
            if((row[testing_col[found_col_index]] not in unsorted_genre_list) and not (pd.isnull(row[testing_col[found_col_index]]))):     
                unsorted_genre_list.append(row[testing_col[found_col_index]])
    
    
    return unsorted_genre_list

def filtered_search(dataframe,genre1,genre2,genre3):
    """
    MAKE HEADER HERE 
    """
    if((genre1 == None) & (genre2 == None) & (genre3 == None)):
        return print("Cannot do an empty filter search")

    else:

    
        #include the random pick after implementing filter , and default arguments 
        
        found_cols = []
        testing_col = list(dataframe.columns.values)

        #get gnere col locations 
        for i in range(len(testing_col)):
            if "Genre" in testing_col[i]:
                found_cols.append(testing_col[i])
        #get the title colum 


        #filter 
        genre_list = [genre1,genre2,genre3]   
        filt = (dataframe[found_cols[0]].isin(genre_list)) | (dataframe[found_cols[1]].isin(genre_list)) | (dataframe[found_cols[2]].isin(genre_list)) 

        #reset the indexes for database and create new daatframe to make selecton 
        new_manga_base  = dataframe.loc[filt].reset_index(drop = True)
        #generate rand manga 
        max_row = new_manga_base[new_manga_base.columns[0]].count()-1
        return generate_rand_manga(new_manga_base,max_row)
    
def main_menu(userinput,dataframe):
    valid_menu = [1,2,3]
    print("Main Menu: \n1) Random Pick\n2)Filtered Random Pick \n3)Exit")
    userinput = input("Enter Menu option ")
    user_valid = True
    
            
        
        

   
   
   

if __name__ == "__main__":
    #initlize the dataframe
    manga_base = pd.read_excel('Manga database.xlsx') #make this a function soon 
    cols = list(manga_base.columns.values)
    max_row = manga_base[manga_base.columns[0]].count()-1
    user_input = 0
    print("Welcome to the prototype fortune cookie")



    #main_menu(0,manga_base)

    

    
  
    #filtered_search(manga_base,"Comedy","Action",None)
    #print(sorted_genre_cols(manga_base))
    #print(generate_rand_manga(manga_base,max_row))
    
    



    

    

    





