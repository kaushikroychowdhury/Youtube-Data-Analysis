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

### Visualization

Distribution of the dataset according to Year ...
![](/IMG_CA/Barplot/yearVSNo_of_videos.png)

Category vs Parameters ..

![](/IMG_CA/Barplot/categoryVScomment_count.png)

As we can see 

![](/IMG_CA/Barplot/categoryVSdislikes.png)
![](/IMG_CA/Barplot/categoryVSlikes.png)
![](/IMG_CA/Barplot/categoryVSviews.png)
![](/IMG_CA/Barplot/catVScomment_count_2017.png)
![](/IMG_CA/Barplot/catVSdislikes_2017.png)
![](/IMG_CA/Barplot/catVSlikes_2017.png)
![](/IMG_CA/Barplot/catVSviews_2017.png)
![](/IMG_CA/Barplot/popular_channel.png)
![](/IMG_CA/Barplot/categoryVSno_of_videos.png)
