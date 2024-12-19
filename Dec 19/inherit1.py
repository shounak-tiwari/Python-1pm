# parent class 
class Enquiry:
    def __EnquiryInput(self):
        self.name = str(input('enter the name of student : '))
        self.course = str(input('enter the course of student : '))
        self.contact = int(input('enter the contact number : '))
        self.email = (input('enter the email : '))

    def EnquiryPrint(self):
        print('name of student ',self.name)
        print('course of student ',self.course)
        print('contact of student ',self.contact)
        print('email of student ',self.email)
    
# child class
class Details(Enquiry):
    def ChildInput(self):
        Enquiry.__EnquiryInput(self)
        self.start_date = input('enter date in date/month/year : ')
        self.faculty_name = input('enter name of trainer : ')

    def ChildPrint(self):
        Enquiry.EnquiryPrint(self)
        print('starting date of course : ',self.start_date)
        print('faculty name of course : ',self.faculty_name)



obj = Details()

obj.ChildInput()

obj.ChildPrint()