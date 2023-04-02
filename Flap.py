
import pygame
from random import randint

#Create screen
NGANGSCR=400
DAISCR=600
pygame.init()
screen = pygame.display.set_mode((NGANGSCR, DAISCR))
pygame.display.set_caption('GAME CUC HAY')
running = True

#Color
GREEN = (0, 200, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
BLUE1=(0,255,)
RED = (255,0,0)
YELLOW=(255,255,0)
GRAY=(128,128,128)

clock = pygame.time.Clock()

#coordinates bird
CHIMX = 50
chimy = 400
NGANGCHIM = 30
CAOCHIM = 30
tocdobandau = 0
TOCDOCONGDON =0.5

#coordinates tube
NGANG=50
TOCDO=3
KCONGMOI=550
KC2ONG=150

#coordinates x
ong1_x=600
ong2_x=800
ong3_x=1000

#tube hight
ong1_cao=randint(100,300)
ong2_cao=randint(100,300)
ong3_cao=randint(100,300)

#paint screen
diem = 0
font=pygame.font.SysFont('sans',30)

diquaong1=False
diquaong2=False
diquaong3=False

#load images
backgr = pygame.image.load("hinhnen.png")
chim= pygame.image.load("bird2.png")
mauong=pygame.image.load("ong.png")
mauong1=pygame.image.load("ong1.png")

checkpause=False

#main while
while running:		
	clock.tick(60)
	screen.fill(GREEN)

    #put the picture on the screen
	screen.blit(backgr,(0,0))
	

	#paint sand
	baicat_rect=pygame.draw.rect(screen,GRAY,(0,550,400,50))

	
	#paint bird 
	bird_rect=screen.blit(chim,(CHIMX,chimy))

    #falling bird
	chimy+=tocdobandau

	#speed 
	tocdobandau+=TOCDOCONGDON

	#paint tube 

    #upper tube
	ong1_rect=pygame.draw.rect(screen,BLUE,(ong1_x,0, NGANG, ong1_cao))
	ong2_rect=pygame.draw.rect(screen,BLUE,(ong2_x,0, NGANG, ong2_cao))
	ong3_rect=pygame.draw.rect(screen,BLUE,(ong3_x,0, NGANG, ong3_cao))

	#lower tube 
	ong4_rect=pygame.draw.rect(screen,BLUE,(ong1_x, ong1_cao+KC2ONG, NGANG, DAISCR-ong1_cao-KC2ONG))
	ong5_rect=pygame.draw.rect(screen,BLUE,(ong2_x, ong2_cao+KC2ONG, NGANG, DAISCR-ong2_cao-KC2ONG))
	ong6_rect=pygame.draw.rect(screen,BLUE,(ong3_x, ong3_cao+KC2ONG, NGANG, DAISCR-ong3_cao-KC2ONG))



	#tube moves to the left
	ong1_x-=TOCDO
	ong2_x-=TOCDO
	ong3_x-=TOCDO

	#tao ra ong moi khi ong cham vao mep trai
	#khi tao ong moi phai random lai chieu cao neu khong no se lap lai y chang
	if ong1_x <-NGANG:
		ong1_x=KCONGMOI
		ong1_cao=randint(100,300)
		diquaong1=False
	if ong2_x <-NGANG:
		ong2_x=KCONGMOI
		ong2_cao=randint(100,300)
		diquaong2=False
	if ong3_x <-NGANG:
		ong3_x=KCONGMOI
		ong3_cao=randint(100,300)
		diquaong3=False


	diem_txt = font.render("Point: "+str(diem), True, BLACK)
	screen.blit(diem_txt,(5,5))
	#cong diem
	#chi tinh diem 1 lan duy nhat
	if ong1_x+NGANG<=CHIMX and diquaong1==False:
		diem+=1
		diquaong1=True
	if ong2_x+NGANG<=CHIMX and diquaong2==False:
		diem+=1
		diquaong2=True
	if ong3_x+NGANG<=CHIMX and diquaong3==False:
		diem+=1
		diquaong3=True

	#check cham vao nhau
	for ong in [ong1_rect,ong2_rect,ong3_rect,ong4_rect,ong5_rect,ong6_rect,baicat_rect]:
		if bird_rect.colliderect(ong):
			checkpause=True
			TOCDO=0
			tocdobandau=0
			gameover_txt = font.render("Loser , Point:  "+str(diem), True, BLACK)
			screen.blit(gameover_txt,(80,200))
			ga_txt = font.render("Ban choi ga qua! ", True, BLACK)
			screen.blit(ga_txt,(80,250))
			choilai_txt = font.render("Bam Space de choi tiep", True, BLACK)
			screen.blit(choilai_txt,(80,300))




	#vong lap ben trong (nut bam)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=false
		if event.type == pygame.KEYDOWN:
			if event.key ==pygame.K_SPACE:
				#reset choi lai
				if checkpause:
					chimy=400
					TOCDO=3
					ong1_x=600
					ong2_x=800
					ong3_x=1000
					diem=0
					checkpause=False


				tocdobandau = 0
				tocdobandau = -8





	pygame.display.flip()

pygame.quit()