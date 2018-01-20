import praw
from datetime import datetime
#from json.json_util import dumps

reddit = praw.Reddit(client_id='rueV3_rhsdbfgg',
                     client_secret='45N-HS2wbzk1-AlWLolb-St2g7M',
                     user_agent='Python:com.meme:v1.0 (by /u/Leafwing)')

def test():
	ans = []
	subreddit = reddit.subreddit('memes')
	for submission in subreddit.rising(limit=1):
		print vars(submission)
		ans.append([datetime.utcfromtimestamp(submission.created_utc), submission.title, submission.ups, submission.preview["images"][0]["source"]["url"]])
	return ans

subreddit = reddit.subreddit('memes')
for submission in subreddit.rising(limit=1):
    print str(datetime.utcfromtimestamp(submission.created_utc)) + " " + submission.title + " " + str(submission.ups)
    print vars(submission)
    print submission.subreddit.subscribers
print datetime.utcnow()

sr = ['memes', 'dankmemes']
instances = []

# goes through list of strings and creates subreddit instance for each

def initialize_subreddits(sub_names):
    for sub in sr:
        instances.append(reddit.subreddit(sub))

# goes through list of subreddit instances and gets top rising posts and their
# created time and their upvote number, as well as the subreddit size
def get_rising_post_attributes(instances):
    posts = []
    for inst in instances:
        posts.extend(inst.rising(limit=3))
    postToAttributes = {}
    for post in posts:
        postToAttributes[post] = (post.created_utc, post.ups, post.subreddit.subscribers)

# gives score to a post based on created time, upvotes, and subreddit size
def score(created, ups, sr_size):
	return 1

# gives score to each post in l, sorts and takes top ones
def quack(l):
    return

#lookup on origin?