SEARCH_KEY = "AIzaSyBTS4lOa9dDbElpkIGv8DzoPK0q0fl8ax8"
SEARCH_ID = "40e747ae83939462a"
COUNTRY = "us"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *