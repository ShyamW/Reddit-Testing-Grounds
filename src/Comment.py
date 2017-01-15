
class Comment():
	author = ''
	content = ''
	score = 0
	parent_id = ''


	def __init__(self, comment):
		self.author = comment.author
		self.content = comment.body
		self.score = comment.score
		self.parent_id = comment.parent_id
		print vars(comment)

	def print_results(self):
		print self.author
		print self.content
		print self.score
		print self.parent_id