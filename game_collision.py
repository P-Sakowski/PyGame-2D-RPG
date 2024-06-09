import pygame
from game_task import Task
from item import Item


class GameCollision:

	def __init__(self) -> None:
		pass

	@staticmethod
	def enemy_collision(player, enemies):
		collision = pygame.sprite.spritecollide(player, enemies, False)
		if len(collision) > 0:
			enemy = collision[0]
			if enemy.name == "enemy_1":
				print("wykonuję przejście gracza")
				if len(enemy.path) == 0:
					enemy.move(15, 16)
			if enemy.name == "warrior":
				if Task(collision[0].task.task_nr).check_task(player):
					print("Dziękuję za ratunek bracie")
					player.equipment.append(Item(0, 0, "coin", 40))
					collision[0].kill()
				else:
					player.active_task.append(collision[0].task)
					print("Nowe zadanie:")
					print("Nazwa: {}".format(collision[0].task.name))
					print("Opis: {}".format(collision[0].task.description))
					print("Cel: {}".format(collision[0].task.requred_object))

	def item_collision(self, player, items):
		collision = pygame.sprite.spritecollide(player, items, False)
		if len(collision) > 0:
			if collision[0].type == "coin":
				player.coin += collision[0].coin_value
				print("Zebrano {} monet".format(collision[0].coin_value))
				collision[0].kill()
			elif collision[0].type == "task":
				player.active_task.append(collision[0].task)
				print("Nowe zadanie:")
				print("Nazwa: {}".format(collision[0].task.name))
				print("Opis: {}".format(collision[0].task.description))
				print("Cel: {}".format(collision[0].task.requred_object))
				collision[0].kill()
			elif collision[0].type == "key":
				print("Zebrano klucz ")
				player.equipment.append(collision[0])
				collision[0].kill()
			elif collision[0].type == "apple":
				print("Zebrano jabłko")
				player.equipment.append(collision[0])
				collision[0].kill()
			elif collision[0].type == "potion":
				print("Zebrano miksturę leczniczą")
				player.equipment.append(collision[0])
				for item in player.equipment:
					print(item.name)
				collision[0].kill()
			elif collision[0].type == "box":
				if collision[0].task is not None:
					print("Skrzynia zawiera zadanie")
					if Task(collision[0].task.task_nr).check_task(player):
						print("Skrzynia zostałą otwarta")
						self._get_item_from_box(player, collision[0])
						collision[0].kill()
					else:
						print("nie można otworzyć skrzyni")
				else:
					print("Skrzynia zostałą otwarta")
					self._get_item_from_box(player, collision[0])
					collision[0].kill()

	@staticmethod
	def _get_item_from_box(player, box):
		player.coin += box.coin_value
		print("W skrzyni było {} monet".format(box.coin_value))
		print("W skrzyni jest więcej obiektów:")
		for item in box.equipment:
			player.equipment.append(item)
			print(item.type)
