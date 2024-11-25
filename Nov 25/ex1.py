
import re

def UserFormValidation(first,last,email,phone,dob):
	First_regrex= r"^[A-Za-z\s]+$"

	Last_regrex = r"^[A-Za-z\s]+$"

	E_mail_regrex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

	Contact_regrex = r"^(\+91[\s-]?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{3}[\s-]?\d{4}$"

	#Contact_regrex = r"^(\+?\d{1,3}[-\s]?)?(\(?\d{3}\)?[-\s]?)?\d{3}[-\s]?\d{4}$"

	Date_of_birth_regrex =   r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d\d$|^\d{4}-\d{2}-\d{2}$"

	if re.match(First_regrex , first):
		if re.match(Last_regrex , last):
			if re.match(E_mail_regrex , email):
				if re.match(Contact_regrex,phone):
						return "valid"
				else:
					return "contact not valid"
			else:
				return "e-mail not valid"

		else:
			return "last name not vaild"
	else:
		return "first name not valid"


#DD/MM/YYYY


result = UserFormValidation('Piyush','Verma','Piyushvarma@123gmail.com','+91 898718828288','04/10/2000')

print(result)