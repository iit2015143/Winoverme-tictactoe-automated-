"""The user will always input X with the help of
numbers in the sequence as follows:
7 8 9
4 5 6
1 2 3
    """
import sys
import pygame
pygame.init()

key1=257
key9=265
t_offset=30
screen_h=600
screen_w=600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
green_tl=(0,255,0,230)
b_width=4
h_color=(255, 153, 255)
s_color=(230, 153, 0)

def printmsg(msg,x,y,size,color):
	fontobj=pygame.font.Font('freesansbold.ttf',size)
	if msg=='X':
		textsurf=fontobj.render(msg,True,color)
	else:
		textsurf=fontobj.render(msg,True,color)
	textrect=textsurf.get_rect()
	textrect.center=(x,y)
	screen.blit(textsurf,textrect)

def pbrd(emsg,x,y):
	"""print(v[7]+'|'+v[8]+'|'+v[9])
	print('-+-+-')
	print(v[4]+'|'+v[5]+'|'+v[6])
	print('-+-+-')
	print(v[1]+'|'+v[2]+'|'+v[3])"""
	screen.fill(s_color)

#keep in mind 'i' is y coord and 'j' is x coord
#it took you 30 mins to find it out

	for i in range(1,4):
		for j in range(1,4):
			pygame.draw.rect(screen,black,[j*screen_w/5,i*screen_h/5,screen_w/5,screen_h/5],b_width)
			c=3*(3-i) + j
			if v[c]!=' ':
				if v[c]=='X':
					printmsg(v[c],j*120 + 60,i*120 +60,120,red)
				else:
					printmsg(v[c],j*120 + 60,i*120 +60,120,green)
	pygame.draw.rect(screen,s_color,[120,120,360,360],4)
	printmsg(emsg,x,y,t_offset-5,h_color)
	pygame.display.update()
	
def xenter():
	print('Mr. '+ pname+' please enter the number')
	p=input()
	try:
		p=int(p)
	except ValueError:
		p=55
	while p>9 or p<1 or v[p]!=' ':
		print('Mr. ' +pname+' your move was invalid enter again')
		p=input()
		try:
	    		p=int(p)
		except ValueError:
	    		p=55
	v[p]='X'
	#pbrd()
def defense():
    global c
    for i in [7,4,1]:
        if v[i]=='X' and v[i]==v[i+1] and v[i+2]==' ':
            v[i+2]='O'
            c=c+1
            return
        elif v[i+1]=='X' and v[i+2]==v[i+1] and v[i]==' ':
            v[i]='O'
            c=c+1
            return
        elif v[i+2]=='X' and v[i]==v[i+2] and v[i+1]==' ':
            v[i+1]='O'
            c=c+1
            return
    for i in [1,2,3]:
        if v[i]=='X' and v[i]==v[i+3] and v[i+6]==' ':
            v[i+6]='O'
            c=c+1
            return
        elif v[i+3]=='X' and v[i+6]==v[i+3] and v[i]==' ':
            v[i]='O'
            c=c+1
            return
        elif v[i+6]=='X' and v[i]==v[i+6] and v[i+3]==' ':
            v[i+3]='O'
            c=c+1
            return
    for i in [1]:
        if v[i]=='X' and v[i]==v[i+4] and v[i+8]==' ':
            v[i+8]='O'
            c=c+1
            return
        elif v[i+4]=='X' and v[i+8]==v[i+4] and v[i]==' ':
            v[i]='O'
            c=c+1
            return
        elif v[i+8]=='X' and v[i]==v[i+8] and v[i+4]==' ':
            v[i+4]='O'
            c=c+1
            return
    for i in [3]:
        if v[i]=='X' and v[i]==v[i+2] and v[i+4]==' ':
            v[i+4]='O'
            c=c+1
            return
        elif v[i+2]=='X' and v[i+4]==v[i+2] and v[i]==' ':
            v[i]='O'
            c=c+1
            return
        elif v[i+4]=='X' and v[i]==v[i+4] and v[i+2]==' ':
            v[i+2]='O'
            c=c+1
            return
