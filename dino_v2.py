import maths
import movement

world_size = 32
if not maths.is_even(world_size) and world_size > 2:
	world_size -= 1

clear()
set_world_size(world_size)

apple_goal = world_size**2 - 2
while True:
	apple_count = 0
	while apple_count < apple_goal:
		if apple_count == 0:
			change_hat(Hats.Dinosaur_Hat)
		v_dir = North
		for x in range(world_size):
			dist = world_size - 1
			if 0 < x and x < (world_size - 1):
				dist = world_size - 2
			for _ in range(dist):
				movement.move_by(1, v_dir)
				if get_entity_type() == Entities.Apple:
					apple_count += 1
			movement.move_by(1, East)
			if get_entity_type() == Entities.Apple:
				apple_count += 1
			v_dir = movement.dir_invert(v_dir)

		for _ in range(world_size - 1):
			movement.move_by(1, West)
			if get_entity_type() == Entities.Apple:
				apple_count += 1

	change_hat(Hats.Wizard_Hat)