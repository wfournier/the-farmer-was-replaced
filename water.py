def fill():
	while not can_harvest() and num_items(Items.Water) > 0 and get_water() <= 0.75:
		use_item(Items.Water)