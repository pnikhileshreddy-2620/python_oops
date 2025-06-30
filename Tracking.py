class Customer:
    customer=0
    def __init__(self, name):
        self.name=name
        Customer.customer+=1
    print(customer)
print(Customer.customer)
customer1= Customer("Nikhilesh")
customer2= Customer("Nikhilesh")
customer3= Customer("Nikhilesh")
customer4= Customer("Nikhilesh")
customer5= Customer("Nikhilesh")
customer6= Customer("Nikhilesh")
print(Customer.customer)