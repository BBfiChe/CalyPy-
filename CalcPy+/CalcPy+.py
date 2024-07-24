
# FIX Add sprite replacements for new symbols

import thumby
from time import sleep

# Calculator icon
# BITMAP: width: 31, height: 38
bitmap0 = bytearray([254,255,255,7,7,7,199,71,71,71,71,71,71,71,71,71,71,71,71,71,7,103,103,97,253,253,97,111,111,15,254,
           255,255,255,0,0,0,231,228,228,228,228,4,4,228,228,228,228,228,4,4,228,228,228,224,227,3,0,0,255,255,255,
           255,255,255,0,0,0,243,243,243,243,243,0,0,243,243,243,243,243,0,0,243,243,243,243,243,0,0,0,255,255,255,
           255,255,255,0,0,0,249,249,249,249,249,0,0,249,249,249,249,249,0,0,249,249,249,249,249,0,0,0,255,255,255,
           31,63,63,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,63,63,31])
           
splash = thumby.Sprite(31, 38, bitmap0, 1, 1)

thumby.display.drawSprite(splash)
thumby.display.setFont('/lib/font8x8.bin', 8, 8, -1)
thumby.display.drawText('Ca', 32, 5, 1)
thumby.display.drawText('l', 45, 5, 1)
thumby.display.drawText('cPy', 51, 5, 1)
thumby.display.update()
sleep(1.3)
thumby.display.setFont('/lib/font5x7.bin', 5, 7, 1)
thumby.display.drawText('by', 46, 14, 1)
thumby.display.setFont('/lib/font3x5.bin', 3, 5, 1)
thumby.display.drawText('UnRedKnown', 33, 23, 1)
thumby.display.drawText('BBf', 41, 30, 1)
thumby.display.drawText('i', 51, 30, 1)
thumby.display.drawText('Che', 54, 30, 1)
thumby.display.update()
thumby.display.fill(0)
sleep(1)

import math
import thumbyButton as button

prevExp = ''
layer = 0
cursor_pos = 1
prevCursor_pos = 0
char = ''
exp = ''
result = ''
exclude = ['del', 'clr', 'right', 'left', 'menu']
sqrts = []
pis = []
donewline = 0
selx = 0
sely = 0
frameCounter = 0
borw = 0
rOffset = 0
doOffset = 0

# Layer 1
# BITMAP: width: 29, height: 33
bitmap1 = bytearray([255,1,1,9,125,1,1,1,1,73,101,85,73,1,1,1,85,85,85,41,1,1,17,17,125,17,17,1,1,
           255,0,12,16,16,124,0,0,0,76,84,84,52,0,0,0,56,84,84,48,0,0,16,16,16,16,16,0,0,
           255,0,4,116,12,0,0,0,0,40,84,84,40,0,0,0,8,84,84,56,0,0,0,40,16,40,0,0,0,
           255,0,56,68,68,56,0,0,16,40,84,16,16,0,0,0,56,68,68,0,0,0,16,16,84,16,16,0,0,
           1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
layer1 = thumby.Sprite(29, 33, bitmap1, 43, 7)

# Layer 2
# BITMAP: width: 29, height: 33
bitmap2 = bytearray([255,1,17,41,69,1,1,1,1,1,69,41,17,1,1,17,9,5,9,17,1,1,3,63,3,3,63,67,1,
           255,0,0,56,68,0,0,0,0,0,68,56,0,0,0,0,0,24,24,0,0,0,0,56,84,84,24,0,0,
           255,124,0,8,84,84,56,0,0,16,32,60,4,0,0,68,32,16,8,68,0,0,4,8,240,8,4,0,0,
           255,0,16,40,68,0,0,0,0,0,68,40,16,0,0,0,40,40,40,40,0,0,68,40,16,40,68,0,0,
           1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
layer2 = thumby.Sprite(29, 33, bitmap2, 43, 7)

# Layer 3



# Square root
# BITMAP: width: 3, height: 5
bitmap3 = bytearray([4,15,1])
sqrt = thumby.Sprite(3, 5, bitmap3, 0, 0)

# Cursor, just a line
# BITMAP: width: 4, height: 1
bitmap4 = bytearray([1,1,1,1])
cursor = thumby.Sprite(4, 1, bitmap4, 0, 0)

# Cursor, just a line but black
# BITMAP: width: 4, height: 1
bitmap5 = bytearray([0,0,0,0])
cursorb = thumby.Sprite(4, 1, bitmap5, 0, 0)

def printex(message):
      if len(message) > 12:
          message = message[:12]+'\n'+message[12:]
          if len(message) > 25:
              message = message[:25]+'\n'+message[25:]
              if len(message) > 38:
                  message = message[:38]+'\n'+message[38:]
                  if len(message) > 51:
                      message = message[:51]+'\n'+message[51:]
                  
      message = str(message)
      txt = [""]
      for line in message.split("\n"):
          for word in line.split(" "):
              next_len = len(txt[-1]) + len(word) + 1
              if next_len*thumby.display.textWidth + (next_len-1) > thumby.display.width:
                  txt += [""]
              txt[-1] += (" " if txt[-1] else "") + word
          txt += [""]
      for ln, line in enumerate(txt):
          thumby.display.drawText(line, 0, (thumby.display.textHeight+1)*ln, 1)

while(1):
    frameCounter += 1
    
    if doOffset == 1:
        if frameCounter % 10 == 0:
            rOffset += 1
        
    if doOffset == 3:
        if rOffset > -4:
            if frameCounter % 10 == 0:
                rOffset -= 1
        else:
            doOffset = 4
    
    if doOffset == 2:
        if frameCounter % 100 == 0:
            doOffset = 3
    
    if doOffset == 4:
        if frameCounter % 100 == 0:
            doOffset = 0
    
    if len(str(result)) > 12:
        if rOffset < (len(str(result))*4) - 44:
            if doOffset == 0:
                doOffset = 1
        else:
            rOffset -= 1
            doOffset = 2
    else:
        doOffset = 0
    
    if doOffset == 3 and rOffset == -4:
        doOffset == 0
    
    if frameCounter % 60 == 0:
        borw = (borw+1) % 2
        
    if 'a' in exp:
        sqrts = [i for i, c in enumerate(exp) if c == 'a']
        
    for s in sqrts:
        try:
            if exp[s] != 'a':
                sqrts.pop(sqrts.index(s))
        except:
            sqrts.pop(sqrts.index(s))
            
    if 'b' in exp:
        pis = [i for i, c in enumerate(exp) if c == 'b']
    
    for p in pis:
        try:
            if exp[p] != 'b':
                pis.pop(pis.index(p))
        except:
            pis.pop(pis.index(p))
            
    if len(exp) > 60: exp = exp[:-1]
    cursor.x = 1 if cursor_pos == 0 else (cursor_pos%12)*4 if cursor_pos < 60 else 80
    cursor.y = ((cursor_pos // 12)*6)+6
    cursorb.x = cursor.x
    cursorb.y = cursor.y
    thumby.display.fill(0)
    thumby.display.drawLine(50, 0, 50, 6, 1)
    thumby.display.drawLine(50, 7, 72, 7, 1)
    thumby.display.drawLine(0, 32, 49, 32, 1)
    printex(exp)
    result = str(result)
    thumby.display.update()
