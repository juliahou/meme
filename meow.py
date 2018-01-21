import praw
from datetime import datetime
from operator import itemgetter
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

#from json.json_util import dumps

reddit = praw.Reddit(client_id='rueV3_rhsdbfgg',
                     client_secret='45N-HS2wbzk1-AlWLolb-St2g7M',
                     user_agent='Python:com.meme:v1.0 (by /u/Leafwing)')

subreddit = reddit.subreddit('memes')
'''for submission in subreddit.rising(limit=1):
	print vars(submission)
    print str(datetime.utcfromtimestamp(submission.created_utc)) + " " + submission.title + " " + str(submission.ups)
    print vars(submission)
    print submission.subreddit.subscribers
print datetime.utcnow()'''

sr = ['memes', 'dankmemes']

# goes through list of strings and creates subreddit instance for each

def initialize_subreddits(sub_names):
	instances = []
	for sub in sr:
		instances.append(reddit.subreddit(sub))
	return instances

# goes through list of subreddit instances and gets top rising posts and their
# created time and their upvote number, as well as the subreddit size
def get_rising_post_attributes(instances):
    posts = []
    for inst in instances:
        posts.extend(inst.rising(limit=5))
    postToAttributes = {}
    for post in posts:
        postToAttributes[post] = (datetime.utcfromtimestamp(post.created_utc), post.ups, post.subreddit.subscribers)
    return postToAttributes

# gives score to a post based on created time, upvotes, and subreddit size
def score(created, ups, sr_size):
    now = datetime.utcnow()
    elapsed_time = now - created
    elapsed_time_minutes = elapsed_time.total_seconds()/60
    if(elapsed_time_minutes > 120):
        return 1.0 * ups / sr_size * 1000000
    else:
	   return 1.0 * ups / sr_size / (1.0 * elapsed_time_minutes / 120) * 1000000

# gives score to each post in d, sorts and takes top ones
def score_sort(d):
    result_list = []
    for key, value in d.iteritems():
        result_list.append((key, score(value[0],value[1],value[2])))
    result_list = sorted(result_list, key=itemgetter(1))
    result_list.reverse()
    print result_list
    return result_list

def test(l, n):
	ans = []
	for sub in l[:n]:
		submission = sub[0]
		utc = datetime.utcfromtimestamp(submission.created_utc)
		utc = utc.replace(tzinfo=from_zone)
		est = utc.astimezone(to_zone)
		ans.append([est, submission.title, sub[1], "http://reddit.com"+str(submission.permalink), submission.preview["images"][0]["source"]["url"]])
	return ans

def main(n):
	# d goes from post to attributes
	d = get_rising_post_attributes(initialize_subreddits(sr))
	return test(score_sort(d), n)

#lookup on origin?