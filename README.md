# 【TheFarmerWasReplaced 编程农场代码库】
用来记录自己在编程农场里的学习和思考更新的库。这些代码都不是客观意义上的最优解，而是目前能够让我推动游戏进程范围内的最优解，随时都会更新。希望以后能够无限接近最优解。
A repository used to update my codes and mind chain during playing TheFarmerWasReplaced.

# -HarvestAll-
```
for i in range(get_world_size()):
		harvest()
		move(North)
		for i in range(get_world_size()):
			harvest()
			move(East)
```

# -Optimal Solution for Hay in Single Drone-
```
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
```

# -Optimal Solution for Wood in Single Drone-
```
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
```

# -Optimal Solution for Carrot in Single Drone-
```
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
```

# -Optimal Solution for Tree in Single Drone-
```
def GoEdge():
	for i in range(get_world_size()):
		if get_pos_x() != 31:
			move(East)
			for i in range(get_world_size()):
				if get_pos_y() != 31:
					move(South)
					
def is_even(n):
	return (n+2) % 2 == 0
	
def is_danshu(n):
	return (n+2) % 2 != 0

def heavestTree():
	if(get_entity_type() == Entities.tree):
		harvest()
	
clear()
GoEdge()

while True: 
	for i in range(get_world_size() + 1):
		heavestTree()
		move(North)
		for i in range(get_world_size() + 1):
			heavestTree()
			move(East)
			if (is_even(get_pos_x()) and is_even(get_pos_y())):
				heavestTree()
				plant(Entities.Tree)
				move(North)
			elif (is_danshu(get_pos_x()) and is_danshu(get_pos_y())):
					heavestTree()
					plant(Entities.Tree)
					move(North)
		heavestTree()
		move(North)
```

# -Optimal Solution for Pumpkin in Single Drone-
```
Bad_Path = []
Num_Dead_Pumpkin = 0
Result_Num_Dead_Pumpkin = 1

def GoEdge():
	for i in range(get_world_size()):
		if get_pos_x() != 31:
			move(East)
			for i in range(get_world_size()):
				if get_pos_y() != 31:
					move(South)
					
def tillSoil():
	if get_ground_type() != Grounds.Soil:
		till()
					
def detectBadPumpkin():
	if get_entity_type() == Entities.Dead_Pumpkin:
		current_pos = [get_pos_x(), get_pos_y()]
		Bad_Path.append(current_pos)
		
def Go_anywhere(x,y):
	while x != get_pos_x():
		move(East)
	while y != get_pos_y():
		move(North)
						
GoEdge()

while True:
	for i in range(get_world_size()):
		tillSoil()
		if can_harvest():
			harvest()
		plant(Entities.Pumpkin)
		move(North)
		for i in range(get_world_size()):
			tillSoil()
			if can_harvest():
				harvest()
			plant(Entities.Pumpkin)
			move(East)
		
	while Result_Num_Dead_Pumpkin > 0:	

		Num_Dead_Pumpkin = 0
		Bad_Path = []

		for i in range(get_world_size()):
			for i in range(get_world_size()):
				if get_entity_type() == Entities.Dead_Pumpkin:
					Num_Dead_Pumpkin = Num_Dead_Pumpkin + 1
					current_pos = [get_pos_x(), get_pos_y()]
					Bad_Path.append(current_pos)
					plant(Entities.Pumpkin)
				move(East)
			move(North)
		
		Result_Num_Dead_Pumpkin = Num_Dead_Pumpkin
		
		for i in Bad_Path:
			Go_X = i[0]
			Go_y = i[1]
			Go_anywhere(Go_X, Go_y)
			plant(Entities.Pumpkin)
	harvest()
```

# -Optimal Solution for Cactus in Single Drone-
```
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
```

# -Optimal Solution for Dinosaur's Bone in Single Drone-
//Unfinished!
```
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
```
