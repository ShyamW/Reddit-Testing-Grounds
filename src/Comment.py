class Comment():
    reddit_comment = None
    reddit_api = None

    author = ''
    content = ''
    score = 0
    parent_id = ''

    """Constructor Methods for Comment"""

    def __init__(self, reddit_api, comment=None, id=None):
        # If constructing from id"""
        if id != None:
            self.reddit_comment = self.reddit_api.comment(id)
        # If constructing from praw comment object
        else:
            self.reddit_comment = comment
        # alias praw api
        self.reddit_api = reddit_api

    #
    # self.author = str(comment.author)
    # self.content = comment.body
    # self.score = str(comment.score)
    # self.parent_id = str(comment.parent_id)


    """Instance Methods for Comment """

    def reply(self, message):
        self.reddit_comment.reply(message)

    def print_results(self, indent):

        print self.reddit_comment.author
        # a = self.reddit_api.submission(
        print "\t" * indent + "Author:" + "\tu/" + str(self.reddit_comment.author) + "\tParent ID:" + \
              str(self.reddit_comment.parent_id) + "\t\tScore:" + str(self.reddit_comment.score)
        print "\t" * indent + str(self.reddit_comment.body.encode('utf-8')).replace('\n', '')
        print "-" * 50


def upvote(self):
    self.reddit_comment.upvote()


def report(self, report_message):
    self.reddit_comment.report(report_message)
