import utils
import maths
import movement
import water

def cultivate(type, patch_width, patch_height, start_x = 0, start_y = 0, vertical_dir = North, horizontal_dir = East):
	movement.move_to(start_x, start_y)
	for x in range(patch_width):
		for y in range(patch_height):
			relative_y = y
			if vertical_dir == South:
				relative_y = patch_height - y - 1
				
			pos_x, pos_y = (start_x + x, start_y + relative_y)
			tmp_type = check_companion(pos_x, pos_y)
			if tmp_type == None:
				tmp_type = type
						
			if type == Entities.Pumpkin:
				if pumpkin(patch_width, patch_height, start_x, start_y, x, y) == "STOP":
					return
			elif type == Entities.Cactus:
				cactus(patch_width, patch_height, pos_x, pos_y, start_x, start_y, x, relative_y)
			elif type == Entities.Dinosaur:
				pass
			elif tmp_type == Entities.Tree:
				tree(x, relative_y)
			elif tmp_type == Entities.Bush:
				bush()
			elif tmp_type == Entities.Carrot:
				carrot()
			elif tmp_type == Entities.Sunflower:
				sunflower()
			else:
				grass()

			if y == (patch_height - 1):		
				vertical_dir = movement.dir_invert(vertical_dir)
			else:
				movement.move_by(1, vertical_dir)
			
		if x != (patch_width - 1):
			movement.move_by(1, East)

companions = {}
# Check if the tile has a companion and add its position to a dictionary
# Also, if there is a companion that should be planted at this position, return its type
def check_companion(x, y):
	companion_type, comp_coords = (None, None)
	companion = get_companion()
	if companion != None:
		companion_type, comp_coords = companion
				
	if not comp_coords in companions:
		companions[comp_coords] = companion_type
				
	type = None
	if (x, y) in companions:
		type = companions.pop((x, y))
		
	return type
			
# Plant then harvest some grass
def grass():
	if can_harvest():
		harvest()
	
	plant(Entities.Grass)

# Plant then harvest some trees and bushes in a grid pattern
def tree(x, y):	
	if can_harvest():
		harvest()
	
	if (maths.is_even(x) and maths.is_even(y)) or (not maths.is_even(x) and not maths.is_even(y)):
		plant(Entities.Tree)
	else:
		plant(Entities.Grass)

# Plant then harvest some bushes		
def bush():
	if can_harvest():
		harvest()
		
	plant(Entities.Bush)
	
# Plant then harvest some carrots
def carrot():
	if can_harvest():
		harvest()
		
	if get_ground_type() != Grounds.Soil:
		till()
	
	plant(Entities.Carrot)
	water.fill()
	
# Plant then harvest some sunflowers
sunflowers = []
def sunflower():
	if can_harvest():
		harvest()
		
	if get_ground_type() != Grounds.Soil:
		till()
	
	plant(Entities.Sunflower)
	water.fill()

# Check if sunflower should be harvested then plant another
# Old method, is way less efficient than just planting and harvesting without checks
def sunflower_old():
	entity = get_entity_type()
	if len(sunflowers) >= 10 and can_harvest() and entity == Entities.Sunflower:
		size = measure()
		if size >= max(sunflowers):
			harvest()
			sunflowers.remove(size)
		
	if entity != Entities.Sunflower:
		if can_harvest():
			harvest()
		
		if get_ground_type() != Grounds.Soil:
			till()
			
		plant(Entities.Sunflower)
		size = measure()
		if size != None:
			sunflowers.append(size)

# Plant pumpkins until they are all grown into a big one then harvest it
# Replant dead pumpkins with fertilizer
pumpkins = {}
def pumpkin(patch_width, patch_height, start_x, start_y, x, y):
	if get_ground_type() != Grounds.Soil:
		till()
		
	entity = get_entity_type()
	if entity != Entities.Pumpkin:
		plant(Entities.Pumpkin)
		if entity == Entities.Dead_Pumpkin and num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
		else:
			water.fill()
	
	if x == 0 and y == 0:
		pumpkins[(start_x, start_y)] = measure()

	if x == (patch_width - 1) and measure() == pumpkins[(start_x, start_y)] and can_harvest():
		harvest()
		cultivate(Entities.Pumpkin, patch_width, patch_height, start_x, start_y)
		return "STOP"
	
	return "CONTINUE"

# Plant cacti and sort them into ascending order then harvest them all at once when sorted
sorted_cactus = {}
def cactus(patch_width, patch_height, pos_x, pos_y, start_x, start_y, x, y):
	if pos_x == start_x and pos_y == start_y:
		if (start_x, start_y) in sorted_cactus and sorted_cactus[(start_x, start_y)] and can_harvest():
			harvest()
			sorted_cactus.pop((start_x, start_y))
		else:
			sorted_cactus[(start_x, start_y)] = True
	
	if get_ground_type() != Grounds.Soil:
		till()
		
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	
	if x != (patch_width - 1):
		size_right = measure(East)
		if size_right != None and measure() > size_right:
			swap(East)
			sorted_cactus[(start_x, start_y)] = False
		
	if y != (patch_height - 1):
		size_up = measure(North)
		if size_up != None and measure() > size_up:
			swap(North)
			sorted_cactus[(start_x, start_y)] = False
		
# Create a maze from a bush then hug the right wall until the treasure is found
def treasure(maze_size, start_x, start_y):
	if maths.is_even(maze_size):
		movement.move_to(start_x + maze_size / 2, start_y + maze_size / 2)
	else:
		movement.move_to(start_x + (maze_size - 1) / 2, start_y + (maze_size - 1) / 2)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1))
	# Order is clockwise: N -> E -> S -> W
	directions = [North, East, South, West]
	current_dir_index = 0  # Assuming we start facing North (index 0)
	
	goal_x, goal_y = measure()
	
	while get_pos_x() != goal_x or get_pos_y() != goal_y:
		# If, for some reason, the maze disappears (maybe a conflict with another drone)
		if get_entity_type() != Entities.Hedge:
			treasure(maze_size, start_x, start_y)
			return
			
		# Calculate which direction is to the RIGHT of the current facing
		# (Index + 1) % 4 gives us the next direction clockwise
		right_dir_index = (current_dir_index + 1) % 4
		right_dir = directions[right_dir_index]
		
		# Calculate which direction is FORWARD (Current facing)
		forward_dir = directions[current_dir_index]
		
		# Priority 1: Hug the wall (Turn Right)
		# If there is no wall to the right, turn there to follow the corner.
		if can_move(right_dir):
			current_dir_index = right_dir_index # Update facing
			move(right_dir)
		# Priority 2: Follow the wall (Go Straight)
		# If there is a wall to the right, try to continue forward.
		elif can_move(forward_dir):
			move(forward_dir)
			# Note: We do not change current_dir_index here
		# Priority 3: Hit a corner (Turn Left)
		# Wall on right AND wall in front. We must rotate to find a path.
		else:
			# (Index - 1) % 4 gives us the previous direction (Counter-Clockwise)
			current_dir_index = (current_dir_index - 1) % 4
			# We do NOT move in this step. We just rotate. 
			# The next iteration of the 'while' loop will check if we can move.
	harvest()