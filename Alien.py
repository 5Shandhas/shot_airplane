import pygame
from pygame.sprite import Sprite
from random import randint
# import game_functions as gf
class Alien(Sprite):
	def __init__(self,sts,screen):
		super().__init__()
		self.screen=screen
		self.sts=sts
		self.screen_rect=screen.get_rect()
		# 加载外星人的图片设置其rect属性
		self.image=pygame.image.load('image/mines.bmp')
		self.rect=self.image.get_rect()

		# 每个外星人都在屏幕左上角
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		# 储存准确位置
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)

		# 速度
		self.speed=0.02
	def update(self,b):
		# print('上边：',b[k])
		if b[self]==0:
			self.move_ri()
			if self.rect.right <self.screen_rect.right:
				b[self]=0
			else:
				b[self]=1
		else:
			self.move_le()
			if self.rect.left>self.screen_rect.left:
				b[self]=1
			else:
				b[self]=0
		# print(b[k])
		# print('右边：',self.rect.right,self.screen_rect.right,'左边：',self.rect.left,self.screen_rect.left)
		
	def blitme(self,b):
		self.update(b)
		self.screen.blit(self.image,self.rect)

	def move_ri(self):
		self.y+=5*self.speed
		self.rect.y=self.y
		self.x+=randint(0,5)*self.speed*10
		self.rect.x=self.x
	def move_le(self):
		self.y+=5*self.speed
		self.rect.y=self.y
		self.x+=randint(-5,0)*self.speed*10
		self.rect.x=self.x