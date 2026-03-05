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