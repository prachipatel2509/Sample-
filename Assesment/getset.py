class getset():
    def __init__(self):
        self.string=""
        
    def get(self):
        self.string=raw_input("enter anything: ")
        
    
    def se(self):
        print("You enterd: ")
        print(self.string)

obj=getset()
obj.get()
obj.se()
