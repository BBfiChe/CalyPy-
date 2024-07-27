
# FIX Add sprite replacements for new symbols
# FIX Add x calculation
# FIX factorial
# FIX make showhelp function

import thumby
from time import sleep

# Calculator icon
# BITMAP: width: 31, height: 38
bitmap0 = bytearray([254,255,255,7,7,7,199,71,71,71,71,71,71,71,71,71,71,71,71,7,231,231,225,253,253,253,225,239,239,15,254,
            255,255,255,0,0,0,231,228,228,228,228,4,4,228,228,228,228,228,4,4,228,228,224,231,231,7,0,0,254,254,255,
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
cursor_pos = 0
prevCursor_pos = 0
char = ''
desc = ''
exp = ''
result = ''
exclude = ['del', 'clr', 'right', 'left', 'log', 'toggle', '|', 'help']
sqrts = []
pis = []
selx = 0
sely = 0
frameCounter = 0
borw = 0
rOffset = 0
doOffset = 0
logsel = 0
thelog = ''
thumby.saveData.setName('CalcPy+')
if thumby.saveData.hasItem('layers'):
    hasmorelayers = thumby.saveData.getItem('layers')
else:
    thumby.saveData.setItem('layers', 1)
    hasmorelayers = 1

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
           255,68,40,16,40,68,0,0,4,8,240,8,4,0,0,0,16,32,60,4,0,0,68,32,16,8,68,0,0,
           255,0,16,40,68,0,0,0,0,0,68,40,16,0,0,0,40,40,40,40,0,0,68,84,120,0,124,20,8,
           1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
layer2 = thumby.Sprite(29, 33, bitmap2, 43, 7)

# Layer 3
# BITMAP: width: 29, height: 33
bitmap6 = bytearray([255,1,73,85,37,1,1,1,1,57,69,69,1,1,1,1,5,125,5,1,1,1,1,1,189,1,1,1,1,
           255,104,88,112,72,84,36,0,104,88,112,56,68,68,0,104,88,112,4,124,4,0,0,0,252,0,0,0,0,
           255,28,32,28,72,84,36,0,28,32,28,56,68,68,0,28,32,28,4,124,4,0,0,124,0,80,104,120,0,
           255,28,32,28,36,84,72,0,28,32,28,68,68,56,0,28,32,28,64,124,64,0,0,4,180,28,0,0,0,
           1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
layer3 = thumby.Sprite(29, 33, bitmap6, 43, 7)

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

# Cursor, but for the keyboard
# BITMAP: width: 8, height: 9
bitmap7 = bytearray([255,1,1,1,1,1,1,255,
           1,1,1,1,1,1,1,1])
cursorc = thumby.Sprite(8, 9, bitmap7, 0, 0, 0)

# Log selection
# BITMAP: width: 21, height: 13
bitmap10 = bytearray([0,254,2,242,82,82,2,2,2,146,82,98,2,2,242,2,226,18,226,254,0,
           0,15,8,9,9,9,8,12,8,9,9,9,8,12,9,8,9,9,9,15,0])
logselection = thumby.Sprite(21, 13, bitmap10, 52, 10)

# Log cursor
# BITMAP: width: 7, height: 9
bitmap11 = bytearray([255,1,1,1,1,1,255,
           1,1,1,1,1,1,1])
logcursor = thumby.Sprite(7, 9, bitmap11, 0, 12, 0)

# Pi
# BITMAP: width: 4, height: 5sd,
bitmap12 = bytearray([15,1,15,17])
pi = thumby.Sprite(4, 5, bitmap12, 0, 0)

# 3 page indicator
# BITMAP: width: 8, height: 9
bitmap13 = bytearray([0,68,84,120,0,124,20,8,
            0,0,0,0,0,0,0,0])
ispage = thumby.Sprite(8, 9, bitmap13, 64, 31)

# 2 page indicator
# BITMAP: width: 8, height: 9
bitmap14 = bytearray([0,100,84,88,0,124,20,8,
            0,0,0,0,0,0,0,0])
isntpage = thumby.Sprite(8, 9, bitmap14, 64, 31)

thumby.display.setFPS(120)

def chartable(x, y, l):
    if l == 0:
        if x == 0:
            if y == 0: c, d = '1', ''
            elif y == 1: c, d = '4', ''
            elif y == 2: c, d = '7', ''
            elif y == 3: c, d = '0', ''
        elif x == 1:
            if y == 0: c, d = '2', ''
            elif y == 1: c, d = '5', ''
            elif y == 2: c, d = '8', ''
            elif y == 3: c, d = 'del', 'DELETE'
        elif x == 2:
            if y == 0: c, d = '3', ''
            elif y == 1: c, d = '6', ''
            elif y == 2: c, d = '9', ''
            elif y == 3: c, d = 'clr', 'CLEAR'
        elif x == 3:
            if y == 0: c, d = '+', ''
            elif y == 1: c, d = '-', ''
            elif y == 2: c, d = '*', ''
            elif y == 3: c, d = '/', ''
    elif l == 1:
        if x == 0:
            if y == 0: c, d = 'left', 'LEFT'
            elif y == 1: c, d = '(', ''
            elif y == 2: c, d = 'x', ''
            elif y == 3: c, d = '<', 'LESS'
        elif x == 1:
            if y == 0: c, d = 'right', 'RIGHT'
            elif y == 1: c, d = ')', ''
            elif y == 2: c, d = 'y', ''
            elif y == 3: c, d = '>', 'MORE'
        elif x == 2:
            if y == 0: c, d = '^', 'POWER'
            elif y == 1: c, d = '.', 'POINT'
            elif y == 2: c, d = 'a', 'ROOT'
            elif y == 3: c, d = '=', ''
        elif x == 3:
            if y == 0: c, d = 'b', 'PI'
            elif y == 1: c, d = 'e', 'EULER\'S'
            elif y == 2: c, d = '%', ''
            elif y == 3: c, d = 'toggle', '3 PAGES' if hasmorelayers == 1 else '2 PAGES'
    elif l == 2:
        if x == 0:
            if y == 0: c, d = 'w', 'SIN'
            elif y == 1: c, d = 'd', 'ARC SIN'
            elif y == 2: c, d = ']', 'HB SIN'
            elif y == 3: c, d = 'l', 'HBIVSIN'
        elif x == 1:
            if y == 0: c, d = 'c', 'COS'
            elif y == 1: c, d = 'f', 'ARC COS'
            elif y == 2: c, d = 'j', 'HB COS'
            elif y == 3: c, d = '[', 'HBIVCOS'
        elif x == 2:
            if y == 0: c, d = 'z', 'TAN'
            elif y == 1: c, d = 'g', 'ARC TAN'
            elif y == 2: c, d = 'k', 'HB TAN'
            elif y == 3: c, d = 'n', 'HBIVTAN'
        elif x == 3:
            if y == 0: c, d = '!', ''
            elif y == 1: c, d = '|', 'ABSOLUT'
            elif y == 2: c, d = 'log', 'LOG'
            elif y == 3: c, d = 'help', 'HELP'
    return c, d

def solve(exp):
    exp = str(exp)
    if '^' in exp:
        exp = exp.replace('^', '**')
    if '%' in exp:
        exp = exp.replace('%', '/100*')
    if 'a' in exp:
        exp = exp.replace('a', 'math.sqrt')
    if '!' in exp:
        pass
    if 'n' in exp:
        exp = exp.replace('n', 'math.atanh')
    if 'l' in exp:
        exp = exp.replace('l', 'math.asinh')
    if 'g' in exp:
        exp = exp.replace('g', 'math.atan')
    if 'o' in exp:
        exp = exp.replace('o', 'math.log')
    if 'p' in exp:
        exp = exp.replace('p', 'math.log2')
    if 'b' in exp:
        exp = exp.replace('b', 'math.pi')
    if 'c' in exp:
        exp = exp.replace('c', 'math.cos')
    if 'f' in exp:
        exp = exp.replace('f', 'math.acos')
    if '|' in exp:
        if exp.count('|') == 1:
            return 'ERROR'
        else:
            absindex = exp.find('|')
            exp = exp[:absindex] + exp[absindex+1:]
            exp = exp[:absindex] + 'math.fabs(' + exp[absindex:]
            absindex = exp.find('|')
            exp = exp[:absindex] + exp[absindex+1:]
            exp = exp[:absindex] + ')' + exp[absindex:]
    if ']' in exp:
        exp = exp.replace(']', 'math.sinh')
    if '[' in exp:
        exp = exp.replace('[', 'math.acosh')
    if 'u' in exp:
        exp = exp.replace('u', 'math.acosh')
    if 'e' in exp:
        exp = exp.replace('e', 'math.e')
    if 'v' in exp:
        exp = exp.replace('v', 'math.log10')
    if 'w' in exp:
        exp = exp.replace('w', 'math.sin')
    if 'z' in exp:
        exp = exp.replace('z', 'math.tan')
    if 'd' in exp:
        exp = exp.replace('d', 'math.asin')
    if 'j' in exp:
        exp = exp.replace('j', 'math.cosh')
    if 'k' in exp:
        exp = exp.replace('k', 'math.tanh')
    return str(eval(exp))

def printex(message):
      if len(message) > 10:
          message = message[:10]+'\n'+message[10:]
          if len(message) > 21:
              message = message[:21]+'\n'+message[21:]
              if len(message) > 32:
                  message = message[:32]+'\n'+message[32:]
                  if len(message) > 43:
                      message = message[:43]+'\n'+message[43:]
                  
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

def whichlog():
    global logsel
    while(1):
        logcursor.x = logsel*6 + 53
        thumby.display.drawSprite(logselection)
        thumby.display.drawSprite(logcursor)
        thumby.display.update()
        if button.buttonL.justPressed():
           logsel = (logsel-1) % 3
        elif button.buttonR.justPressed():
            logsel = (logsel+1) % 3
        if button.buttonA.justPressed():
           if logsel == 0:
               return 'o'
           elif logsel == 1:
               return 'p'
           elif logsel == 2:
               return 'v'
        elif button.buttonB.justPressed():
            return ''

while(1):
    frameCounter += 1
    print(hasmorelayers)
    if len(result) > 10 and doOffset == 0:
        if rOffset > len(result)*4-40:
            doOffset = 1
        else:
            if frameCounter % 30 == 0:
                rOffset += 1
    elif len(result) <= 10:
        doOffset = 0
        rOffset = 0
    if doOffset == 1:
        if rOffset < -2:
            doOffset = 0
        else:
            if frameCounter % 30 == 0:
                rOffset -= 1
    
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
            
    if len(exp) > 50: exp = exp[:-1]
    cursor.x = 1 if cursor_pos == 0 else (cursor_pos%10)*4 if cursor_pos < 50 else 80
    cursor.y = ((cursor_pos // 10)*6)+6
    cursorb.x = cursor.x
    cursorb.y = cursor.y
    cursorc.x = selx*7+43
    cursorc.y = sely*8+7
    thumby.display.fill(0)
    thumby.display.drawLine(43, 0, 43, 6, 1)
    thumby.display.drawLine(0, 32, 42, 32, 1)
    thumby.display.drawSprite(cursor if borw == 0 else cursorb)
    printex(exp)
    if 'a' in exp:
       for s in sqrts:
            sqrt.x = s%10 * 4
            sqrt.y = (s//10)*6
            thumby.display.drawFilledRectangle(sqrt.x, sqrt.y, 4, 5, 0)
            thumby.display.drawSprite(sqrt)
    if 'b' in exp:
       for p in pis:
            pi.x = p%10 * 4
            pi.y = (p//10)*6
            thumby.display.drawFilledRectangle(pi.x, pi.y, 4, 5, 0)
            thumby.display.drawSprite(pi)
    if result == '<function>':
        thumby.display.drawText('USE (', 1, 34, 1)
    else:
        thumby.display.drawText(result, 1-rOffset, 34, 1)
    try:
        result = solve(exp)
    except:
        if len(exp) == 0:
            result = '='
        else:
            result = 'ERROR'
    if layer == 0:
        thumby.display.drawSprite(layer1)
    elif layer == 1:
        thumby.display.drawSprite(layer2)
        thumby.display.drawSprite(ispage if hasmorelayers == 1 else isntpage)
    elif layer == 2:
        thumby.display.drawSprite(layer3)
    thumby.display.drawText(desc, 45, 1, 1)
    thumby.display.drawSprite(cursorc)
    thumby.display.update()
    
    if cursor_pos < 0:
        cursor_pos = len(exp)
    elif cursor_pos > len(exp):
        cursor_pos = 0
    
    if button.buttonB.justPressed():
        if hasmorelayers == 1:
            layer = (layer+1) % 3
        else: layer = (layer+1) % 2
        
    if button.buttonL.justPressed():
        selx = (selx-1)%4
    elif button.buttonR.justPressed():
        selx = (selx+1)%4
        
    if button.buttonU.justPressed():
        sely = (sely-1)%4
    elif button.buttonD.justPressed():
        sely = (sely+1)%4
    
    char, desc = chartable(selx, sely, layer)
    
    if button.buttonA.justPressed():
        borw = 0
        frameCounter = -60
        if char in exclude:
            if char == 'del':
                if cursor_pos != 0:
                    exp = exp[:cursor_pos-1] + exp[cursor_pos:]
                if len(exp) > 0 and cursor_pos != 0: cursor_pos -= 1
            elif char == 'clr':
                if prevExp == '':
                    prevExp = exp
                    prevCursor_pos = cursor_pos
                    exp = ''
                    cursor_pos = 0
                elif prevExp != '':
                    if exp == '':
                        exp = prevExp
                        cursor_pos = prevCursor_pos
                        prevExp = ''
                        prevCursor_pos = 0
                    else:
                        prevExp = exp
                        prevCursor_pos = cursor_pos
                        exp = ''
                        cursor_pos = 0
            elif char == 'log':
                logsel = 0
                exp = exp[:cursor_pos] + whichlog() + exp[cursor_pos:]
                cursor_pos += 1
            elif char == 'toggle':
                hasmorelayers = 1 if hasmorelayers == 0 else 0
                thumby.saveData.setItem('layers', hasmorelayers)
                thumby.saveData.save()
            elif char == 'left': cursor_pos -= 1
            elif char == 'right': cursor_pos += 1
            elif char == '|':
                if exp.count('|') < 2:
                    exp = exp[:cursor_pos] + char + exp[cursor_pos:]
                    cursor_pos += 1
            elif char == 'help':
                showhelp()
        else:
            exp = exp[:cursor_pos] + char + exp[cursor_pos:]
            cursor_pos += 1
