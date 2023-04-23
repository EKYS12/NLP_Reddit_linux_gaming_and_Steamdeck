#!/bin/bash

python3 praw_scraper_subreddits.py

python3 title_data_merge.py

python3 comment_data_merge.py
