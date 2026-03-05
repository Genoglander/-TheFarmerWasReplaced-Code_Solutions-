def Edge():
	for i in range(get_world_size()):
		if get_pos_x() != 31:
			move(East)
			for i in range(get_world_size()):
				if get_pos_y() != 31:
					move(South)
def is_even(n):
	return n % 2 == 0
def is_danshu(n):
	return n % 2 != 0
clear()
Edge()
while True: 
	for i in range(get_world_size()):
		move(North)
		for i in range(get_world_size()):
			if (is_even(get_pos_x()) and is_even(get_pos_y())):
				plant(Entities.Tree)
			else:
				move(East)
				if(is_danshu(get_pos_x()) and is_danshu(get_pos_y())):
					plant(Entities.Tree)
				else:
					move(North)