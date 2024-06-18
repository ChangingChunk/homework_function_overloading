class Buildings:
  def __init__(self, numberOfFloors, buildingType):
    self.numberOfFloors = numberOfFloors
    self.buildingType = buildingType

  def __eq__(self, other):
    return self.numberOfFloors == other.numberOfFloors and \
    self.buildingType == other.buildingType


house = Buildings(2, "House")
house2 = Buildings(2, "House")
store = Buildings(1, "Store")

print(house == store)
print(house == house2)