
from datetime import time
from posixpath import basename
import pandas as pd

from PIL import Image


import urllib.request
from PIL import Image

from pandas.core.frame import DataFrame
from pandas.tseries.offsets import DateOffset

def initlize_dataframe(file_name):
    """
    MAKE HEADER HERE 
    return: List [mangadataframe,rowcount]
    """
    #try to load in a valid xlsx file 
    try:
        pd.read_excel(file_name)
    #fail, exception thrown 
    
    except FileNotFoundError:
        print("Error: File could not be found")
        return None
    #Success 
    else:
        #initlize the dataframe
        manga_base = pd.read_excel(file_name)
        
        cols = list(manga_base.columns.values)
        max_row = manga_base[manga_base.columns[0]].count()-1
        #remove column white space
        manga_base.columns = manga_base.columns.str.replace(' ', '')
        print("File load in success!")

        return manga_base