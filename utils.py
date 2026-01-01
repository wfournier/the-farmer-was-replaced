def grows_on_soil(type):
	return type in [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower]
	
def can_harvest_immediately(type):
	return type in [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]