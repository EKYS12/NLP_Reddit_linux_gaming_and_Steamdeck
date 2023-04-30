# Author: Yasser Siddiqui
# Date: 2023/04/21

# Importing libraries

# Importing these libraries to get access to variables in the .env file that has the log in and client credentials
import os
from dotenv import load_dotenv

# Importing praw and pandas to get and export the data
import praw
import pandas as pd

# Importing datetime so that the files names are always labeled by the date they are retrieved and to prevent overwites.
import datetime

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables for user credentials
username = os.getenv('MY_USERNAME')
password = os.getenv('MY_PASSWORD')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET') 

# Define user agent
USER_AGENT = "praw_scraper_1.0 by Yasser Siddiqui"

# Create an instance of reddit class using the env variables and user agent variable
reddit = praw.Reddit(username=username,
                     password=password,
                     client_id=client_id,
                     client_secret=client_secret,
                     user_agent=USER_AGENT
)

# Getting the Date for later when we save the csv files. YYYY-mm-dd format
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Defining a function to gather data for our chosen subreddit
# This function takes in a subreddit name and then pulls out submissions.
# It will then take the submissions and store the Titles, Comments, and their ids into lists, which will then be stored into a DataFrame
# Lastly the Dataframe gets exported as a csv file to be stored and used in the project.
def pull_subreddit(subreddit_name):
    # Create the sub-reddit instance
    subreddit = reddit.subreddit(subreddit_name)
    
    # Purely to help keep make sure the function is running. The script can take 30 mins to run, so this can help ease the mind.
    print(f'Latest hot from {subreddit.display_name}')
    
    # Empty lists that we will append our data to 
    titles=[]
    title_ids=[]
    comments=[]
    comment_ids=[]
    
    # For loop to go through each submission. We are looking at the data in the "hot" category. We are taking the maximum amount of data the api will let us gather.
    for submission in subreddit.hot(limit=None):
        # Making sure not to get the pinned post at the top of the 'hot' section.
        if not submission.stickied:
            
            # Grabbing the titles of posts
            titles.append(submission.title)
            title_ids.append(submission.id)
    
            # This is used to not be stopped and get an error when the comment chain can get rather long, and lets us gather more data. 
            submission.comments.replace_more(limit=5)

            # Looping over comments and appending them to the list of comments.
            for comment in submission.comments.list():
                comments.append(comment.body)
                comment_ids.append(comment.id)

    # Taking the lists that we made and turning them into data frames.
    subred_title_df = pd.DataFrame(list(zip(title_ids, titles)), columns=['title_id', 'title']) 
    subred_comment_df = pd.DataFrame(list(zip(comment_ids, comments)), columns=['comment_id', 'comments']) 

    # Adding the target variable column, which is original subreddit the posts are from
    subred_title_df['subreddit'] = subreddit_name
    subred_comment_df['subreddit'] = subreddit_name

    # Exporting the dataframe as a csv. Labeling with the subreddit name and the date of collection
    subred_title_df.to_csv(f'../data/raw_data/{subreddit_name}_title_data_{current_date}.csv', index=False)
    subred_comment_df.to_csv(f'../data/raw_data/{subreddit_name}_comment_data_{current_date}.csv', index=False)

    return

# This function will be used to pull the data from the Top section. We only need to run this function once and then can comment out the call after that.
def pull_subreddit_top(subreddit_name):
    # Create the sub-reddit instance
    subreddit = reddit.subreddit(subreddit_name)
    
    # Purely to help keep make sure the function is running. The script can take 30 mins to run, so this can help ease the mind.
    print(f'Top from{subreddit.display_name}')
    
    # Empty lists that we will append our data to 
    titles=[]
    title_ids=[]
    comments=[]
    comment_ids=[]
    
    # For loop to go through each submission. We are looking at the data in the "hot" category. We are taking the maximum amount of data the api will let us gather.
    for submission in subreddit.top(limit=None, time_filter='all'):
        # Making sure not to get the pinned post at the top of the 'hot' section.
        if not submission.stickied:
            
            # Grabbing the titles of posts
            titles.append(submission.title)
            title_ids.append(submission.id)
    
            # This is used to not be stopped and get an error when the comment chain can get rather long, and lets us gather more data. 
            submission.comments.replace_more(limit=5)

            # Looping over comments and appending them to the list of comments.
            for comment in submission.comments.list():
                comments.append(comment.body)
                comment_ids.append(comment.id)

    # Taking the lists that we made and turning them into data frames.
    subred_title_df = pd.DataFrame(list(zip(title_ids, titles)), columns=['title_id', 'title']) 
    subred_comment_df = pd.DataFrame(list(zip(comment_ids, comments)), columns=['comment_id', 'comments']) 

    # Adding the target variable column, which is original subreddit the posts are from
    subred_title_df['subreddit'] = subreddit_name
    subred_comment_df['subreddit'] = subreddit_name

    # Exporting the dataframe as a csv. Labeling with the subreddit name and the date of collection
    subred_title_df.to_csv(f'../data/raw_data/{subreddit_name}_top_title_data_{current_date}.csv', index=False)
    subred_comment_df.to_csv(f'../data/raw_data/{subreddit_name}_top_comment_data_{current_date}.csv', index=False)

    return


# Calling function on our subreddits
pull_subreddit('linux_gaming')

pull_subreddit('SteamDeck')

# These two functions should only be run once.
# pull_subreddit_top('linux_gaming')

# pull_subreddit_top('SteamDeck')
