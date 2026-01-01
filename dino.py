import movement
import maths

dir = {'v': North, 'h': East}
def farm(apple_count = 0, goal = 16):
	if apple_count == None:
		apple_count = 0

	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_entity_type() == Entities.Apple:
				apple_count += 1
				if apple_count == goal:
					clear()
					change_hat(Hats.Dinosaur_Hat)
					return 0
			move(dir['v'])
		dir['v'] = movement.dir_invert(dir['v'])
		move(dir['h'])
	dir['h'] = movement.dir_invert(dir['h'])
	dir['v'] = movement.dir_invert(dir['v'])
	return apple_count

apple_count = 0
goal = 16
world_size = goal / 2
if not maths.is_even(goal):
	world_size = (goal + 1) / 2
	
set_world_size(world_size)
change_hat(Hats.Dinosaur_Hat)

while True:
	apple_count = farm(apple_count, goal)
	