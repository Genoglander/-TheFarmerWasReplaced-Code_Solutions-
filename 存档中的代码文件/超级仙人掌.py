def Go00():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(South)

def plant9x9():
	for i in range(5):
		for i in range(9):
			till()
			plant(Entities.Cactus)
			move(North)
		till()
		plant(Entities.Cactus)
		move(East)
		for i in range(9):
			till()
			plant(Entities.Cactus)
			move(South)
		till()
		plant(Entities.Cactus)
		move(East)

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
	while get_pos_y() != 22:
		move(North)
	move(West)
	for i in range(3):
		plant9x9()
		move(East)
		
		
def Back_x():
	while get_pos_x() != 0:
		move(West)
		
def Back_y():
	while get_pos_y() != 0:
		move(South)
		
def sort_current_row():
	n = 10
	for i in range(n):
		for j in range(n-1):
			if measure() != None and measure(East) != None:
				if measure() > measure(East):
					swap(East)
				move(East)
				
		for j in range(n-1):
			move(West)
		n -= 1

def sort_current_collon():
	n = 10
	for i in range(n):
		for j in range(n-1):
			if measure() != None and measure(North) != None:
				if measure() > measure(North):
					swap(North)
				move(North)
		for j in range(n-1):
			move(South)
		n -= 1
		
def arrange9x9():
	for i in range(10):
		sort_current_row()
		move(North)
	for i in range(10):
		move(South)
	for i in range(10):
		sort_current_collon()
		move(East)


#种植
plant31x31Cactus()
Go00()

#排序
arrange9x9()
move(East)
arrange9x9()
move(East)
arrange9x9()
while get_pos_y() != 11:
	move(North)
arrange9x9()
move(East)
arrange9x9()
move(East)
arrange9x9()
while get_pos_y() != 22:
	move(North)
arrange9x9()
move(East)
arrange9x9()
move(East)
arrange9x9()

#收获
for i in range(3):
	harvest()
	
	for i in range(2):
		for i in range(11):
			move(South)
		harvest()
			
	for i in range(11):
		move(East)
	while get_pos_y() != 22:
		move(North)

