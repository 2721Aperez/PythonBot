import praw 

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("monsterhunter")

for submission in subreddit.hot(limit=5):
    print('Title: ', submission.title)
    print('Text: ', submission.selftext)
    print("Score: ", submission.score)
    print("URL: ", submission.url)
    print("Visited: ", submission.visited)
    print("--------------------------------------\n")