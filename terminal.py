def shell():
	import os
	import time
	import shutil
	while True:	
		os.system("title mash")
		cwd = os.getcwd()
		print(cwd)
		shellInput = input("$ ")
		if shellInput=="ls":
			for i in os.listdir():
				print(i)
		elif shellInput=="cd":
			print("Enter the path of the folder")
			change_path_input = input()
			try:
				os.chdir(change_path_input)
			except Exception as e:
				print(e)
		elif shellInput=="read":
			print("Enter the name of which file you want to read")
			which_file_to_read = input()
			try:
				f = open(which_file_to_read)
				print(f.read())
			except Exception as e:
				print(e)

		elif shellInput=="rm":
			print("Which file you want to remove")
			which_to_remove = input()
			try:
				os.remove(which_to_remove)
				print("Removed")
			except Exception as e:
				print(e)
			
		elif shellInput=="exit":
			print("logout")
			time.sleep(1)
			exit()
		elif shellInput=="pwd":
			print(os.getcwd())
		elif shellInput=="--mash":
			print("you are already inside the mash")
		elif shellInput=="cls":
			continue
		elif shellInput=="mkrepo":
			os.makedirs('.repo/version1')
			print('Which file you want to send to version1')
			which_to_add_version1 = input()
			try:
				shutil.copy(which_to_add_version1, ".repo/version1")
			except Exception as e:
				print(e)
			
		elif shellInput=="clear":
			os.system('cls')
		elif shellInput=="code":
			try:
				os.system('code')
			except Exception as e:
				print(e)
			
		elif shellInput=="python":
			try:
				os.system('python')
			except Exception as e:
				print(e)
		elif shellInput=="":
			continue
		else:
			try:
				os.system(shellInput)
			except Exception as e:
				print(e)


shell()