import praw
import ConfigParser

"""Wrapping PRAW API to fully understand it"""
class reddit():
	# Instance of reddit api
	reddit_api = None

	"""API LOGIN INFORMATION"""
	# unique id of script
	CLIENT_ID = ''
	# secret key for api
	CLIENT_SECRET = ''
	# reddit password for api account
	PASSWORD = ''
	# official description for api use
	USER_AGENT = ''
	# reddit username for api account
	USERNAME = ''

	"""
	Main Method"""

	def main(self):
		print "LETS DO SOMETHING"

	"""
	Reads API login information from config.ini (gitignored for security purposes. See templates for a template"""

	def read_login_info(self):
		config = ConfigParser.ConfigParser()
		config.read('../data/config.ini')
		self.client_id = config.get('API_INFO', 'id')
		self.CLIENT_SECRET = config.get('API_INFO', 'secret')
		self.PASSWORD = config.get('API_INFO', 'password')
		self.USER_AGENT = config.get('API_INFO', 'user_agent')
		self.USERNAME = config.get('API_INFO', 'username')

	"""Logs into reddit api"""

	def login(self):
		self.read_login_info()
		self.reddit_api = praw.Reddit(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET,
		                              password=self.PASSWORD, user_agent=self.USER_AGENT, username=self.USERNAME)
		submissions = self.reddit_api.subreddit('OSU').hot(limit=1)
		for x in submissions:
			print x.title
			print str(x)
			print x
			print type(x)


api = reddit()
api.login()
