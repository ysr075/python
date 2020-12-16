import time
import sys

def program():

	yeslist = ["yes", "y", "yeah", "c", "co", "continue"]
	ANDlist = ["AND", "and", '1']
	ORlist = ["OR", "or", '2']
	NOTlist = ["NOT", "not", '3']
	RESTART = ["restart", "RESTART", "r"]
	QUIT = ["QUIT", "STOP", "stop", "quit", "Q", "q", "S", "s"]

	choise = input("\nAND, OR, NOT: ")

	if choise in ANDlist:
		def ANDpoort():
			
			IF1 = float(input("\nIF1: "))
			IF2 = float(input("IF2: "))

			if IF1 == 1 and IF2 == 1:
				while True:
					try:
						print("\nlamp aan!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							ANDpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()

				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...:").lower()
						ANDpoort()
					except:
						exit()

			if IF1 < 1 or IF2 < 1:
				while True:
					try:
						print("\nlamp uit!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							ANDpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()

				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...:").lower()
						ANDpoort()
					except:
						exit()
		ANDpoort()

	if choise in ORlist:
		def ORpoort():

			IF1 = float(input("\nIF1: "))
			IF2 = float(input("IF2: "))

			if IF1 > 0 or IF2 > 0:
				while True:
					try:
						print("\nlamp aan!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							ORpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()

				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...:").lower()
						ORpoort()
					except:
						exit()

			if IF1 < 1 and IF2 < 1:
				while True:
					try:
						print("\nlamp uit!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							ORpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()

				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...:").lower()
						ORpoort()
					except:
						exit()
		ORpoort()

	if choise in NOTlist:
		def NOTpoort():

			IF1 = float(input("\nIF1: "))

			if IF1 == 0:
				while True:
					try:
						print("\nlamp aan!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							NOTpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()

				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...: ").lower()
						NOTpoort()
					except:
						exit()

			if IF1 == 1:
				while True:
					try:
						print("\nlamp uit!")
						restart = input("\nrefresh program... (c)ontinue looping? or (Q)uit or (r)estart ?: ").lower()
						if restart in yeslist:
							NOTpoort()
						if restart in RESTART:
							program()
						if restart in QUIT:
							print("\nprogram closing in 3sec...")
							seconds = int(3)
							for i in range(seconds):
							    print(str(seconds - i))
							    time.sleep(1)
							    def exitprogram():
							    	sys.exit()
							    exitprogram()
						else:
							exit()
					except:
						exit()
				while False:
					try:
						print("\ninput INVALID")
						restart = print("\nrefreshing program...: ").lower()
						NOTpoort()
					except:
						exit()

		NOTpoort()
program()
