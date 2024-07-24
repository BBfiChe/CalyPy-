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
from sys import path
path.append('/Games/CalcPy')
import CalcFun
