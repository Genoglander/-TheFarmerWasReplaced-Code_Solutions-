clear()
while True: 
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Grassland:
			till()
		else:
			if can_harvest():
				harvest()
				move(North)
				for i in range(get_world_size()):
					if get_ground_type() != Grounds.Grassland:
						till()
					else:
						if can_harvest():
							harvest()
							move(East)
	