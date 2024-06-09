import math

from board_map import *
from hero import Hero
from game_task import Task

class Enemy(Hero):

	def __init__(self, x, y, player, name):
		super().__init__(x, y, name)
		self.speed = 1.5
		self.player = player
		self.get_enemy_img(name)
		if(self.name == 'warrior'):
			self.task = Task(3)

	def get_enemy_img(self, name):
		width, height = 16, 16
		enemy_img_pos = {"enemy_1": 0, "enemy_2": 1, "enemy_3": 2, "warrior": 3}
		img = pygame.image.load(os.path.join("assets", "objects", "Dungeon_Character_2.png"))
		image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
		image.blit(img, (0, 0), ((enemy_img_pos[name] * width), 0, width, height))
		image.set_colorkey()
		self.image = image

	def check_distance(self):
		dx = self.player.pose.x - self.rect.centerx
		dy = self.player.pose.y - self.rect.centery
		return math.sqrt(dx ** 2 + dy ** 2)

	def interaction(self):
		distance = self.check_distance()
		if distance < 50:
			match self.behavior:
				case "agressive":
					self.move("attac")
				case "passive":
					self.move("run")
		else:
			self.move(None)
