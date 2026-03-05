def Purple():
	for i in range(get_world_size()):
		if get_pos_x() != 31:
			move(East)
			for i in range(get_world_size()):
				if get_pos_y() != 31:
					move(South)
					
Purple()
while True: 
	for i in range(get_world_size()):
		move(North)
		plant(Entities.Bush)
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			for i in range(get_world_size()):
				move(East)
				plant(Entities.Bush)
				if can_harvest():
					harvest()
					plant(Entities.Bush)
	
	