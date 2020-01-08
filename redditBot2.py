import praw
import pdb
import re
import os

#Create a reddit instance
reddit = praw.Reddit('bot1')


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit('pythonforengineers')
for submissions in subreddit.hot(limit = 5):
    if submissions.id not in posts_replied_to:
        if re.search('I love python', submissions.title, re.IGNORECASE):
            submissions.reply("Botty McBotFace says: Me Too!!")
            print("Bot replying to: ", submissions.title)

            posts_replied_to.append(submissions.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")