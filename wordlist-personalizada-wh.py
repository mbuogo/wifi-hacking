#!/usr/bin/env python3

import sys
import string
import datetime
import re
from unicodedata import normalize

dic = {'aioO':'@100','aeioOs':'43100$','aeiou':'AEIOU','IilLsS':'1111$$'}
wordlist = open('wordlist.txt', 'w')
data = datetime.datetime.now()


def function_2 (word):
	for l in range(1001):
		wordlist.write(word+str(l)+'\n')
		wordlist.write(word+'@'+str(l)+'\n')

def function_1 (line):
	for i in dic:
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])))
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).upper())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).lower())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).capitalize())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).title())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'@'+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).swapcase())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+str(data.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'@'+str(data.year)+'\n')

def main():
	with open(sys.argv[1]) as file:
		for t in file:
			linha = t.rstrip('\n')
			function_1(linha)
	wordlist.close()

if __name__ == '__main__':
  main()