def oenter():
    #print('See Mr.'+pname+' how fast Queen is')
    #winning strategy
    for i in [7,4,1]:
        if v[i]=='O' and v[i]==v[i+1] and v[i+2]==' ':
            v[i+2]='O'
            return
        elif v[i+1]=='O' and v[i+2]==v[i+1] and v[i]==' ':
            v[i]='O'
            return
        elif v[i+2]=='O' and v[i]==v[i+2] and v[i+1]==' ':
            v[i+1]='O'
            return
    for i in [1,2,3]:
        if v[i]=='O' and v[i]==v[i+3] and v[i+6]==' ':
            v[i+6]='O'
            return
        elif v[i+3]=='O' and v[i+6]==v[i+3] and v[i]==' ':
            v[i]='O'
            return
        elif v[i+6]=='O' and v[i]==v[i+6] and v[i+3]==' ':
            v[i+3]='O'
            return
    for i in [1]:
        if v[i]=='O' and v[i]==v[i+4] and v[i+8]==' ':
            v[i+8]='O'
            return
        elif v[i+4]=='O' and v[i+8]==v[i+4] and v[i]==' ':
            v[i]='O'
            return
        elif v[i+8]=='O' and v[i]==v[i+8] and v[i+4]==' ':
            v[i+4]='O'
            return
    for i in [3]:
        if v[i]=='O' and v[i]==v[i+2] and v[i+4]==' ':
            v[i+4]='O'
            return
        elif v[i+2]=='O' and v[i+4]==v[i+2] and v[i]==' ':
            v[i]='O'
            return
        elif v[i+4]=='O' and v[i]==v[i+4] and v[i+2]==' ':
            v[i+2]='O'
            return
    # it is a simple jugaad to return twice from fn defense().
    b=c
    defense()
    if c>b:
        return
    if j==3 and v[7]=='X' and v[7]==v[3]:
        v[2]='O'
        return
    if j==3 and v[1]=='X' and v[1]==v[9]:
        v[2]='O'
        return
    #to defend by tricks....
    if v[1]==' ':
        if (v[2]=='X' or v[3]=='X') and (v[4]=='X' or v[7]=='X'):
            v[1]='O'
            return
    if v[3]==' ':
        if (v[2]=='X' or v[1]=='X') and (v[6]=='X' or v[9]=='X'):
            v[3]='O'
            return
    if v[7]==' ':
        if (v[8]=='X' or v[9]=='X') and (v[1]=='X' or v[4]=='X'):
            v[7]='O'
            return
    if v[9]==' ':
        if (v[6]=='X' or v[3]=='X') and (v[7]=='X' or v[8]=='X'):
            v[9]='O'
            return
    #it is to attack...
    if j==1 and v[5]==' ':
        v[5]='O'
        return
    #attacking trick
    if v[1]==' ':
        if (v[2]=='O' or v[3]=='O') and (v[4]=='O' or v[7]=='O'):
            v[1]='O'
            return
    if v[3]==' ':
        if (v[2]=='O' or v[1]=='O') and (v[6]=='O' or v[9]=='O'):
            v[3]='O'
            return
    if v[7]==' ':
        if (v[8]=='O' or v[9]=='O') and (v[1]=='O' or v[4]=='O'):
            v[7]='O'
            return
    if v[9]==' ':
        if (v[6]=='O' or v[3]=='O') and (v[7]=='O' or v[8]=='O'):
            v[9]='O'
            return
    for i in [1,3,7,9]:
        if v[i]==' ':
            v[i]='O'
            return
    for i in [2,4,6,8]:
        if v[i]==' ':
            v[i]='O'
            return
def chk():
    global a
    if v[1]==v[2] and v[2]==v[3] and v[1]!=' ':
        a=1
    if v[4]==v[5] and v[5]==v[6] and v[4]!=' ':
        a=1
    if v[7]==v[8] and v[8]==v[9] and v[9]!=' ':
        a=1
    if v[7]==v[5] and v[5]==v[3] and v[5]!=' ':
        a=1
    if v[9]==v[5] and v[5]==v[1] and v[1]!=' ':
        a=1
    if v[1]==v[4] and v[4]==v[7] and v[7]!=' ':
        a=1
    if v[2]==v[5] and v[5]==v[8] and v[5]!=' ':
        a=1
    if v[3]==v[6] and v[6]==v[9] and v[6]!=' ':
        a=1

def setglobals():
	global j,c,a,v
	j=0
	v={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
	a=0
	c=1

def endhandler(msg):
	screen_t_b=screen.convert_alpha()
	screen_t_b.fill(green_tl)
	screen.blit(screen_t_b,(0,0))
	loadimg("small22.png",120)
	printmsg(msg,screen_w/2,screen_h/2,t_offset,red)
	printmsg('PRESS P TO PLAY AGAIN AND Q TO QUIT',screen_w/2,screen_h/2+50,t_offset-5,s_color)
	pygame.display.update()
	
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_p:
					setglobals()	
					pbrd(string,screen_w/2, t_offset-10)
					gameloop()
				if event.key==pygame.K_q:
					pygame.quit()
					quit()

def loadimg(name,y):
	img=pygame.image.load(name)
	imgrect=img.get_rect()
	imgrect.center=(screen_w/2, y)
	screen.blit(img,imgrect)

def gameloop():
	global j
	empty=True
	while empty:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				empty=False
			if event.type==pygame.KEYDOWN:
				#print(event)
				#print(event.key)
				if event.key>=key1 and event.key<=key9 and v[event.key- key1 + 1]==' ':
					v[event.key- key1 + 1]='X'
					j=j+1
					chk()
					'''if a==1:
            					print('Mr.'+pname +' wins...')
            					sys.exit()'''
					if j==9:
						msg='None of you could make it.... '
						endhandler(msg)
					
					pbrd('',0,0)
					loadimg("think.png",60)
					pygame.display.update()
					pygame.time.wait(1000)
					oenter()
					j=j+1
					pbrd('',0,0)
					chk()
					if a==1:
						msg='Queen wins... nxt time try harder'
						endhandler(msg)
						#sys.exit()
					
						#empty=False
				else:
					printmsg("OOOPS You made a wrong move",300,30,t_offset,red)
					pygame.display.update()


print('Please enter your name')
pname=input()
#print(pname+' Vs Queen')
#print('Here it begins.... all the very best')
v={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
a=0
global c
c=1

#the screen variable here can have flags such as resizable and noframe
screen= pygame.display.set_mode((screen_w,screen_h),pygame.RESIZABLE)
music=pygame.mixer.Sound("toogg2.ogg")
music.play(-1)
string="Hi "+ pname + " Here it begins, all the very best"
pbrd(string,screen_w/2, t_offset)
j=0
gameloop()
"""for j in range (9):
    if j%2==0:
        xenter()
        chk()
        if a==1:
            print('Mr.'+pname +' wins...')
            sys.exit()
    else:
        oenter()
        pbrd()
        chk()
        if a==1:
            print('Mrs. Queen wins... nxt time try harder Mr.'+ pname)
            sys.exit()"""
