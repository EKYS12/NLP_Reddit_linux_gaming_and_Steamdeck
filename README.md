# README

*This project is a work in progress*

In this project I have taken data on the Titles and Comments from the subreddits of r/SteamDeck and r/linux_gaming to build a classification model that can correctly predict which of the two subreddits a random post is from.

## Why This Interested Me

I decided to do this project on these subreddits because the topics were of interest to me. I personally own a Steam Deck and was one of the people who reserved one when they were still being set to release. I am also a Linux user, however, I still haven't made the jump to gaming on Linux just yet outside of my steam deck (but that's primarily due to hardware reasons, something that will change in the future).

The SteamDeck is seen as revolutionary when it comes to the Linux gaming space, and was expected to be a huge push towards stronger support for gaming on Linux. However, an interesting question to me was how separated was the SteamDeck community to the general Linux gaming community. How much was the SteamDeck actually pushing people towards the Linux space and how isolated was it from the greater Linux space. Is the SteamDeck it's own little bubble? After all many users of the SteamDeck do not use Linux at all period outside of the device, and many may have not even heard of Linux before the SteamDeck (and a few probably still don't).

The goal of this project is to see how well a NLP Classification Model can differentiate posts between the two related subreddits. The stronger the model preforms, the more it stands to reason that the two spheres of interests are separated. However, the worse the model preforms, the more it stands to reason that two spheres are highly integrated.

## Starting Hypothesis

My starting hypothesis is that the rate that the model will predict true values for the r/linux_gaming subreddit will be higher than it's ability to predict posts from r/SteamDeck. This is because the SteamDeck itself is a big topic for both subreddits. This will make any post about the SteamDeck difficult to classify, while posts outside of the SteamDeck itself will probably end up being classified towards r/linux_gaming.

## Data Collection Scripts

To start the project I begin by writing scripts that handle our data collection process. I chose to use the reddit API through PRAW as the uptime of pushshift was very limited and it seemed like too much of a hassle to me. By writing a script for PRAW I can just set up the script, make sure it works, and then run it every few days to collect new data. This would allow me to get the data I would need, even if PRAW limits you to only being able to pull the last 1000 posts in the specific category that you specify (which in this case, we use the "Hot" category).

The scripts take in the title and comment data from the posts in the specific subreddit and stores them in lists. From there I can the take the lists and put them together in a Pandas Dataframe. Finally I can just export the dataframes as csv files. I make sure to label each of these csv files with the date that they were collected so as to not cause overwriting.

After collecting the data from various days, we can use other scripts that go through the process of merging the datasets together. We can just import the csv files into dataframes, and then concat the dataframes together to merge all our datasets. From there you just export them as csv files again.

Will all the scripts written, you can then just write a bash script that just runs each script for you in order when you call it. We could further automate this with a CRON job, but as I was not running this project on a server at the time, that would be a pointless step.

## Exploratory Data Analysis

From here on, a lot of the proccess is documented in the notebooks themselves, so I will be more brief. EDA was done on the comment and title data that was gathered. After some brief cleaning, the data was processed and vectorized. I explored the differences of length, word count, frequent words, and easily noticeable sentiment from both subreddits. From there I was able to pick up on a few patterns that the machine learning models might pick up on as they train themselves to identify between the two subreddits. 

## Modeling

In this project I used the modeling techinques of ADA Boosting over a Random Forest and a Logistic Regression, and Stacking a Random Forest, Bagging Model, and KNN model together and feeding them into a Logistic Regression. After examining their performances over the various metrics, it seemed that the ADA Boosted Logistic Regression was the model that performed the best over all, and had the highest accuracy. I would like to try exploring other boosting methods over a logistic regression in the future on this data set if I ever find the time. I am interested to see the difference in performance of an ADA Boost, Gradient Boost, and XGBoost with this data set.

## Conclusions

All 3 models did pretty well over all at predicting whether a post was from one subreddit over the other. ADA Boosted Logistic Regression seemed to have done the best. Our hypothesis of the two subreddit's differences making them easily identifiable seems to be true. This can be an indication that the SteamDeck community isn't as integrated into the greater Linux Gaming space as some may wish. However, it is not a hard conclusion. This is merely the results of my own testing, and not the fairest comparison. r/SteamDeck is a highly focused subreddit in comparison to r/linux_gaming, and their subject matter is going to differ. But it seems that they differ pretty greatly even though both love the same device, and both are about using computer technology to play PC video games on a linux OS. 
