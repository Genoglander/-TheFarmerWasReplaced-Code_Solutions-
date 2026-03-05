for i in range(get_world_size()):
		harvest()
		move(North)
		for i in range(get_world_size()):
			harvest()
			move(East)