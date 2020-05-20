#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
#print(os.listdir("../input"))


# In[2]:


data = pd.read_csv('data.csv')
data.head(5)


# In[3]:


len(data)


# In[4]:


data.describe()


# In[5]:


data.describe(include=[object])


# In[6]:


data.info()


# # Предобработка датасета

# In[2]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[8]:


data.query('budget == budget.max()')


# In[3]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[10]:


data.query('runtime == runtime.max()')


# In[4]:


answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[12]:


data.query('runtime == runtime.min()')


# In[5]:


answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[14]:


data.runtime.mean()


# In[6]:


answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[16]:


data.runtime.median()


# In[7]:


answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[18]:


data['margin'] = data['revenue'] - data['budget']
data.query('margin == margin.max()')


# In[8]:


answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[20]:


data[data.margin == data.margin.min()]


# In[9]:


answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[22]:


len(data[data.margin > 0])


# In[10]:


answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[24]:


data_9 = data[data.release_year == 2008]
data_9.query('margin == margin.max()')


# In[11]:


answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[26]:


data_10 = data[(data.release_year >= 2012) & (data.release_year <= 2014)]
data_10.query('margin == margin.min()')


# In[12]:


answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[28]:


pd.DataFrame(data.genres.str.split('|').tolist()).stack().value_counts()


# In[13]:


answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[30]:


data_12 = data[data.margin > 0]
pd.DataFrame(data_12.genres.str.split('|').tolist()).stack().value_counts()


# In[14]:


answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[32]:


pd.DataFrame(data.director.str.split('|').tolist()).stack().value_counts()


# In[15]:


answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[34]:


data_14 = data[data.margin > 0]
pd.DataFrame(data_14.director.str.split('|').tolist()).stack().value_counts()


# In[16]:


answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[36]:


dir_df = pd.DataFrame(data.director.str.split('|').tolist()).stack().reset_index()
dir_df.columns = ['data_index', 'qty_index', 'director']

dir_df['margin'] = dir_df.data_index.apply(lambda x:data.iloc[x]['margin'])
dir_df.groupby(['director'])['margin'].sum().sort_values(ascending=False)


# In[17]:


answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[38]:


act_df = pd.DataFrame(data.cast.str.split('|').tolist()).stack().reset_index()
act_df.columns = ['data_index', 'qty_index', 'actor']

act_df['margin'] = act_df.data_index.apply(lambda x:data.iloc[x]['margin'])
act_df.groupby(['actor'])['margin'].sum().sort_values(ascending=False)


# In[18]:


answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[40]:


act_df['release_year'] = act_df.data_index.apply(lambda x:data.iloc[x]['release_year'])
sorted_act = act_df[act_df.release_year == 2012]
sorted_act.groupby(['actor'])['margin'].sum().sort_values()


# In[19]:


answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[42]:


act_df['budget'] = act_df.data_index.apply(lambda x:data.iloc[x]['budget'])
high_budget = act_df[act_df.budget > data.budget.mean()]
high_budget.actor.value_counts()


# In[20]:


answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[44]:


act_df['genres'] = act_df.data_index.apply(lambda x:data.iloc[x]['genres'])
NicCage = act_df[act_df.actor == 'Nicolas Cage']
genres_df = pd.DataFrame(NicCage.genres.str.split('|').tolist()).stack().value_counts()
display(genres_df)


# In[21]:


answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[46]:


pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().value_counts()


# In[22]:


answer_ls.append(1)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[48]:


studio_df = pd.DataFrame(data.production_companies.str.split('|').tolist()).stack().reset_index()
studio_df.columns = ['data_index', 'qty_index', 'studio']

studio_df['release_year'] = studio_df.data_index.apply(lambda x:data.iloc[x]['release_year'])

sorted_studio = studio_df[studio_df.release_year == 2015]
sorted_studio.studio.value_counts()


# In[23]:


answer_ls.append(4)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[50]:


studio_df['genres'] = studio_df.data_index.apply(lambda x:data.iloc[x]['genres'])


qty_of_std = pd.DataFrame(studio_df.data_index.value_counts())
studio_df['revenue'] = studio_df.data_index.apply(lambda x:data.iloc[x]['revenue'])

sort_stud = studio_df[studio_df.genres.str.contains("Comedy", na=False)]
sort_stud.groupby(['studio'])['revenue'].sum().sort_values(ascending=False)


