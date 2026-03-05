Bad_Path = []

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
	while x != get_pos_x:
		move(East)
	while y != get_pos_y:
		move(South)
						
GoEdge()

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
		

for i in range(get_world_size()):
	if get_entity_type() == Entities.Dead_Pumpkin:
		current_pos = [get_pos_x(), get_pos_y()]
		Bad_Path.append(current_pos)
		plant(Entities.Pumpkin)
	move(North)
	for i in range(get_world_size()):
		if get_entity_type() == Entities.Dead_Pumpkin:
			current_pos = [get_pos_x(), get_pos_y()]
			Bad_Path.append(current_pos)
			plant(Entities.Pumpkin)
		move(East)
		
for i in range(get_world_size()):
		harvest()
		move(East)
		for i in range(get_world_size()):
			harvest()
			move(South)