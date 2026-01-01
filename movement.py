import utils
import water
import farm

# Returns the opposite direction
def dir_invert(dir):
	inverts = {
		North: South,
		South: North,
		East: West,
		West: East
	}
	
	return inverts[dir]

# Moves the drone to some coordinates (vertically, then horizontally)
def move_to(x, y):
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	
	while cur_x != x or cur_y != y:		
		dir = None
		move_x = 0
		move_y = 0
		
		if cur_y < y:
			dir = North
			move_y = 1
		elif cur_y > y:
			dir = South
			move_y = -1
		elif cur_x < x:
			dir = East
			move_x = 1
		elif cur_x > x:
			dir = West
			move_x = -1
			
		move(dir)
		cur_x += move_x
		cur_y += move_y

# Moves the drone by a fixed distance in a direction
def move_by(dist, dir):
	for _ in range(dist):
		move(dir)