import random, primitives
from node import Node

TARGET = None

def gen_val():
	return random.randint(1, 1000)

prim_set = [primitives.add, primitives.sub, primitives.div, primitives.mult]
term_set = [gen_val]

total = prim_set + term_set

def gen_ind(n, depth = 3, no_term = False):
	choice = None
	if depth == 0:
		choice = gen_val
	elif no_term:
		choice = random.choice(prim_set)
	else:
		choice = random.choice(total)
	
	
	n.target = choice
	if choice in prim_set:
		n.left = Node()
		n.left = gen_ind(n.left, depth = depth-1)
		n.right = Node()
		n.right = gen_ind(n.right, depth = depth-1)
	else:
		n.target = choice()
	
	return n

def get_children(nodes):
	new_nodes = []
	for node in nodes:
		if node.right:
			new_nodes.append(node.right)
		if node.left:
			new_nodes.append(node.left)
		
	return new_nodes

def mutate(root, prob = 0.1, depth = 3):
	options = [root]
	choice = None
	
	while len(options) > 0:
		for item in options:
			if prob < random.random():
				choice = item
				options = None
				break
		
		if options is None:
			break
		
		options = get_children(options)
	
	if choice is not None:
		d = random.randint(0, depth)
		choice.right = gen_ind(Node(), d)
	
	return root

def copy_ind(old):
	new = Node()
	
	new.target = old.target
	if old.right:
		new.right = copy_ind(old.right)
	if old.left:
		new.left = copy_ind(old.left)
	
	return new

def eval(ind):
	val = ind.run()
	
	return abs(TARGET - val)

if __name__ == "__main__":
	ind = gen_ind(Node())
	
	ind.print_tree()
	
	new = mutate(ind, prob = 0.25)
	
	print("After mutation:")
	
	new.print_tree()
	
	print(new.run())
	
	