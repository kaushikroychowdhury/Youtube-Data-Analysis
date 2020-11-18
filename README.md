# Youtube-Data-Analysis
Exploratory Data Analysis (EDA) of Youtube trending Dataset.

### Context
YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes). Note that they’re not the most-viewed videos overall for the calendar year”. Top performers on the YouTube trending list are music videos (such as the famously virile “Gangam Style”), celebrity and/or reality TV performances, and the random dude-with-a-camera viral videos that YouTube is well-known for.

This dataset is a daily record of the top trending YouTube videos.

Note that this dataset is a structurally improved version of this dataset https://www.kaggle.com/datasnaek/youtube.

### About the Dataset
This dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for the US, GB, DE, CA, IN, and FR regions (USA, Great Britain, Germany, Canada, India, and France, respectively), with up to 200 listed trending videos per day.

Each region’s data is in a separate file. Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count.

The data also includes a category_id field, which varies between regions. To retrieve the categories for a specific video, find it in the associated JSON. One such file is included for each of the five regions in the dataset.

### Acknowledgements
This dataset was collected using the YouTube API.

# Analysis of Trending Videos from Canada Region

## Visualization

Distribution of the dataset according to Year ...
![](/IMG_CA/Barplot/yearVSNo_of_videos.png)

![](/IMG_CA/Barplot/categoryVSno_of_videos.png)

As we can see 

### Category vs Parameters ..

![](/IMG_CA/Barplot/categoryVScomment_count.png)

![](/IMG_CA/Barplot/categoryVSdislikes.png)

![](/IMG_CA/Barplot/categoryVSlikes.png)

![](/IMG_CA/Barplot/categoryVSviews.png)

### category vs parameters .. in the year of 2017

![](/IMG_CA/Barplot/catVScomment_count_2017.png)

![](/IMG_CA/Barplot/catVSdislikes_2017.png)

![](/IMG_CA/Barplot/catVSlikes_2017.png)

![](/IMG_CA/Barplot/catVSviews_2017.png)

### category vs parameters .. in the year of 2018

![](/IMG_CA/Barplot/catVScomment_count_2018.png)

![](/IMG_CA/Barplot/catVSdislikes_2018.png)

![](/IMG_CA/Barplot/catVSlikes_2018.png)

![](/IMG_CA/Barplot/catVSviews_2018.png)

### 20 Popular Channels in Canada

![](/IMG_CA/Barplot/popular_channel.png)

### Correlation between variables ..

![](/IMG_CA/correlation/corr.png)

From the correlation matrix we can see that likes and views are highly correlated with the value of 0.83 and likes and comment_count are highly correlated with the value of 0.84.
To See wheather the Correlation matrix is correct or not, we can plot Scatter plot for verification ..

![](/IMG_CA/Scatterplot/viewsVSlikes.png)

Let's see the other scatter plots ..
![](/IMG_CA/Scatterplot/viewsVSdislikes.png)

![](/IMG_CA/Scatterplot/viewsVScomment_count.png)

Let's the relation between views and likes, dislikes, and comment count according to the year ..
### 2017
![](/IMG_CA/Scatterplot/viewsVSlikes_2017.png)

![](/IMG_CA/Scatterplot/viewsVSdislikes_2017.png)

![](/IMG_CA/Scatterplot/viewsVScomment_count_2017.png)

### 2018
![](/IMG_CA/Scatterplot/viewsVSlikes_2018.png)

![](/IMG_CA/Scatterplot/viewsVSdislikes_2018.png)

![](/IMG_CA/Scatterplot/viewsVScomment_count_2018.png)

### Lets see the Distribution of likes, Dislikes, views, and comment_counts
As the data is too much skewed, hence I applied Log Transformation of the data, so that we can have good insights ..

![](/IMG_CA/LogPDFs/log_likes.png)

![](/IMG_CA/LogPDFs/log_dislikess.png)

![](/IMG_CA/LogPDFs/log_views.png)

![](/IMG_CA/LogPDFs/log_comment_count.png)

### Wordcloud
Let's see which words are used most in tittle and tags..

### Title
![](/IMG_CA/WordCLoud/title.png)

### Tags
![](/IMG_CA/WordCLoud/tags.png)
