import tasks

clear()

drones = [
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
	{'id': 1, 'type': Entities.Treasure, 'size': 32, 'x': 0, 'y': 0},
]

for i in range(len(drones) - 1):
	spawn_drone(tasks.get_task(drones, i))
	for _ in range(5000):
		pass

# Final drone
task = tasks.get_task(drones, len(drones) - 1)
task()