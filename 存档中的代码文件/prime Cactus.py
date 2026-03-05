def Go00():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(South)
		
def Back_x():
	while get_pos_x() != 0:
		move(West)
		
def Back_y():
	while get_pos_y() != 0:
		move(South)
		
def sort_current_row():
	n = get_world_size()
	for i in range(n):
		for j in range(n-1):
			if measure() > measure(East):
				swap(East)
			move(East)
		Back_x()
		n -= 1
		
def sort_current_collon():
	n = get_world_size()
	for i in range(n):
		if measure() > measure(North):
			swap(North)
		move(North)
	Back_y()
	n -= 1
		
Go00()

for i in range(get_world_size()):
	sort_current_row()
	move(North)
	
Go00()


for i in range(get_world_size()):
	sort_current_collon()
	move(East)
	
harvest()
