import os

def rename_files():
	file_list = os.listdir(r"/Users/Angadlamba21/Documents/Myprojects/python/udacity/prank")
	print file_list

	saved_path = os.getcwd()
	os.chdir(r"/Users/Angadlamba21/Documents/Myprojects/python/udacity/prank")
	for file_name in file_list:
		os.renames(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
rename_files()