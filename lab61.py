import random

a={1:'rock',2:'paper',3:'scissor'}

while True:
	p=input('enter your choice:')

	c=a[random.randint(1,3)]

	print("you chose:",p,"\ncomputer chose:",c)

	if(p==c):
		print('\t\t   **Draw!**  ')
	elif(p=='rock' and c=='paper'):
		print('\t\t ## you lose! ##')
	elif(p=='rock' and c=='scissor'):
		print('\t\t ## you win! ## ')
	elif(p=='paper' and c=='rock'):
		print('\t\t## you win! ##')
	elif(p=='paper' and c=='scissor'):
		print('\t\t ## you lose! ## ')
	elif(p=='scissor' and c=='rock'):
		print('\t\t ## you lose! ## ')
	elif(p=='scissor' and c=='paper'):
		print('\t\t ## you win! ## ')
	else:
		print('\n\t bored?')
		exit()						