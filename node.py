class Node:
	def __init__(self):
		self.target = None
		self.left = None
		self.right = None
	
	def print_tree(self, level = 0):
		print("At level {}: {}".format(level, self.target))
		if self.right:
			self.right.print_tree(level + 1)
		if self.left:
			self.left.print_tree(level + 1)
	
	def run(self):
		if type(self.target) == int:
			return self.target
		
		return self.target(self.left.run(), self.right.run())
		
			
			