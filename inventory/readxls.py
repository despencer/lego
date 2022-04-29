#!/usr/bin/python3

import pandas as pd

lego = pd.read_excel('/mnt/mobihome/lego/lego.xls', sheet_name=1)
lego = lego[lego.Item.notnull()]
print(lego.columns)
print(lego.head(5))
print(lego.tail(5))