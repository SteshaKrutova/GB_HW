import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})
df2=pd.DataFrame(columns=['human','robot'])
for i in range(df.shape[0]):
  if df.at[i,'whoAmI']=='robot':
    df2.at[i,'robot']='True'
    df2.at[i,'human']='False'
  else:
    df2.at[i,'robot']='False'
    df2.at[i,'human']='True'
df2.head()
print(df2)