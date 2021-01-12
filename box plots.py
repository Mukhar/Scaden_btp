import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon

organ='breast'
import pandas as pd
df_n=pd.read_csv('Downloads/scaden_predictions_'+organ+'_normal.txt',sep='\t')
df_c=pd.read_csv('Downloads/scaden_predictions_'+organ+'_cancer.txt',sep='\t')
if organ =='liver': 
    df_n['Unknown']=df_n['Unknown']+df_n['Unknown.1']
    df_n.drop('Unknown.1',inplace=True,axis=1)
    df_c['Unknown']=df_c['Unknown']+df_c['Unknown.1']
    df_c.drop('Unknown.1',inplace=True,axis=1)
# f,axes=plt.subplots(1,2)
# axes[0].set_xlabel("Normal",labelpad=20)
# axes[1].set_xlabel("Cancer",labelpad=20)
columns=list(df_n.columns)
x=9
df_plt=pd.DataFrame()
# for x in range(1,len(columns)):
    # df_n[columns[x]].boxplot(rot=80,figsize=(25,12),ax=axes[0],showfliers=False)
    # df_c[columns[x]].boxplot(rot=80,figsize=(25,12),ax=axes[1],showfliers=False)

df_plt['normal']=df_n[columns[x]]
df_plt['cancer']=df_c[columns[x]]

# plt.xlabel(columns[x],labelpad=10)
# plt.ylabel("Cell Fractions",labelpad=10)
# df_plt.boxplot(rot=30)
# plt.savefig('./'+organ+'/'+organ+'_'+columns[x]+'.png')
# plt.clf()

df_long=pd.melt(df_plt,var_name='Cell type',value_name='cell fraction')
# df_long=df_long[::-1]
f=sns.boxplot(x='Cell type',y='cell fraction',data=df_long,palette='pastel',showfliers=False)
f = sns.stripplot(x="Cell type", y="cell fraction", data=df_long, palette='Set1')
# f = sns.scatterplot(x="Cell type", y="cell fraction", data=df_long, palette='Set1')

f.set(xlabel=organ.capitalize()+' '+columns[x])
f1=f.get_figure()
f1.savefig('./'+organ+'/'+organ+'_'+columns[x]+'.png')

stat,p=wilcoxon(df_plt['normal'],df_plt['cancer'])
print(columns[x],p,stat)