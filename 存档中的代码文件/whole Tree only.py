def GoEdge():
	for i in range(get_world_size()):
		if get_pos_x() != 31:
			move(East)
			for i in range(get_world_size()):
				if get_pos_y() != 31:
					move(South)
					
def is_even(n):
	return (n+2) % 2 == 0
	
def is_danshu(n):
	return (n+2) % 2 != 0

def heavestTree():
	if(get_entity_type() == Entities.tree):
		harvest()
	
clear()
GoEdge()

while True: 
	for i in range(get_world_size() + 1):
		heavestTree()
		move(North)
		for i in range(get_world_size() + 1):
			heavestTree()
			move(East)
			if (is_even(get_pos_x()) and is_even(get_pos_y())):
				heavestTree()
				plant(Entities.Tree)
				move(North)
			elif (is_danshu(get_pos_x()) and is_danshu(get_pos_y())):
					heavestTree()
					plant(Entities.Tree)
					move(North)
		heavestTree()
		move(North)