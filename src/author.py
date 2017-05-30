from Comment import Comment

class author():
    reddit_api = None
    redditor = None

    def __init__(self, reddit_api, author_name):
        self.reddit_api = reddit_api
        self.redditor = self.reddit_api.redditor(author_name)

    def print_comments(self):
        for comment in self.redditor.comments.top(limit=None):
            Comment(self.reddit_api, comment).print_results(0)

