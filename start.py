import random, requests, os.path, wget, time, configparser, json, os
from PIL import Image
from instagrapi import Client


config = configparser.ConfigParser()
config.read("config.ini")


subreddits = json.loads(config.get('data', 'subreddits'))
reddit = "https://meme-api.herokuapp.com/gimme/"
hashtags = json.loads(config.get('data', 'hashtags'))
cooldown = config.getint('settings', 'time')
hashtags_quantity = config.getint('settings', 'hashtags_selection')

username = config['account']['username']
password = config['account']['password']


def main():
    while True:
        post_random = requests.get((reddit+random.choice(subreddits))).json()

    #Post_random individual data
        image_url = post_random['url']
        image_name = post_random['url'].split('/')[-1]
        post_link = post_random['postLink']
        title = post_random['title']
        author = post_random['author']
        subreddit = post_random['subreddit']
        hashtags_selection = " ".join(random.sample(hashtags, hashtags_quantity))

        description_post = f"\n{title}\n\n\nBy: u/{author}\nFrom: r/{subreddit}\n{post_link}\n{hashtags_selection}"

    #Check for repeated photo
        if os.path.isfile(f"memes/{image_name}"):
            print("\nRepeated")
            continue
        else:
            print("\nNo repeated")
        #Download image
            wget.download(image_url, out="memes")

    #Convert png to jpg
        if post_random["url"][-3::] == "png":
            image_png = Image.open(f"memes/{image_name}")
            rgb_im = image_png.convert('RGB')
            rgb_im.save(f"memes/{image_name[0:-3]}jpg")
            os.remove(f"memes/{image_name}")
        else:
            pass

    #Resize image
        meme = Image.open(f"memes/{image_name[0:-3]}jpg")

        if (meme.width/meme.height) <= 0.8:
            new_meme = meme.resize((meme.width, int(meme.width*1.25)))
            new_meme.save(f'memes/{image_name[0:-3]}jpg')
            print("\n4:5 Image")
        
        elif (meme.width/meme.height) <= 1.2:
            print("\n1:1 Image")
            pass
        
        else:
            new_meme = meme.resize((meme.width, int(meme.width*0.5625)))
            new_meme.save(f'memes/{image_name[0:-3]}jpg')
            print('\n16:9 Image')

        #Upload Photo
        bot.photo_upload(f"memes/{image_name[0:-3]}jpg", description_post)

        print(f'Done! Starting {cooldown} cooldown')

        time.sleep(cooldown)


if __name__ == "__main__":
    bot = Client()
    bot.login(username, password)
    main()
