import pandas as pd 
dfn=pd.read_excel('C:/Users/mukha/Downloads/liver_sc_name.xlsx',header=None,sep=' ')
index={}
dfn.drop([0,1],axis=0,inplace=True)
dfn.drop([2,3],axis=1,inplace=True)
dfn.rename(columns={0:'A',1:'B'},inplace=True)
index = dict(zip(dfn.A,dfn.B))