#
#  ___  ____  ____  
#(  _ \(  _ \(  _ \
# )___/ )   / )(_) )
#(__)  (_)\_)(____/
#
# Created by PR&DTeam. 
# Sorry, we don't know English =) (we tried hard)
# Beta version 0.1
#
# -*- coding: utf-8 -*-
#
#  lisp.py
#  
#  Copyright 2023 PR&DTeam 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

# Add modules
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

width = 128
height = 64

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled = SSD1306_I2C(width, height, i2c)
oled.fill(0)

oled.text('Welcome toyLisp!',0,32)
oled.show()
utime.sleep(3)

oled.fill(0)
oled.show()

buffer = bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x91\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xa9\x91\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x91kZ\xd6\xb5\xadkZ\xd6\xb5\xadkZ\xd6\xb5\x11\xab!\x08B\x10\x84!\x08B\x10\x84!\x08B\x11\xa9\x90\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x11\x83\x90B\x10\x84!\x08B\x10\x84!\x08B\x10\x8a\x81\x92\x9a\xd6\xb5\xadkZ\xd6\xb5\xadkZ\xd6\xb5\xae\x11\xa8\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xa9\x92\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xeb\x91\x80\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x01\x93\xab\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xaa\x91\xaa\x8b\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xae)\x90\xeb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xa2\x91\x82\xab?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf9\xab\x81\x90\x8b \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xa2\x11\xab\xab \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xaa\xa9\x92\x8b(\x07\xff\xf8\x01\xff\xf8\x01\xff\xf8\x00)\xae\x11\x80\xeb(\x07\xff\xfc\x01\xff\xfc\x01\xff\xfc\x00)\xa2\x81\x92\xab(\x07\xff\xfe\x01\xff\xfe\x01\xff\xfe\x00)\xab\x91\xa8\x8b(\x07\x00\x07\x01\xc0\x07\x01\xc0\x07\x00)\xa2)\x93\xab(\x07@\x03\x81\xd0\x03\x81\xd0\x03\x80)\xaa\x91\x82\x8b(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xae\x01\x90\xeb(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xa2\x91\xaa\xab(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xab\xa9\x90\x8b(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xa2\x11\x83\xab(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xaa\x81\x92\x8b(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xae\x11\xa8\xeb(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xa2\xa9\x92\xab(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xab\x91\x80\x8b(\x07@\x01\xc1\xd0\x03\x81\xd0\x03\x80)\xa2\x01\x93\xab(\x07@\x01\xc1\xc0\x07\x81\xc0\x07\x80)\xaa\x91\xaa\x8b(\x07@\x01\xc1\xff\xff\x01\xff\xff\x00)\xae)\x90\xeb(\x07@\x01\xc1\xff\xfe\x01\xff\xfe\x00)\xa2\x91\x82\xab(\x07@\x01\xc1\xff\xfc\x01\xff\xfc\x00)\xab\x81\x90\x8b(\x07@\x01\xc1\xc0\x00\x01\xc0x\x00)\xa2\x11\xab\xab(\x07@\x01\xc1\xc0\x00\x01\xc0<\x00)\xaa\xa9\x92\x8b(\x07@\x01\xc1\xc0\x00\x01\xc0\x1e\x00)\xae\x11\x80\xeb(\x07@\x01\xc1\xc0\x00\x01\xc0\x0f\x00)\xa2\x81\x92\xab(\x07@\x03\x81\xc0\x00\x01\xc0\x07\x80)\xab\x91\xa8\x8b(\x07\x00\x07\x01\xc0\x00\x01\xc0\x03\x80)\xa2)\x93\xab(\x07\xff\xfe\x01\xc0\x00\x01\xc0\x03\x80)\xaa\x91\x82\x8b(\x07\xff\xfc\x01\xc0\x00\x01\xc0\x03\x80)\xae\x01\x90\xeb(\x07\xff\xf8\x01\xc0\x00\x01\xc0\x03\x80)\xa2\x91\xaa\xab \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xab\xa9\x90\x8b \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\xa2\x11\x83\xab?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf9\xaa\x81\x92\x8b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xae\x11\xa8\xeb\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa2\xa9\x92\xab\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xab\x91\x80\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x01\x93\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xea\x91\xaa\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0e)\x90\xebZ\xd6\xb5\xadkZ\xd6\xb5\xadkZ\xd6\xb2\x91\x82\xa2\x10\x84!\x08B\x10\x84!\x08B\x10\x84\x13\x81\x90\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x11\xab\x10\x84!\x08B\x10\x84!\x08B\x10\x84!\t\xa9\x91Z\xd6\xb5\xadkZ\xd6\xb5\xadkZ\xd6\xb5\xad\x11\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x91\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xaa\xa9\x91\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11')

fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
oled.blit(fb,0,0)
oled.show()
utime.sleep(3)

oled.fill(0)
oled.show()
# Enviroment variables.
ENV = dict()

#Lexer. Breaks string into token.
def lexer(s):
    res = []
    str_buff = ''
    for i in s:
        if i == '(':
            res.append(i)
        else:
            if i == ')':
                if str_buff == '':
                    res.append(i)
                else:
                    res.append(str_buff)
                    str_buff = ''
                    res.append(i)
            else:
                if (i != ' ') and (i != '\n'):
                    str_buff += i
                else:
                    if str_buff != '':
                        res.append(str_buff)
                        str_buff = ''
    return res

# Parser. Turns tokens into a tree-like structure.
def parser(tokens):
    tkn = tokens.pop(0)
    if tkn == '(':
        ret = []
        while len(tokens):
            if (tokens[0] == ')'):
                tokens.pop(0)
                return ret
            else:
                ret.append(parser(tokens))
    else:
        try:
            return float(tkn)
        except:
            return tkn

# Gate function.
def gates(obj, env):
    val = env.get(obj)
    if val == None:
        if isinstance(obj, float):
            return obj
        elif isinstance(obj, bool):
            return obj
        else:
            oled.fill(0)
            oled.text('E> Unexpected value!',0,0)
            oled.show()
    else:
        return val

# Eval function.
def eval(obj, env):
    if isinstance(obj, list):
        if obj[0] == '+':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)+eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '*':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)*eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '^':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)**eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '-':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)-eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '/':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                if eval(obj[2],env) != 0:
                    return eval(obj[1],env)/eval(obj[2],env)
                else:
                    oled.fill(0)
                    oled.text('E>Zero division!',0,0)
                    oled.show()
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '$':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)//eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == '%':
            if isinstance(eval(obj[1],env), float) and isinstance(eval(obj[2],env), float):
                return eval(obj[1],env)%eval(obj[2],env)
            else:
                oled.fill(0)
                oled.text('E>Typecast!',0,0)
                oled.show()
        elif obj[0] == 't':
            return True
        elif obj[0] == 'nil':
            return False
        elif obj[0] == 'progn':
            res = eval(['nil'], env)
            for i in range(1, len(obj)):
                res = eval(obj[i], env)
            return res      
        elif obj[0] == 'def':
            name = obj[1]
            par = eval(obj[2],env)
            env.update([[name,par]])
            return par
        elif obj[0] == 'quote':
            try:
                return obj[1]
            except:
                return eval(['nil'], env)
        elif obj[0] == 'if':
            if eval(obj[1], env):
                return eval(obj[2], env)
            else:
                return eval(['nil'], env)
        elif obj[0] == 'lambda':
            try:
                local_env = dict()
                j = 1
                for i in obj[1]:
                    if j < len(obj[1])+1:
                        local_env.update([[i, eval(obj[j+2], local_env)]])
                        j+=1  
                return eval(obj[2], local_env)
            except:
                oled.fill(0)
                oled.text('E>Lambda args!',0,0)
                oled.show()
    else:
        return gates(obj, env)

while True:
    oled.fill(0)
    oled.text('tL>',0,0)
    oled.show()
    utime.sleep(0.45)
    oled.fill(0)
    oled.text('tL>|',0,0)
    oled.show()
    utime.sleep(0.45)
    