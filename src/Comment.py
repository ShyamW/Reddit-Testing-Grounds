
class Comment():
	author = ''
	content = ''
	score = 0
	parent_id = ''


	def __init__(self, comment):
		self.author = str(comment.author)
		self.content = comment.body
		self.score = str(comment.score)
		self.parent_id = str(comment.parent_id)


	def print_results(self, indent):
		print "\t"*indent + "Author:" + "\tu/" + self.author + "\tParent ID:" + self.parent_id + "\t\tScore:" + self.score
		print "\t"*indent + str(self.content.encode('utf-8')).rstrip('\n')
		print "-" * 50