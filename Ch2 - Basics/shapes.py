class Shape():
    def __init__(self,body):
        self.body=body
    def color(self,bColor):
        self.bColor=bColor
class Triangle(Shape):
    def __init__(self, height,length):
        super().__init__(Triangle)
        self.height=height
        self.length=length
        
    def color(self,bcolor):
        super().color(bcolor)
    def area(self):
        self.area=0.5*self.height*self.length
        print("The color of my Triangle is ",self.bColor," and area is ",self.area)
class Rectangle(Shape):
    def __init__(self, height,width):
        super().__init__(Rectangle)
        self.height=height
        self.width=width
    def color(self, Color):
        super().color(Color)
    def area(self):
        self.area=self.height*self.width
        print("The color of my Triangle is ",self.bColor," and area is ",self.area)
r1=Rectangle(3,6)
t1=Triangle(6,9)
t2=Triangle(7,76)
r1.color("red")
t1.color("blue")
t2.color("black")
r1.area()
t1.area()
t2.area()
