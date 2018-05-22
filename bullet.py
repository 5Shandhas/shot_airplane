import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""对子弹进行管理"""
	def __init__(self,sts,screen,Ship):
		# 在飞船的位置建立子弹
		super(Bullet,self).__init__()
		self.screen=screen

		# 先在（0,0）处创建一个子弹，再设置它的位置
		self.rect=pygame.Rect(0, 0, sts.bullet_width, sts.bullet_height)
		# 位置是船的中心和顶端
		self.rect.centerx=Ship.rect.centerx
		self.rect.top=Ship.rect.top
		# 储存用小数表示子弹的位置
		self.y=float(self.rect.y)
		self.color=sts.bullet_color
		self.speed_factor=sts.bullet_speed_factor
	def update(self):
		"""调整子弹"""
		# 更新表示位置的数值
		self.y-=self.speed_factor
		# 更新位置
		self.rect.y=self.y
	def draw_bullet(self):
		self.update()
		if self.rect.y>-10:
			pygame.draw.rect(self.screen,self.color,self.rect)
		else:
			self.rect.y=-20
			pygame.draw.rect(self.screen,self.color,self.rect)