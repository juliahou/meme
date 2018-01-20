import praw
from datetime import datetime

reddit = praw.Reddit(client_id='rueV3_rhsdbfgg',
                     client_secret='45N-HS2wbzk1-AlWLolb-St2g7M',
                     user_agent='Python:com.meme:v1.0 (by /u/Leafwing)')
subreddit = reddit.subreddit('memes')
for submission in subreddit.rising(limit=30):
	print str(datetime.utcfromtimestamp(submission.created_utc)) + " " + submission.title + " " + str(submission.ups)
print datetime.utcnow()

sr = ['memes']

# goes through list of strings and creates subreddit instance for each
def meow(l):

# goes through list of subreddit instances and gets top rising posts and their
# created time and their upvote number, as well as the subreddit size
def woof(l):

# gives score to a post based on created time, upvotes, and subreddit size
def score(created, ups, sr_size):
	return 1

# gives score to each subreddit instance in l, sorts and takes top ones
def quack(l):


#lookup on origin?