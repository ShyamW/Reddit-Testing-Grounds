import praw
import ConfigParser


def main():
	reddit = praw.Reddit(client_id='2_U-LEkcgmbwAw', client_secret='6Za54KDrCSkmRzcNpZLJ1eEEX6k', password='password', user_agent='utility to grab hot items', username='bot1417')
	print(reddit.read_only)
	submissions = reddit.subreddit('OSU').hot(limit=5)
	for x in submissions:
		print x.title

def read_login_info():
	config = ConfigParser.ConfigParser()
	config.read('data/config.ini')
	print config.get('api_cred', 'id')
	print config.get('api_cred', 'secret')
	print config.get('api_cred', 'passkey')
	print config.get('api_cred', 'description')
	print config.get('api_cred', 'username')





