def plant31x31Cactus():
	clear()
	Go00()
	for i in range(3):
		plant9x9()
		move(East)
	while get_pos_y() != 11:
		move(North)
	move(West)
	for i in range(3):
		plant9x9()
		move(East)
	while get_pos_y() != 21:
		move(North)
	move(West)
	for i in range(3):
		plant9x9()
		move(East)