# Instagram-auto-meme-post
This script takes a random image from the subreddit of your choice and posts it to your instagram account.

------------


## Installation

You will need:
- [Python 3.6+](https://www.python.org/downloads/ "Python 3.6+")
- Any computer (Personal recommendation: Use a Raspberry Pi)

1. Download the repository via GitHub or Git.  `git clone https://github.com/EliasKernel/Instagram-auto-meme-post`
2. Install the required modules by running `python -m pip install -r requirements.txt`
3. Modify the  `config.ini` information


------------

## The config file
| Variable  | Defaults  | Explanation  |
| :------------: | :------------: | :------------: |
| username  | Username  | Your instagram username  |
| password  | Password  | Your Instagram password  |
| subreddits  | ["Memes", "Dankmemes"]  | List of all subreddits  |
| hashtags  | ["#Hashtag1","#Hashtag2","#Hashtag3"]  | List of all Hashtags  |
| time  | 3600  | Time between posts (in seconds)  |
| hashtag_selection  | 3  |  How many hashtags |


