from datetime import time
from posixpath import basename
import pandas as pd

from PIL import Image


#function files
from file_handling import * 
from datafram_mannip import *
from mangadx_integration import *
#--------------------------------
from PIL import Image

from pandas.core.frame import DataFrame
from pandas.tseries.offsets import DateOffset
   
file_path = r"C:\Users\Tj\Desktop\Manga database.xlsx" #file path as a strig literal, change this file path for browser

if __name__ == "__main__":

 
    manga_base = initlize_dataframe(file_path)
    manga_max_row = get_max_row_count(manga_base)
  
    print("Welcome to the prototype fortune cookie")
    #testing only, generate a random manga and image from mangadex 
    manga_fortune_cookie = generate_rand_manga(manga_base,manga_max_row)
    #------TESTING CASES-----------------------------------------------
    #manga_fortune_cookie = filtered_search(manga_base,"Action")
    img_url = generate_image_url(manga_fortune_cookie[0])
    #img_url = generate_image_url('Temple')
    #filtered_search(manga_base,'Drama')
    

    
    
    



    

    

    





