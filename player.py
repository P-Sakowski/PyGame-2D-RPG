import os
import pygame

from hero import Hero


class Player(Hero):

	def __init__(self, x, y, name):
		super().__init__(x, y, name)
		self.get_player_img(name)

	def get_player_img(self, name):
		width, height = 16, 16
		enemy_img_pos = {"person_1": 0, "person_2": 1, "person_3": 2, "person_4": 3}
		img = pygame.image.load(os.path.join("assets", "objects", "Dungeon_Character_2.png"))
		image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
		image.blit(img, (0, 0), ((enemy_img_pos[name] * width), 0, width, height))
		image.set_colorkey()
		self.image = image
