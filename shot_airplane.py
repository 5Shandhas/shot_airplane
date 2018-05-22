# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:40:04 2017

@author: My Laptop
"""

# import sys  #简化后主程序文件没必要使用sys，因为次程序已经在用
import pygame
from settings import settings
from ship import ship
import game_functions as gf
from pygame.sprite import Group
import threading



def run_game():
	sts=settings()

	# 初始化游戏，创建屏幕对象
	pygame.init()
	# 占位大小
	screen =pygame.display.set_mode((sts.screen_width,sts.screen_height))
	pygame.display.set_caption('shot airplane!!')
	# 背景色的设置
	# bg_color = (230,230,230)
	# 放置飞船
	Ship=ship(screen)
	bullets=Group()
	aliens=Group()
	
	# 创建外星人群
	b=gf.create_fleet(sts,screen,aliens)
	# 开始游戏循环
	while 1:
		# 感知键盘鼠标操作
		# for event in pygame.event.get():
		# 	# 该处应该是‘关闭’操作
		# 	if event.type==pygame.QUIT:
		# 		sys.exit()
		# 上述代码替换为
		gf.check_events(sts,screen,Ship,bullets,aliens)
		Ship.update()

		# screen.fill(sts.bg_color)
		# Ship.blitme()
		# # 让绘制的屏幕大小可见
		# pygame.display.flip()
		# 删除子弹的代码

		# 上述代码替换为
		gf.update_screen(sts,screen,Ship,bullets,aliens,b)
		if bool(b)==False:
			b=gf.create_fleet(sts,screen,aliens)
		if len(aliens)==0:
			b=gf.create_fleet(sts, screen, aliens)
run_game()