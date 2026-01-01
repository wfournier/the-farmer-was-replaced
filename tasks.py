import farm

# Returns a function to be executed by a drone
def get_task(tasks, i):
	params = tasks[i]
	func = None
	id, type, x, y = params['id'], params['type'], params['x'], params['y']
	if type == Entities.Treasure:
		# Wait a bit to prevent drones from being stuck in another drone's maze
		for _ in range(5000):
			pass
		size = params['size']
		def _t():
			change_hat(Hats.Top_Hat)
			while True:
				#print(id)
				farm.treasure(size, x, y)
		func = _t
	else:
		width, height = params['width'], params['height']
		def _x():
			change_hat(Hats.Top_Hat)
			while True:
				#print(id)
				farm.cultivate(type, width, height, x, y)
		func = _x
		
	return func