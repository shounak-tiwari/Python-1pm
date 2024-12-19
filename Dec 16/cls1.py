class Class_name:

	def input_cls(temp):
		name = input('enter the name of student : ')
		address = input('enter the address of student : ')

		temp.x = name 
		temp.y = address

	def print_cls(temp):
		print('Name of student : ',temp.x)
		print('address of student : ',temp.y)


Piyush = Class_name()

Piyush.input_cls()

Piyush.print_cls()
