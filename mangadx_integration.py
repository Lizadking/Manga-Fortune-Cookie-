from datetime import time
from posixpath import basename
import pandas as pd
import webbrowser
from PIL import Image
import urllib.request
from PIL import Image

from pandas.core.frame import DataFrame
from pandas.tseries.offsets import DateOffset

#this file will contain mangadex integration such as user auth

def go_to_page(manga_id):
    """
    Function: 
    Pre-Condition: 
    Post-Conditon: Take user to randomly generated manga's page 
    Return: 
    Misc: 
    """
    base_url = 'https://mangadex.org/title/'
    base_url+=manga_id

    try:
        webbrowser.open(base_url)  # Go to example.com
    except webbrowser.Error as ex:
        print("Something went wrong with opening the url ")