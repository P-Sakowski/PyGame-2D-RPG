from board_map import *


class SpriteAnimation:

	def __init__(self, image, row, cell, step, width, height) -> None:
		self.sheet = image
		self.rect = pygame.math.Vector2(self.get_position(row, cell))
		self.list_frame = []
		for x in range(step):
			self.list_frame.append(self.cut_image(x, width, height))
		self.frame = 0

	def cut_image(self, x, width, height):
		image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
		image.blit(self.sheet, (0, 0), ((x * width), 0, width, height))
		image.set_colorkey()
		return image

	@staticmethod
	def get_position(row, cell):
		temp_pos = pygame.math.Vector2([0, 0])
		temp_pos.x = cell * TILE_SIZE[0] + int(TILE_SIZE[0] / 2)
		temp_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1] / 2)
		return temp_pos

	def update(self, offset) -> None:
		self.rect.x += offset.x
		self.rect.y += offset.y

	def draw(self, win):
		win.blit(self.list_frame[self.frame], self.rect)
