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