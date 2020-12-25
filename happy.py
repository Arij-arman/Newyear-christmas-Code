"""CREATED ON *DATE=25 DEC,2020 *TIME= 13.50 COUNTRY= India, BLOOD=Muslim"""
########################################
# DEVELOPER'S NAME:- ARIJ ARMAN MANDAL #
# CONTACT:-mrxanonymous633@gmail.com   #
# KEEP SUPORTING ME..... THANK YOU     #
########################################
import time
from random import randint
import os

# REMEMBER USE PYTHON 3 FOR THIS
for i in range(1,45):
	print('')
s = ''

for i in range(1,1000):
	count = randint(1,100)
	while (count > 0):
		s += ' '
		count -= 1
		
	if (i%10==0):
		print(s + 'Happy New Year')
	elif (i % 17==0):
		print(s + 'Merry Christmas')
	else :
		print(s + '*     ❤️     *   🎄️*     *🎅️') # IF ANY PROBLEM THEN ERASE THE EMOJIS
		
		
	s= ''
	
	time.sleep(0.3)
	
