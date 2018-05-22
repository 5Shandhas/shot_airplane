# 重构模块game_functions
import sys
import pygame
from bullet import Bullet
from Alien import Alien
from random import randint
# 响应屏幕和鼠标的动向
def check_events(sts,screen,Ship,bullets,aliens):
	"""响应屏幕和鼠标的动向"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		# 如果不退出移动飞船
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				Ship.moving_r=True
			elif event.key==pygame.K_LEFT:
				Ship.moving_l=True
			elif event.key==pygame.K_UP:
				Ship.moving_u=True
			elif event.key==pygame.K_DOWN:
				Ship.moving_d=True
			elif event.key==pygame.K_q:
				sys.exit()
			elif event.key==pygame.K_SPACE:
				# 创建一颗子弹
				new_bullet=Bullet(sts,screen,Ship)
				bullets.add(new_bullet)

		elif event.type==pygame.KEYUP:
			Ship.moving_r= False
			Ship.moving_l= False
			Ship.moving_u= False
			Ship.moving_d= False
def create_fleet(sts,screen,aliens):
	# 创建外星人
	n=randint(8, 12)
	fang={}
	# 方向
	s=sts.screen_width/n
	for num in range(n-1):
		alien=Alien(sts, screen)
		a=randint(0, 1)
		fang[alien]=a
		alien.x=(num+1)*s
		alien.rect.x=int(alien.x)
		aliens.add(alien)
	return fang


# 在屏幕上绘制图形
def update_screen(sts,screen,Ship,bullets,aliens,b):
	screen.fill(sts.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	# for bullet in bullets:
		if bullet.rect.y<0:
			bullets.remove(bullet)
	Ship.blitme()
	collosion(aliens, bullets)
	if bool(b)==False:
		pass
	else:	
		for alien in aliens:
			alien.blitme(b)
			if alien.rect.y>700:
				aliens.empty()
				del b[alien]
	# 让绘制的屏幕大小可见
	pygame.display.flip()

def collosion(aliens,bullets):
	collosions=pygame.sprite.groupcollide(bullets,aliens,True,True)
