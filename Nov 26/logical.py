import re

def Validation_Name(first,last):
	First_regrex= r"^[A-Za-z\s]+$"
	Last_regrex = r"^[A-Za-z\s]+$"

	if re.match(First_regrex,first) and re.match(Last_regrex,last):
		return "valid name "
	else:
		return "enter valid name"


def Validation_EC(email,contact):
	E_mail_regrex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

	Contact_regrex = r"^(\+91[\s-]?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}$"

	if re.match(E_mail_regrex,email) and re.match(Contact_regrex,contact):
		return "valid EC details"
	else:
		return "Enter and check ec details"


