import praw
import ConfigParser
import pprint
from Comment import Comment

"""Wrapping PRAW API to fully understand it"""
class reddit():
    # Instance of reddit api to be wrapped
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
    Main Method
    """
    def main(self):
        print "LETS DO SOMETHING"

    """
    Reads API login information from config.ini (gitignored for security purposes. See data/config_template for template
    """
    def read_login_info(self):
        config = ConfigParser.ConfigParser()
        config.read('../data/config.ini')
        self.CLIENT_ID = config.get('API_INFO', 'id')
        self.CLIENT_SECRET = config.get('API_INFO', 'secret')
        self.PASSWORD = config.get('API_INFO', 'password')
        self.USER_AGENT = config.get('API_INFO', 'user_agent')
        self.USERNAME = config.get('API_INFO', 'username')
        """If No Api key info in config file: warn user"""
        if len(self.CLIENT_ID) == 0:
            print "You need to insert your own values in data/config.ini"
            exit()

    """Processes the comment tree"""
    def process_comments(self, comments, indent):
        for top_level_comments in comments:
            Comment(top_level_comments).print_results(indent)
            #print '\t' * indent + str(top_level_comments.author).encode('utf-8')
            # recursively process nested comments
            self.process_comments(top_level_comments.replies, indent+1)



    """
    Processes a reddit post
    """
    def process_submission(self, submission):
        print 'Title: ' + str(submission.title)
        print 'Score: ' + str(submission.score)
        print 'Id: ' + str(submission.id)
        print 'Url: ' + str(submission.url)
        print 'Author: ' + str(submission.author)
        """Print all the comments in the thread"""
        print "-" * 50
        comments = submission.comments.list()
        self.process_comments(comments, indent=0)

    """
    fetches {@code data_count} hot posts from {@code subreddit}.
    """
    def fetch_data(self, subreddit, data_count):
        submissions = self.reddit_api.subreddit(subreddit).hot(limit=data_count)
        """Submissions is a list"""
        for submission in submissions:
            self.process_submission(submission)

    """
    Logs into reddit api
    """
    def login(self):
        self.read_login_info()
        self.reddit_api = praw.Reddit(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET,
                                      password=self.PASSWORD, user_agent=self.USER_AGENT, username=self.USERNAME)


if __name__ == '__main__':
    api = reddit()
    api.login()
    api.fetch_data(subreddit='OSU', data_count=1)
