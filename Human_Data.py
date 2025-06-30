class MAN:
    def __init__(self,name, email, phone, city,pincode):
        self.name=name
        self.email=email
        self.phone=phone
        self.city=city
        self.pincode=pincode


man1 = MAN("Ravi", "ravi@example.com", "9876543210", "Hyderabad", "500001")
man2 = MAN("Sita", "sita@example.com", "8765432109", "Bangalore", "560001")
man3 = MAN("Amit", "amit@example.com", "7654321098", "Mumbai", "400001")
man4 = MAN("Priya", "priya@example.com", "6543210987", "Chennai", "600001")
man5 = MAN("Karan", "karan@example.com", "5432109876", "Delhi", "110001")



All_data =[man1,man2,man3,man4,man5]
print("Before updating the Instance")
for person in All_data:
    print(f"My Myself {person.name}I am from {person.city} and my pincode is {person.pincode} email {person.email} Telephone No{person.phone}")

print("After updating the MAN 5 instance ")
man5.name='Nikhilesh'
for person in All_data:
    print(f"My Myself {person.name}I am from {person.city} and my pincode is {person.pincode} email {person.email} Telephone No{person.phone}")

