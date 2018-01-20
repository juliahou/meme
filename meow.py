import praw
from datetime import datetime

reddit = praw.Reddit(client_id='rueV3_rhsdbfgg',
                     client_secret='45N-HS2wbzk1-AlWLolb-St2g7M',
                     user_agent='Python:com.meme:v1.0 (by /u/Leafwing)')
subreddit = reddit.subreddit('memes')
for submission in subreddit.rising(limit=30):
	print str(datetime.utcfromtimestamp(submission.created_utc)) + " " + submission.title + " " + str(submission.ups)
print datetime.utcnow()

def score(created, ups, sr_size):
	return 1

#lookup on origin?