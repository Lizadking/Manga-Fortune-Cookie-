import pandas as pd
import random

manga_base = pd.read_excel('Manga database.xlsx')
cols = list(manga_base.columns.values)
max_row = manga_base[manga_base.columns[0]].count()-1

rand_manga_index = random.randint(0,max_row)


print(manga_base.iloc[rand_manga_index])



