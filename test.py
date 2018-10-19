import pandas as pd
import os


tables = pd.io.html.read_html("https://www.click-sec.com/corp/guide/commission_list/")



print(tables[0])

