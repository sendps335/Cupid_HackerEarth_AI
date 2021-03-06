import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

eng_st_words=stopwords.words('english')
df_data=pd.read_csv(r'C:\Users\DEBIPRASAD\Desktop\Projetc Work\Cupid_Role_AI\dataset\data.csv')
col=df_data.columns
#for i in col:
#    print(i)
#    print(df_data[i].describe())
curious=['pets']
useless=['username','bio']
df_data.drop(useless,axis=1,inplace=True)

""" Age """
print(np.mean(df_data.age))
print(np.median(df_data.age))
sns.displot(df_data.age,color='pink')
plt.title('Age EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Status """
print(df_data.status.value_counts()/df_data.shape[0]*100)
df_data.status.value_counts().plot(kind='bar')
plt.title('Status EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Sex of User """
print(df_data.sex.value_counts()/df_data.shape[0]*100)
df_data.sex.value_counts().plot(kind='bar')
plt.title('Sex EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Sexual Orientation """
print(df_data.orientation.value_counts()/df_data.shape[0]*100)
df_data.orientation.value_counts().plot(kind='bar')
plt.title('Sexual Orientation EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Drinks """
print(df_data.drinks.value_counts()/df_data.shape[0]*100)
df_data.drinks.value_counts().plot(kind='bar')
plt.title('Drinks EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Drugs """
print(df_data.drugs.value_counts()/df_data.shape[0]*100)
df_data.drugs.value_counts().plot(kind='bar')
plt.title('Drugs EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Height """
print(np.median(df_data.height))
print(np.mean(df_data.height))
sns.displot(df_data.height)
plt.title('Height EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Job """
print(df_data.job.value_counts()/df_data.shape[0]*100)
df_data.job.value_counts().plot(kind='bar')
plt.title('Job EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Pet """
print(df_data.pets.value_counts()/df_data.shape[0]*100)
df_data.pets.value_counts().plot(kind='bar')
plt.title('Pet EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Body Profile """
print(df_data.body_profile.value_counts()/df_data.shape[0]*100)
df_data.body_profile.value_counts().plot(kind='bar')
plt.title('Body EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Education """
print(df_data.education_level.value_counts()/df_data.shape[0]*100)
df_data.education_level.value_counts().plot(kind='bar')
plt.title('Education Level EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Location Preferences """
print(df_data.location_preference.value_counts()/df_data.shape[0]*100)
df_data.location_preference.value_counts().plot(kind='bar')
plt.title('Location Preferences EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

""" Interests """
print(df_data.interests.value_counts()/df_data.shape[0]*100)
df_data.interests.value_counts().plot(kind='bar')
plt.title('Interests EDA')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()