# In[24]:


answer_ls.append(2)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[52]:


year = studio_df[studio_df.release_year == 2012]
year.groupby(['studio'])['revenue'].sum().sort_values(ascending=False)


# In[25]:


answer_ls.append(3)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[54]:


studio_df['original_title'] = studio_df.data_index.apply(lambda x:data.iloc[x]['original_title'])
studio_df['margin'] = studio_df.data_index.apply(lambda x:data.iloc[x]['margin'])
ParSt = studio_df[studio_df.studio == 'Paramount Pictures']
ParSt.query('margin == margin.min()')


# In[26]:


answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[56]:


data.groupby(['release_year'])['margin'].sum().sort_values(ascending=False)


# In[27]:


answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[58]:


WarBros = data[data.production_companies.str.contains("Warner Bros")]
WarBros.groupby(['release_year'])['margin'].sum().sort_values(ascending=False)


# In[28]:


answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[60]:


data['month'] = data.release_date.apply(lambda x:str(x).split('/')[0])
data.month.value_counts()


# In[29]:


answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[62]:


len(data.query('month == "6" | month == "7" | month == "8"'))


# In[30]:


answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[64]:


winter = data[(data.month == '12') | (data.month == '1') | (data.month == '2')]
pd.DataFrame(winter.director.str.split('|').tolist()).stack().value_counts()


# In[31]:


answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[66]:


pivot = data.pivot_table(values=['margin'], index=['month'], columns=['release_year'], aggfunc='sum')
display(pivot.idxmax().value_counts())


# In[32]:


answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[68]:


studio_df['len_name'] = studio_df.original_title.apply(lambda s:len(s))
studio_df.groupby(['studio'])['len_name'].mean().sort_values(ascending=False)


# In[33]:


answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[70]:


studio_df['words_qty'] = studio_df.original_title.apply(lambda s:len(str(s).split()))
studio_df.groupby(['studio'])['words_qty'].mean().sort_values(ascending=False)


# In[34]:


answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[72]:


names = data.original_title.str.lower()

mutual_list=[]
for name in names:
    mutual_list += str(name).split()

count = collections.Counter()
for word in mutual_list:
    count[word] += 1
len(count)


# In[35]:


answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[ ]:


check = np.percentile(data.vote_average, 99)
data[data.vote_average > check].sort_values(by='vote_average', ascending=False)


# In[36]:


answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[ ]:


first_pair = data[(data.cast.str.contains("Johnny Depp")) & (data.cast.str.contains("Helena Bonham Carter"))]
second_pair = data[(data.cast.str.contains("Hugh Jackman")) & (data.cast.str.contains("Ian McKellen"))]
third_pair = data[(data.cast.str.contains("Vin Diesel")) & (data.cast.str.contains("Paul Walker"))]
fourth_pair = data[(data.cast.str.contains("Adam Sandler")) & (data.cast.str.contains("Kevin James"))]
fifth_pair = data[(data.cast.str.contains("Daniel Radcliffe")) & (data.cast.str.contains("Rupert Grint"))]

pairs = {'first_pair':len(first_pair), 'second_pair':len(second_pair), 'third_pair':len(third_pair), 
         'fourth_pair':len(fourth_pair), 'fifth_pair':len(fifth_pair)}
print(pairs)


# In[37]:


answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[ ]:


df_dir = pd.DataFrame(data.director.str.split('|').tolist()).stack().reset_index()
df_dir.columns =  ['data_index', 'qty_index', 'director']



def budget_film(x):
    if data.iloc[x]['margin'] > 0:
        return 1
    else:
        return 0

df_dir['margin_director'] = df_dir.data_index.apply(budget_film)
df_dir['count']=1


dir_grouped = df_dir.groupby(['director'])[['margin_director', 'count']].sum().reset_index()

dir_grouped['chance'] = dir_grouped['margin_director'] / dir_grouped['count']

display(dir_grouped[dir_grouped.director.isin(['Quentin Tarantino', 'Steven Soderbergh', 'Robert Rodriguez', 'Christopher Nolan', 'Clint Eastwood'])].sort_values(by='chance', ascending=False))


# In[38]:


answer_ls.append(4)


# # Submission

# In[39]:


len(answer_ls)


# In[40]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])

