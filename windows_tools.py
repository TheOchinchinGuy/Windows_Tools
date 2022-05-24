def cleartemp():
	"""
	It deletes the contents of the Windows Temp folder, the Windows Software Distribution folder, and
	the Windows Prefetch folder.
	"""
	import os, subprocess

	del_dir = r'C:\\Users\\%userprofile%\\AppData\\Local\\Temp'
	del_dir2 = r'C:\\Windows\\Temp'
	del_dir3 = r'C:\\Windows\\SoftwareDistribution\\Download'
	del_dir4 = r'C:\\Windows\\Prefetch'

	obj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
	obj2 = subprocess.Popen('rmdir /S /Q %s' % del_dir2, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
	obj3 = subprocess.Popen('rmdir /S /Q %s' % del_dir3, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
	obj4 = subprocess.Popen('rmdir /S /Q %s' % del_dir4, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

	trp = obj.communicate()
	trp2= obj2.communicate()
	trp3= obj3.communicate()
	trp4= obj4.communicate()

	rCod = obj.returncode
	rCod2 = obj2.returncode
	rCod3 = obj3.returncode
	rCod4 = obj4.returncode

	if rCod == 0:
		print('Success: Cleaned Windows Temp Folder \n')
	else:
		print('Fail: Unable to Clean Windows Temp Folder \n')

# def install_programs():

while(True):
	def print_menu():
		"""
		The function print_menu() prints the menu options
		"""
		print('1- Clear Temp Files')
		print('2- Install Programs')
		print('3- Debloat System')
		print('4- Exit')
	print_menu()

	# A menu that allows the user to choose what they want to do.
	option = int(input ('Enter your choise: '))
	if option == 1:
		cleartemp()
	elif option == 2:
		print("Test: Installing programs..")
	elif option == 3:
		print("Test: Debloating system...")
	elif option == 4:
		# Exiting the program.
		exit()
