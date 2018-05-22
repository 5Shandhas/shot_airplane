import pygame

class ship:
	def __init__(self,screen):
		# 初始化飞船党的位置
		self.screen=screen

		# 加载飞船图像并获取其外接矩形
		# 加载图像
		self.image=pygame.image.load('image/mine.bmp')
		# 把图像作为矩形处理
		self.rect=self.image.get_rect()
		# 屏幕矩形初始化
		self.screen_rect=screen.get_rect()
		# 将飞船放到底端
		# 定义rect属性中心
		self.rect.centerx=self.screen_rect.centerx
		# 定义rect的属性底部
		self.rect.bottom = self.screen_rect.bottom
		# 移动标识
		self.moving_r= False
		self.moving_l= False
		self.moving_u= False
		self.moving_d= False

		# 飞船的速度
		self.ship_speed=1.5
		self.center=float(self.rect.centerx)

	def update(self):
		"""根据移动标识调整飞船位置"""
		if self.moving_r and self.rect.right <self.screen_rect.right:
			self.rect.centerx+=self.ship_speed
		if self.moving_l and self.rect.left >self.screen_rect.left:
			self.rect.centerx-=self.ship_speed
		if self.moving_u and self.rect.top > self.screen_rect.top:
			self.rect.bottom-=self.ship_speed
			# print(self.rect.top,self.screen_rect.top,self.rect.bottom,self.screen_rect.bottom)
		if self.moving_d and self.rect.bottom < self.screen_rect.bottom:
			self.rect.bottom+=self.ship_speed


	def blitme(self):
		# 绘制飞船于指定位置
		self.screen.blit(self.image,self.rect)

