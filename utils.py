# Returns if the plant has to be planted on soil
def grows_on_soil(type):
	return type in [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
	
# Returns if the plant can be harvested as soon as its grown (without condition)
def can_harvest_immediately(type):
	return type in [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]