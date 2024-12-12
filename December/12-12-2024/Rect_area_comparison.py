class rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
        
    def Area(self):
        return self.length * self.width
    
    def peri(self):
        return 2*(self.length + self.width)
    
rect1 = rectangle(93,8)
rect2 = rectangle(67,9)

print(f'Area1: {rect1.Area()}')
print(f'Perimeter1: {rect1.peri()}')
print(f'Area2: {rect2.Area()}')
print(f'Perimeter2: {rect2.peri()}')

if(rect1.Area() ==rect2.Area()):
    print("Areas are same")
else:
    print("Areas are not same")
