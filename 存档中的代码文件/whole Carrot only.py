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
		if get_ground_type() != Grounds.Soil:
			till()
			plant(Entities.Carrot)
		else:
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			else:
				plant(Entities.Carrot)
			for i in range(get_world_size()):
				move(East)
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Carrot)
				else:
					if can_harvest():
						harvest()
						plant(Entities.Carrot)
					else:
						plant(Entities.Carrot)
					
		
	