change_hat(Hats.Dinosaur_Hat)
Apple_poz = []
def Go_anywhere(x,y):
	n = 1
	m = 1
	if get_pos_x() > x:
		for i in range(n):
			n = get_pos_x() - x
			move(West)
	else:
		for i in range(m):
			m = x - get_pos_x()
			move(East)
	if get_pos_y() > y:
		for i in range(n):
			n = get_pos_y() - y
			move(South)
	else:
		for i in range(m):
			m = y - get_pos_y()
			move(North)
			
def findApple():
	Apple_poz = measure()
	Next_x = Apple_poz[0]
	Next_y = Apple_poz[1]
	Go_anywhere(Next_x, Next_y)
	
while True:
	findApple()