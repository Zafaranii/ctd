from functools import partial
import re
import pandas as pd
print("Enter the names u want to add to list, press'q' if u want to quit")
lst = []
lst1 = []
lst.extend(i for i in iter(partial(input,'Enter friend for user 1 : '), 'q'))
lst1.extend(i for i in iter(partial(input,'Enter friend for user 2 : '), 'q'))
lst2 = [''.join(x for x in i if x.isalpha()) for i in lst]
lst3 = [''.join(x for x in i if x.isalpha()) for i in lst1]
lst=list(pd.Series(lst2).str.lower())
lst1=list(pd.Series(lst3).str.lower())
print("Mutual Friends :", (set(lst)).intersection(set(lst1)))