def input_student():
	rec_dic = dict()
	for x in range(4):
		new_dic = dict()
		new_dic['name'] = input('enter the name of student : ')

		for marks in range(1,6):
			new_dic[f'{marks}'] = input('enter the marks of student : ')

		rec_dic['x'] = new_dic

input_student()