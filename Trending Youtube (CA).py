import pandas as pd
import numpy as np
import statsmodels.stats.descriptivestats as sm
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud
from collections import Counter
import datetime
import json
sns.set()
desired_width=500
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

CA_vid = pd.read_csv("CAvideos.csv")
ca_vid = pd.read_csv("CAvideos.csv")

with open("CA_category_id.json",'r') as f:
    CA_id = json.load(f)

dic = {}

for i in CA_id['items']:
    dic[int(i['id'])] = i['snippet']['title']

ca_vid['category_name'] = ca_vid['category_id'].map(dic)


print(ca_vid.describe(include = 'all'))

print(ca_vid.columns)
print(ca_vid.info())
ca_vid['description'] = ca_vid['description'].fillna(value=" ")

df = sm.describe(data=ca_vid)
print(df)

### Number of videos according to year ...
year = ca_vid['trending_date'].apply(lambda x: '20' + x[:2]).value_counts().to_frame().reset_index().rename(columns = {'index':'year', 'trending_date':'No_of_videos'})

# here, value_counts() returns number of unique values
# to_frame() converts series to data-frame
# reset_index() add indices
sns.barplot(x = 'year', y = 'No_of_videos', data = year)
print(plt.show())

print(ca_vid['trending_date'].apply(lambda x: '20' + x[:2]).value_counts(normalize=True))
# so as we can see the data is collected on the year 2017 and 2018 with 23% and 77% number of videos respectively ...

data_2017 = ca_vid[ca_vid['trending_date'].apply(lambda x: x[:2]) == '17']
data_2018 = ca_vid[ca_vid['trending_date'].apply(lambda x: x[:2]) == '18']

### Exploration on the Basis of Year ..

sns.barplot(x='category_name', y='views', data=data_2017)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='likes', data=data_2017)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='dislikes', data=data_2017)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='comment_count', data=data_2017)
plt.xticks(rotation = 90)
print(plt.show())

#################################################################### 2018

sns.barplot(x='category_name', y='views', data=data_2018)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='likes', data=data_2018)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='dislikes', data=data_2018)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='comment_count', data=data_2018)
plt.xticks(rotation = 90)
print(plt.show())

### Scatter plot
sns.relplot(x='views', y='likes', hue="category_id", palette="ch:s=.25,rot=-.25", data=data_2017)
print(plt.show())

sns.relplot(x='views', y='dislikes', hue="category_id", data=data_2017)
print(plt.show())

sns.relplot(x='views', y='comment_count', hue="category_id", palette="ch:s=.25,rot=-.75", data=data_2017)
print(plt.show())

sns.relplot(x='views', y='likes', hue="category_id", palette="ch:s=.25,rot=-.25", data=data_2018)
print(plt.show())

sns.relplot(x='views', y='dislikes', hue="category_id", data=data_2018)
print(plt.show())

sns.relplot(x='views', y='comment_count', hue="category_id", palette="ch:s=.25,rot=-.75", data=data_2018)
print(plt.show())


### For getting to know about the data .. PDFs ....
sns.displot(ca_vid['views'])
print(plt.show())
sns.displot(ca_vid['likes'])
print(plt.show())
sns.displot(ca_vid['dislikes'])
print(plt.show())
sns.displot(ca_vid['comment_count'])
print(plt.show())

### for better visualization and to get better insights from the data , we need to transform the data ...
### log Transformation of views, likes, dislikes, comment_count

def float_inf(val):
    if val == float('inf') or val == float('-inf'):
        return 0
    else:
        return val


log_views = np.log(ca_vid['views'])
log_likes = np.log(ca_vid['likes'])
log_dislikes = np.log(ca_vid['dislikes'])
log_comment_count = np.log(ca_vid['comment_count'])

ca_vid['log_views'], ca_vid['log_likes'], ca_vid['log_dislikes'], ca_vid['log_comment_count'] = [log_views, log_likes, log_dislikes, log_comment_count]
ca_vid['log_likes'] = ca_vid['log_likes'].apply(float_inf)
ca_vid['log_dislikes'] = ca_vid['log_dislikes'].apply(float_inf)
ca_vid['log_comment_count'] = ca_vid['log_comment_count'].apply(float_inf)
print(ca_vid.describe())


