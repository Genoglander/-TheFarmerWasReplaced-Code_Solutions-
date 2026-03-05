def Purple():
	for i in range(get_world_size()):
		if get_pos_x() != 16:
			move(East)
		else:
			for i in range(get_world_size()):
				if get_pos_y() != 16:
					move(South)
					

Purple()
print("Hay")
move(South)
print(num_items(Items.Hay))
move(South)
print("Wood")
move(South)
print(num_items(Items.Wood))
move(South)
print("Carrot")
move(South)
print(num_items(Items.Carrot))
move(South)
print("Pumpkin")
move(South)
print(num_items(Items.Pumpkin))
move(South)
print("Cactus")
move(South)
print(num_items(Items.Cactus))
move(South)
print("Water")
move(South)
print(num_items(Items.Water))
move(South)
print("Fertilizer")
move(South)
print(num_items(Items.Fertilizer))
move(South)