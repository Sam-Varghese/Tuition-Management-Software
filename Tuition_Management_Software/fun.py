import pandas as pd
df=pd.read_excel("Students_Records.xlsx")
df['Joining Date']=pd.to_datetime(df['Joining Date'])
a=df.groupby(df['Joining Date'].dt.strftime('%B %Y'))
dic={}
for i in a:
    print(i)
    dic[i[0]]=len(i[1].index)
print(dic)