from random import randint

print("Luật:\nChon Keo, Dam, Bao")

player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Dam"
if computer == 1:
	computer = "Keo"
if computer == 2:
	computer = "Bao"

print("--")
print("Youu CHoose:" + player)
print("Computer Choose" + computer)
print("--")

if player == "Keo":
	if computer == "Keo":
		print("Hòa")
	if computer == "Dam":
		print("Thua")
	else:
		print("Thắng")

if player == "Dam":
	if computer == "Keo":
		print("Thắng")
	if computer == "Dam":
		print("Hòa")
	else:
		print("Thua")

if player == "La":
	if computer == "Keo":
		print("Thua")
	if computer == "Dam":
		print("Thắng")
	else:
		print("Hòa")