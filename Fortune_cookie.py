from datetime import time
import pandas as pd
import random

import requests  
import json
from PIL import Image

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
    Return: A list containing [titel,current chapter]
    Misc: 
    """
    #get the colums in the dataframe
    testing_col = list(dataframe.columns.values)
    
   
    col_locs = []
    #find the title colulm
    title_col_loc= ''
    valid_title_col_names = ['title','Title','TITLE','Name','NAME','name']
    for i in range(len(testing_col)):
        if(testing_col[i] in valid_title_col_names):
            col_locs.append(i)

    
    
    #find the current chapter or chapter coulum 
    chapter_col_loc = ''
    valid_title_col_names = ['chap','number','chapter','Currentchapter']
    for i in range(len(testing_col)):
        if(testing_col[i] in valid_title_col_names):
            col_locs.append(i)
    #generate random manga

    rand_manga_index = random.randint(0,max_row_count)
    #print(dataframe.iloc[rand_manga_index].values)
    #save title and chapter in a list and return it

    #there's a glitch where unicode \xa0 appears and it needs to be removed 
    manga_info = [dataframe.iloc[rand_manga_index,col_locs[0]],dataframe.iloc[rand_manga_index,col_locs[1]]]
    #remove \xa0 
    if manga_info[0].find('\xa0') != -1:
        manga_info[0] = manga_info[0].replace(u'\xa0', u' ')


    return manga_info

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

def generate_image_url(title):
    """
    MAKE HEADER HERE 
    return: a valid managdex image url 
    """
    #Step 1 - send title to mangadex and await response-------
    print(title)
    print("Checking for valid title...")
    payload ={'title': title}
    response = requests.get('https://api.mangadex.org/manga',params=payload,timeout=10)
    
    if(not response.ok):
        print("Error: cannot obtain valid manga ")
        return None #this should return the bidoof url/image

    response_json= response.json() #convert response into a json

    """
    400 check here 
    """
    #step 2 base manga ID check---------
    print("checking for manga ID...")
    base_id = response_json['results'][0]['data']['id'] #exception is thrown here, IndexError: list index out of range, see what manga causes it and 
                                                        #and handle the exception, this could be a manga not in mangadex
    
    id_payload = {}
    id_payload['manga[]'] = [base_id]
    id_payload['limit'] = 100
    cover = requests.get('https://api.mangadex.org/cover',params=id_payload,timeout=10)
    print(cover.status_code)
    #in case 400 code for cover 
    if(not cover.ok):
        print("Error: cannot obtain valid manga ID ")
        return None #this should return the bidoof url/image

    json_cover = cover.json()

    

    #step 3 generate mangadex url---------
    print("Checking for valid url...")
    volume = ""
    file_name = ""
    for item in json_cover['results']:
        print(item['data']['attributes']['volume'],item['data']['attributes']['fileName'])

        if(item['data']['attributes']['volume'] == '1'):
            volume = item['data']['attributes']['volume']
            file_name = item['data']['attributes']['fileName']

        elif(item['data']['attributes']['volume'] == None):#get the default cover if there is none
            file_name = item['data']['attributes']['fileName']

    

    base_cover_url = 'https://uploads.mangadex.org/covers/'
    base_cover_url+= base_id + '/'+file_name

    url_ping = requests.get(base_cover_url)
        
        #failsafe for 400 url_ping
    if(not url_ping.ok):
        print("Error: cannot obtain valid manga  url")
        return None #this should return the bidoof url/image

    return base_cover_url
    

    
            
        
        

   
   
   

if __name__ == "__main__":
    #initlize the dataframe
    manga_base = pd.read_excel('Manga database.xlsx') #make this a function soon 
    cols = list(manga_base.columns.values)
    max_row = manga_base[manga_base.columns[0]].count()-1
    #remove column white space
    manga_base.columns = manga_base.columns.str.replace(' ', '')
    

    user_input = 0
    print("Welcome to the prototype fortune cookie")
    #testing only, generate a random manga and image from mangadex 
    manga_fortune_cookie = generate_rand_manga(manga_base,max_row)
    print(generate_image_url(manga_fortune_cookie[0]))



    #main_menu(0,manga_base)

    

    
  
    #filtered_search(manga_base,"Comedy","Action",None)
    #print(sorted_genre_cols(manga_base))
    #print(generate_rand_manga(manga_base,max_row))
    
    



    

    

    





