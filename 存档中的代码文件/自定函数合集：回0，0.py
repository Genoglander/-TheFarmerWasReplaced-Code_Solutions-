def Go00():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(South)
		
Go00()