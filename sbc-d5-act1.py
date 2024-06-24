#CORRUPT OFFICES
offices = []
def person():
	for i in range(5):
		i = input("Enter a person: ")
		offices.append(i)
def service():
	try: 
		x = len(offices)
		print(x)
		while x >= 1:
			head = input("Naa or Wala ang head: ").capitalize()
			if head == "Naa":
				head = True
			else:
				head = False
			if head is True:
				offices.pop(0)
				print("QUEUE")
				print(offices)
			else:
				print("STACK")
				offices.pop(-1)
				print(offices)
	except IndexError:
		print("Wala nay sulod")

person()
service()