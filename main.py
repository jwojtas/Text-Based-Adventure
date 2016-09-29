#Text based advednture- BY: John Wojtas
import random
import time
roomcount= 0
class Room:
	ranroom = 0
	def __init__(self, name):
		self.name = name

	def randroom():
		Room.ranroom = random.randint(1,4)
		
	def displaytype(self):
		if name == "empty":
			print ("It's an empty room")
		elif name == "chest":
			print("There's a chest in here")
		elif name == "enemy":
			print("There's an enemy in here")
		elif name == "heal":
			print("you get a heal (doesn't really exist yet)")
		elif name == "exit":
			print("Time to go")
		else:
			print("invalid")
	
roomnames = ["Empty", "Chest", "Heal", "Enemy"]

print ("Welcome to Text Based Adventure!")
time.sleep(1)
maptype = input("Enter your map size \n For Small enter 's' - map size 5-9 \n For Medium enter 'm' - map size 10-16 \n For Large  enter 'l' - map size 17-25 \n")
if maptype == "s":
	print ("You have selected map type small")
	rooms = random.randint(5,9) 
	roomcount +=rooms
	print ( "Map size is : %s" % rooms)
elif maptype == "m":
	print ("You have selected map type medium")
	rooms = random.randint(10,16)
	roomcount +=rooms
	print ( "Map size is : %s" % rooms)
elif maptype == "l":
	print ("You have selected map type large")
	rooms = random.randint(17,23)
	roomcount +=rooms
	print ( "Map size is : %s" % rooms)
else:
	print("Not Valid")
	
time.sleep(2)
print("creating layout...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
while roomcount > 0:
		#game()


def makedoor(door):
	n=0
	e=0
	w=0
	s=0
	if door == 1:
		n = 1
		print("There's a door up ahead.")
	elif door == 2:
		n = 1
		e = 1
		print("There's a door up ahead & to the right.")
	elif door == 3:
		n = 1
		e = 1
		s = 1
		print("There's a door up ahead, to the right & to the behind.")
	elif door == 4:
		n = 1
		e = 1
		s = 1
		w = 1
		print("There's a door in every direction.")
	
	print ("pick a door by typing one of the following: \n type 'n' for theh door up ahead \n type 'e' for the door the right \n type 's' for the door behind you \n type 'w' for the door to the right")
	
	time.sleep(1)
	
	select = input("Make your selection here : \n")
	
	if select == "n" and n == 1:
		print ("You have gone forward.")
		roomcount-=1
		new = Room(random.choices(roomnames))
		new.displaytype()
	elif select == "e" and e == 1:
		print ("You have gone to the right.")
		roomcount-=1
		new = Room(random.choices(roomnames))
		new.displaytype()
		
		
def game():
	start = Room("Empty")
	start.displaytype()


	
