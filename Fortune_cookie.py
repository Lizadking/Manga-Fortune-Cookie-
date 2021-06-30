import pandas as pd
import random

from pandas.core.frame import DataFrame

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)





#print(manga_base.loc[(manga_base[cols[5]]== 'Action') | (manga_base[cols[6]] == 'Action') | (manga_base[cols[7]]== 'Action')]) 

def print_dataframe(dataframe):
    return print(dataframe)

def generate_rand_manga(dataframe,max_row_count):
    rand_manga_index = random.randint(0,max_row_count)
    return print(dataframe.iloc[rand_manga_index])

def sorted_genre_cols(dataframe):
    
    found_cols = []
    testing_col = list(dataframe.columns.values)
    #get gnere col locations 
    for i in range(len(testing_col)):
        if "Genre" in testing_col[i]:
            found_cols.append(i)

    #create empty data frame
    temp_dataframe = pd.DataFrame()
    temp_dataframe['Genre'] = ""

    unsorted_genre_list= []

    for found_col_index in found_cols:
        #print(dataframe[testing_col[found_col_index]].values)
        #text=dataframe[testing_col[found_col_index]].values
        #unsorted_genre_list.append(dataframe[testing_col[found_col_index]].values)
        for index,row in dataframe.iterrows():
            #print(row[testing_col[found_col_index]])
            if(row[testing_col[found_col_index]] not in unsorted_genre_list and row[testing_col[found_col_index]] not in unsorted_genre_list != 'nan' ):     
                unsorted_genre_list.append(row[testing_col[found_col_index]])
    
    
    return unsorted_genre_list

def filtered_search(dataframe,genre1,genre2,genre3):
    #include the random pick after implementing filter , and default arguments 
    
    found_cols = []
    testing_col = list(dataframe.columns.values)

    #get gnere col locations 
    for i in range(len(testing_col)):
        if "Genre" in testing_col[i]:
            found_cols.append(testing_col[i])
    #get the title colum 


    #filter 
    #filt =  (dataframe[found_cols[0]] == genre1)
    #print(dataframe.loc[filt,testing_col[1]])
    print(dataframe.loc[filt])

    
        

    """
    return print(dataframe.loc[((dataframe[found_cols[0]] == genre1) | (dataframe[found_cols[1]] == genre1) | (dataframe[found_cols[2]]== genre1)) &
    ((dataframe[found_cols[0]] == genre2) | (dataframe[found_cols[1]] == genre2) | (dataframe[found_cols[2]]== genre2)) &
    ((dataframe[found_cols[0]] == genre3) | (dataframe[found_cols[1]] == genre3) | (dataframe[found_cols[2]]== genre3))])
    """
   
     

        
            
    





if __name__ == "__main__":
    """initlize the dataframe"""
    manga_base = pd.read_excel('Manga database.xlsx')
    cols = list(manga_base.columns.values)
    max_row = manga_base[manga_base.columns[0]].count()-1
    #print(cols)
    #print(sorted_genre_cols(manga_base))
    filtered_search(manga_base,"Action",None,None)
    
    



    

    

    





