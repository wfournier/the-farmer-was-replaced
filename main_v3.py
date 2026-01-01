import farm

clear()

tasks = [
	{'id': 1, 'type': Entities.Pumpkin, 'width': 6, 'height': 6, 'x': 0, 'y': 0},
	{'id': 2, 'type': Entities.Pumpkin, 'width': 6, 'height': 6, 'x': 26, 'y': 0},
	{'id': 3, 'type': Entities.Pumpkin, 'width': 6, 'height': 6, 'x': 0, 'y': 26},
	{'id': 4, 'type': Entities.Tree, 'width': 4, 'height': 8, 'x': 10, 'y': 0},
	{'id': 5, 'type': Entities.Tree, 'width': 10, 'height': 4, 'x': 0, 'y': 6},
	{'id': 6, 'type': Entities.Tree, 'width': 10, 'height': 4, 'x': 22, 'y': 6},
	{'id': 7, 'type': Entities.Tree, 'width': 4, 'height': 8, 'x': 18, 'y': 0},
	{'id': 8, 'type': Entities.Tree, 'width': 10, 'height': 4, 'x': 0, 'y': 22},
	{'id': 9, 'type': Entities.Tree, 'width': 4, 'height': 8, 'x': 10, 'y': 24},
	{'id': 10, 'type': Entities.Tree, 'width': 4, 'height': 8, 'x': 18, 'y': 24},
	{'id': 11, 'type': Entities.Carrot, 'width': 8, 'height': 4, 'x': 0, 'y': 10},
	{'id': 12, 'type': Entities.Carrot, 'width': 12, 'height': 2, 'x': 10, 'y': 8},
	{'id': 13, 'type': Entities.Carrot, 'width': 8, 'height': 4, 'x': 24, 'y': 10},
	{'id': 14, 'type': Entities.Carrot, 'width': 8, 'height': 4, 'x': 24, 'y': 18},
	{'id': 15, 'type': Entities.Carrot, 'width': 8, 'height': 4, 'x': 0, 'y': 18},
	{'id': 16, 'type': Entities.Carrot, 'width': 12, 'height': 2, 'x': 10, 'y': 22},
	{'id': 17, 'type': Entities.Sunflower, 'width': 5, 'height': 6, 'x': 8, 'y': 13},
	{'id': 18, 'type': Entities.Sunflower, 'width': 6, 'height': 6, 'x': 13, 'y': 13},
	{'id': 19, 'type': Entities.Sunflower, 'width': 5, 'height': 6, 'x': 19, 'y': 13},
	{'id': 20, 'type': Entities.Cactus, 'width': 4, 'height': 6, 'x': 6, 'y': 0},
	{'id': 21, 'type': Entities.Cactus, 'width': 4, 'height': 6, 'x': 22, 'y': 0},
	{'id': 22, 'type': Entities.Cactus, 'width': 4, 'height': 8, 'x': 14, 'y': 0},
	{'id': 23, 'type': Entities.Cactus, 'width': 8, 'height': 4, 'x': 0, 'y': 14},
	{'id': 24, 'type': Entities.Cactus, 'width': 8, 'height': 4, 'x': 24, 'y': 14},
	{'id': 25, 'type': Entities.Cactus, 'width': 4, 'height': 6, 'x': 6, 'y': 26},
	{'id': 26, 'type': Entities.Cactus, 'width': 4, 'height': 8, 'x': 14, 'y': 24},
	{'id': 27, 'type': Entities.Cactus, 'width': 16, 'height': 3, 'x': 8, 'y': 19},
	{'id': 28, 'type': Entities.Cactus, 'width': 16, 'height': 3, 'x': 8, 'y': 10},
	{'id': 29, 'type': Entities.Treasure, 'size': 5, 'x': 27, 'y': 27},
	{'id': 30, 'type': Entities.Treasure, 'size': 5, 'x': 22, 'y': 27},
	{'id': 31, 'type': Entities.Treasure, 'size': 5, 'x': 27, 'y': 22},
	{'id': 32, 'type': Entities.Treasure, 'size': 5, 'x': 22, 'y': 22}
]

def get_task(params):
	func = None
	id, type, x, y = params['id'], params['type'], params['x'], params['y']
	if type == Entities.Treasure:
		# Wait a bit to prevent drones from being stuck in another drone
		for _ in range(5000):
			pass
		size = params['size']
		def _t():
			change_hat(Hats.Wizard_Hat)
			while True:
				#print(id)
				farm.treasure(size, x, y)
		func = _t
	else:
		width, height = params['width'], params['height']
		def _x():
			change_hat(Hats.Wizard_Hat)
			while True:
				#print(id)
				farm.cultivate(type, width, height, x, y)
		func = _x
		
	return func

for n in range(len(tasks) - 1):
	spawn_drone(get_task(tasks[n]))
	
get_task(tasks[len(tasks) - 1])()