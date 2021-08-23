# Instagram-auto-meme-post
This script selects a random subreddit from a list, chooses a random image and posts it to instagram.

Uses [Meme_Api from D3vd](https://github.com/D3vd/Meme_Api "Meme_Api from D3vd") and [instagrapi from adw0rd](https://github.com/adw0rd/instagrapi "instagrapi from adw0rd")



## Installation

You will need:
- [Python 3.6+](https://www.python.org/downloads/ "Python 3.6+")
- Any computer (Personal recommendation: Use a Raspberry Pi)

1. Download the repository via GitHub or Git.  `git clone https://github.com/EliasKernel/Instagram-auto-meme-post`
2. Install the required modules by running `python -m pip install -r requirements.txt`
3. Modify the  `config.ini` information
4. Use `python start.py` if you have installed only python 3 or `python3 start.py` if you have python 2 and 3

------------

## The config file
| Variable  | Defaults  | Explanation  |
| :------------: | :------------: | :------------: |
| username  | Username  | Your instagram username  |
| password  | Password  | Your Instagram password  |
| subreddits  | ["Memes", "Dankmemes"]  | List of all subreddits  |
| hashtags  | ["#Hashtag1", "#Hashtag2", "#Hashtag3", "#Hashtag4", "#Hashtag5"]  | List of all Hashtags  |
| time  | 21600  | Time between posts (in seconds)  |
| hashtag_selection  | 3  |  How many hashtags |

Usage recommendations
------------
- Adds more than 3 hours of cooldown to avoid limitations by instagram.
- Add a large list of hashtags and only select from 3 or 5, to avoid shadowbans.


### Disclaimer ⚠️
I am not responsible for the inappropriate use of this bot.