sns.distplot(ca_vid['log_views'])
print(plt.show())
sns.distplot(ca_vid['log_likes'])
print(plt.show())
sns.distplot(ca_vid['log_dislikes'])
print(plt.show())
sns.distplot(ca_vid['log_comment_count'])
print(plt.show())

### Scatter plot
sns.relplot(x='views', y='likes', hue="category_id", palette="ch:s=.25,rot=-.25", data=ca_vid)
print(plt.show())

sns.relplot(x='views', y='dislikes', hue="category_id", data=ca_vid)
print(plt.show())

sns.relplot(x='views', y='comment_count', hue="category_id", palette="ch:s=.25,rot=-.75", data=ca_vid)
print(plt.show())

### Bar plots .. (CATEGORY VS VIEWS, LIKES, DISLIKES, COMMENT_COUNT..............................

sns.barplot(x='category_name', y='views', data=ca_vid)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='likes', data=ca_vid)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='dislikes', data=ca_vid)
plt.xticks(rotation = 90)
print(plt.show())

sns.barplot(x='category_name', y='comment_count', data=ca_vid)
plt.xticks(rotation = 90)
print(plt.show())

###Correlation between dataset variables
#Correlation is represented as a value between -1 and +1 where +1 denotes the highest positive correlation, -1 denotes
#the highest negative correlation, and 0 denotes that there is no correlation.

plt.subplots(figsize = (10,6))
sns.heatmap(ca_vid.corr(), annot=True, cmap=sns.cubehelix_palette(as_cmap=True))
print(plt.show())


### Most common words used in video tittles ..

title_words = list(ca_vid['title'].apply(lambda x: x.split()))
title_words = [x for y in title_words for x in y]
print(Counter(title_words).most_common(25))

wc = wordcloud.WordCloud(width=1200, height=500,
                         collocations=False, background_color="white",
                         colormap="tab20b").generate(" ".join(title_words))
plt.subplots(figsize = (15,10))
plt.imshow(wc, interpolation='bilinear')
plt.grid(None)
plt.axis('off')
print(plt.show())

### Most common words used in video tags ..

tags_words = list(ca_vid['tags'].apply(lambda x: x.split()))
tags_words = [x for y in tags_words for x in y]
# print(Counter(tags_words).most_common(25))

wc = wordcloud.WordCloud(width=1200, height=500,
                         collocations=False, background_color="white",
                         colormap="tab20b").generate(" ".join(tags_words))
plt.subplots(figsize = (15,10))
plt.imshow(wc, interpolation='bilinear')
plt.grid(None)
plt.axis('off')
print(plt.show())


### Most trending videos according to channel tittle .
plt.subplots(figsize = (10,6))
df = ca_vid['category_name'].value_counts().to_frame().reset_index().rename(columns={'index':'category_name', 'category_name':'no_of_videos'})
sns.barplot(y='no_of_videos', x='category_name', data=df, palette=sns.cubehelix_palette(n_colors=20, reverse=True))
plt.xticks(rotation= 90)
print(plt.show())

plt.subplots(figsize = (10,6))
df = ca_vid.groupby('channel_title').size().reset_index(name='no_of_videos').sort_values('no_of_videos', ascending=False).head(20)
sns.barplot(x='no_of_videos', y='channel_title', data=df, palette=sns.cubehelix_palette(n_colors=20, reverse=True))
print(plt.show())


### Analyzing the time and days of trending and publishing
ca_vid['publishing_day'] = ca_vid['publish_time'].apply(lambda x: datetime.datetime.strptime(x[:10], "%Y-%m-%d").date().strftime('%a'))
ca_vid['publishing_hour'] = ca_vid['publish_time'].apply(lambda x: x[11:13])
ca_vid.drop(labels=['publish_time'], axis=1, inplace=True)

df = ca_vid['publishing_day'].value_counts().to_frame().reset_index().rename(columns={'index':'day', 'publishing_day':'num_of_videos'})
plt.subplots(figsize = (10,6))
sns.barplot(x='day', y='num_of_videos', data=df, palette="ch:s=.25,rot=-.75")
print(plt.show())

df = ca_vid['publishing_hour'].value_counts().to_frame().reset_index().rename(columns={'index':'hour', 'publishing_hour':'num_of_videos'})
df = df.sort_values(by=['hour'])
ax = plt.subplots(figsize = (10,6))
sns.barplot(x='hour', y='num_of_videos', data=df, palette="ch:s=.25,rot=-.25")
print(plt.show())

