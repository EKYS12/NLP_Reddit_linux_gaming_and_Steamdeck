# Author: Yasser Siddiqui
# Heavily built off of skeleton code from CHAT-GPT
# Date: 2023/04/22

# Importing libraries
import os
import pandas as pd

# This function will just grab the title data for the specific subreddit identified, and then merge them all into one data set.
def merge_data_subreddit(subreddit_name):
    # Set the directory where the csv files are stored
    dir_path = '../data/raw_data/'

    # Define the naming pattern to filter csv files
    name_pattern = f'{subreddit_name}_comment_data_'

    # Get a list of all csv files in the directory that match the naming pattern
    comment_csv_files = [filename for filename in os.listdir(dir_path) if filename.endswith('.csv') and name_pattern in filename]

    # Looping through the csv files and creating a list of dataframes
    dataframes = []
    for csv_file in comment_csv_files:
        df = pd.read_csv(os.path.join(dir_path, csv_file))
        dataframes.append(df)

    # Concatenate all the dataframes into a single dataframe
    merged_df = pd.concat(dataframes)

    # Get rid of any duplicates cause by the merge
    merged_df.drop_duplicates(subset='comment_id', inplace=True)

    # Export the merged dataframe as a new csv file
    merged_df.to_csv(f'../data/half_merged_data/{subreddit_name}_merged_comment_data.csv', index=False)

    return

# This function takes the 2 different merged sets for each subreddit and merges them into one data set. We do this in 2 steps so as to keep a copy of the seperated merged sets, for data storage safety.
def merge_data(subreddit1, subreddit2):

    # Set the directory where the csv files are stored
    dir_path = '../data/half_merged_data/'

    # Define the naming pattern to filter csv files
    name_pattern1 = f'{subreddit1}_merged_comment_data'
    name_pattern2 = f'{subreddit2}_merged_comment_data'

    # Get a list of all csv files in the directory that match the naming pattern
    csv_files = [filename for filename in os.listdir(dir_path) if filename.endswith('.csv') and (name_pattern1 in filename or name_pattern2 in filename)]

    # Looping through the csv files and creating a list of dataframes
    dataframes = []
    for csv_file in csv_files:
        df = pd.read_csv(os.path.join(dir_path, csv_file))
        dataframes.append(df)

    # Concatenate all the dataframes into a single dataframe
    merged_df = pd.concat(dataframes)

    # Get rid of any duplicates cause by the merge
    merged_df.drop_duplicates(subset='comment_id', inplace=True)

    # Export the merged dataframe as a new csv file
    merged_df.to_csv(f'../data/{subreddit1}_{subreddit2}_merged_comment_data.csv', index=False)

    return

# Calling the function on our subreddits
merge_data_subreddit('linux_gaming')

merge_data_subreddit('SteamDeck')

merge_data('linux_gaming', 'SteamDeck')
