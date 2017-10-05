import seaborn as sns
import pandas as pd

df_co = pd.read_csv("C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity_global\\co_lundi_2001.csv")
len_co = len(df_co['Start'])
df_co['Action'] = pd.Series(['Log in' for x in range(len_co)], index=df_co.index)
print(df_co.head())

df_deco = pd.read_csv("C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\agr_activity_global\\deco_lundi_2001.csv")
len_deco = len(df_deco['End'])
df_deco['Action'] = pd.Series(['Log out' for x in range(len_deco)], index=df_deco.index)
df_deco = df_deco.rename(columns = {'End':'Start'})
print(df_deco.head())

df_main = pd.concat([df_co, df_deco])
print(df_main.head())
sns.set_style("whitegrid")
ax = sns.violinplot(x="Batiment", y="Start", data=df_main, hue="Action", split=True )
fig = ax.get_figure()
fig.savefig("C:\\Users\\antonin.barthelemy\\Documents\\ContestCGI\\sept_2017\\data\\plot\\lundi_vio.png")
