import pandas as pd
import numpy as np

all_data = pd.read_csv('data.csv')
print(all_data.info())
print(all_data.head(100))

# 1.关于条件筛选（仅仅筛选user_id = 1439408 和 date　为空的） “&” 表示并且，　“｜”表示或者

# # 直接筛选方法
# some = all_data[(all_data['User_id'] == 1439408) & (all_data['Date'].isna())]
# print(some)

# # 使用map方法的boolean方法
# user_requried = all_data['User_id'].map(lambda x : x==1439408)
# date_requried = all_data['Date'].map(lambda x : np.isnan(x))
# some = all_data[user_requried & date_requried]
# print(some)

# 使用query方法
some = all_data.query('(User_id == 1439408)')
print(some)