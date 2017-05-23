
class Comment():
	author = ''
	content = ''
	score = 0
	parent_id = ''


	def __init__(self, comment):
		self.author = str(comment.author)
		self.content = str(comment.body)
		self.score = str(comment.score)
		self.parent_id = str(comment.parent_id)


	def print_results(self):
		print ""
		print "*" + "\t" + self.author
		print "\t" + self.content
		print "\t" + self.score
		print "\t" + self.parent_id