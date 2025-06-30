class Method:
    def __init__(self):
        self.text=""
    def add_hello(self):
        self.text +="Hello"
        return self
    def add_greet(self, name):
        self.text+="Nice to meet"
        self.text +=name
        return  self
    def shout(self):
        print(self.text)
        return self

My =Method()
My.add_greet("Nikhilesh").add_hello().shout()
print(My.add_greet("Reddy").add_hello().shout())