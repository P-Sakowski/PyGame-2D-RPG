import math
from collections import deque

from board_map import *


class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, name):
		pygame.sprite.Sprite.__init__(self)
		self.name = name
		# pola dotyczące obrazu
		self.image = pygame.Surface((20, 20))
		self.image.fill((0, 0, 180))
		self.rect = self.image.get_rect()
		# pola dotyczące pozycji i pozycji docelowej
		self.speed = 2.
		self.row = x
		self.cell = y
		self.pose = self.get_position(x, y)
		self.rect.center = self.pose
		self.dest_pos = self.get_position(x, y)
		# pola do poszukiwania drogi
		self.map_dest_pos = (self.row, self.cell)
		self.map_current_pos = (self.row, self.cell)
		self.path = []
		# pola dotyczące wyposarzenia i zachowania
		self.coin = 0
		self.active_task = []
		self.equipment = []
		self.behavior = None

	def update(self, offset) -> None:
		self.pose += self.move_to()
		if offset.x != 0 or offset.y != 0:
			self.pose += offset
			self.dest_pos += offset
		self.rect.center = self.pose

	def move_to(self):
		dx = self.dest_pos.x - self.rect.centerx
		dy = self.dest_pos.y - self.rect.centery
		distance = math.sqrt(dx ** 2 + dy ** 2)
		if distance != 0:
			dx /= distance
			dy /= distance
			speed = 2
			return Vector2(dx * speed, dy * speed)
		elif distance <= 0.1 and len(self.path) > 0:
			temp_pos = self.path.pop()
			self.map_current_pos = temp_pos
			print("kolejna pozycja {}".format(temp_pos))
			self.dest_pos = self.get_position(temp_pos[0], temp_pos[1])
		return Vector2(0, 0)

	def move(self, row, cell):
		# określenie pozycji pod względem kolumny i wiersza z mapy
		if board_map[row, cell] == 2:
			self.map_dest_pos = (row, cell)
			self.path = self.bfs_algorithm(self.map_current_pos, self.map_dest_pos)
			print(self.path)
			print("umieszczam naszego gracza ")
		else:
			print("niedozwolone miejsce")

	@staticmethod
	def get_position(row, cell):
		temp_pos = pygame.math.Vector2([0, 0])
		temp_pos.x = cell * TILE_SIZE[0] + int(TILE_SIZE[0] / 2)
		temp_pos.y = row * TILE_SIZE[1] + int(TILE_SIZE[1] / 2)
		temp_pos += global_offset
		return temp_pos

	@staticmethod
	def bfs_algorithm(start, end):
		map_size = board_map.shape
		direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		queue = deque([start])
		visited = set()
		visited.add(start)
		parent = {start: None}

		while queue:
			current = queue.popleft()

			if current == end:
				break
			for direct in direction:
				neighbor = (current[0] + direct[0], current[1] + direct[1])
				if (0 <= current[0] < map_size[0] and 0 <= current[1] < map_size[1]
							and board_map[current[0], current[1]] == 2 and neighbor not in visited):
					queue.append(neighbor)
					visited.add(neighbor)
					parent[neighbor] = current

		path = []
		step = end
		while step is not None:
			path.append(step)
			step = parent[step]
		return path
