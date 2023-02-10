class RectSector:

	def __init__(self, latitude: int, longitude: int, width: int, length: int):
		self.latitude = latitude
		self.longitude = longitude
		self.width = width
		self.length = length

	def get_sector_area(self):
		return self.width * self.length


