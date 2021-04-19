print("hello GitHub")
class MyName():
    def __init__(self):
        self.my_name = None
    
    def __call__(self, name = 'Incoginto'):
        self.my_name = name
        return "name memorized"
#main code 
myn = MyName()
print(myn.("Serge"))
