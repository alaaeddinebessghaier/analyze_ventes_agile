import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns
### data vente 2016/2015

""" data_vente_2015 = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\vente2015_2016new.xlsx',sheet_name ='2015' )
vente_2015_ac = data_vente_2015.dropna()
vente_2015_ac.to_csv('vente_2015.csv',index=False)  """
""" print(data_vente_2015.head())
print(data_vente_2015.info())
print(data_vente_2015.isnull().sum())  """
""" vente_2016_ac = data_vente_2016.dropna()
 """"""print(data_vente_2015.isnull().sum()) 
print(vente_2015_ac['LIBGVR'].nunique()) 
print(vente_2015_ac['CATPRD'].nunique())  
print(vente_2015_ac.describe())
plt.hist(vente_2016_ac['MOIS']) 
vente_2015_ac['LIBGVR'] = vente_2015_ac['LIBGVR'].str[:2]
plt.bar(vente_2015_ac['MOIS'],vente_2015_ac['SUM(MNTHT)'])
plt.show()  """
""" vente_2016_ac.to_csv('vente_2016.csv',index=False)
 """### data_station

""" data_stations = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\Stations.xlsx', sheet_name ='categorie')
 """"""print(data_stations.info())
print(data_stations.describe())
print(data_stations.isnull().sum()) """
""" data_stations.to_csv('data_stations_categorie.csv',index=False)
 """
### client_listestation
""" data_station = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\codification_clients.xlsx', header=1,sheet_name ='LISTESTATION')
 """"""print(data_station.info())
print(data_station.describe())
print(data_station.isnull().sum())"""
""" data_station_ac = data_station.drop('Unnamed: 4',axis=1)
 """"""print(data_station_ac.info())
print(data_station_ac['GOUVERNORAT'].nunique())
data_station_ac_gov = data_station_ac['GOUVERNORAT'].str[:2]
counts = data_station_ac_gov.value_counts()
plt.bar(counts.index,counts.values)
plt.show()""" 
""" data_station_ac.to_csv('data_station.csv',index=False)
 """
 ### client_listeclients
""" data_client_cod = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\codification_clients.xlsx',sheet_name ='LISTECLIENTS')
 """"""print(data_client_cod.info())
print(data_client_cod.describe())
print(data_client_cod.isnull().sum())"""
""" data_client_cod = data_client_cod.drop(['Unnamed: 0','GOUVERNORAT'],axis=1)
 """"""print(data_client_cod.info())
print(data_client_cod['AME'].nunique())
data_client_cod_sc = data_client_cod['Secteurs clients'].str[:2]
counts = data_client_cod_sc.value_counts()
plt.bar(counts.index,counts.values)
plt.show()    """
""" data_client_cod.to_csv('data_client.csv',index=False)
 """

### SGAZ
""" data_client_gaz = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\codification_clients.xlsx',sheet_name ='LISTECLIENTSGAZ')"""
data_client_gaz = pd.read_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\vente_2015.csv')
""" data_client_gaz.drop('Ancien Compte ',axis=1)"""
""" data_client_gaz = data_client_gaz.iloc[:, 1:]
data_client_gaz.to_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\data_client_gaz.csv', index=False, encoding='utf-8')   """
print(data_client_gaz['LIBGVR'].isnull().sum())
print(data_client_gaz.columns)
""" print(data_client_gaz.info())
 """"""print(data_client_gaz.describe())
print(data_client_gaz.isnull().sum())
print(data_client_gaz['Client '].nunique())
data_client_gaz_sc = data_client_gaz['Gouvernorat'].str[:5]
counts = data_client_gaz_sc.value_counts()
plt.bar(counts.index,counts.values)
plt.show()  """
""" data_client_gaz.to_csv('data_client_gaz.csv',index=False)
 """
### JET 
""" data_client_jet = pd.read_excel('C:\\Users\\bessghaier\\projet_bi\\bi\\data\\codification_clients.xlsx',sheet_name ='LISTECLIENTSJET')
 """"""print(data_client_jet.info())
print(data_client_jet.describe())
print(data_client_jet.isnull().sum())
print(data_client_jet['Type Clients'].nunique())
data_client_jet_sc = data_client_jet['Consolidation Client'].str[:5]
counts = data_client_jet_sc.value_counts()
plt.bar(counts.index,counts.values)
plt.show() """
""" data_client_jet.to_csv('data_client_jet.csv',index=False)
 """



""" vente_2015 = pd.read_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\vente_2015.csv', encoding='utf-8')
 """""" vente_2015 = vente_2015.iloc[:, 1:]  # Remove first 2 columns
vente_2015['année'] = 2015 """
""" vente_2015.insert(0, 'id_fact', range(1, len(vente_2015) + 1))
vente_2015 = vente_2015.dropna()
# Save without index column
vente_2015.to_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\vente_2015.csv', index=False, encoding='utf-8')  """ 

""" vente_2016 = pd.read_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\vente_2016.csv', encoding='utf-8')
 """""" vente_2016 = vente_2016.iloc[:, 2:]  # Remove first 2 columns
vente_2016['année'] = 2016 """
""" vente_2016.insert(0, 'id_fact', range(1, len(vente_2016) + 1))
vente_2016 = vente_2016.dropna() """

# Save without index column
""" vente_2016.to_csv('C:\\Users\\bessghaier\\projet_bi\\bi\\vente_2016.csv', index=False, encoding='utf-8') 
 """


df = pd.read_excel('C:\\talend\\TOS_DI-Win32-20200219_1130-V7.3.1\\workspace\\product.xls')
print(df.nunique())