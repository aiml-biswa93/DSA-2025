class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

# creating instance/object of class
cookie_one = Cookie('red')
cookie_two = Cookie('blue')

print('this is: ', cookie_one)

# method calling of class
print('cookie one is: ', cookie_one.get_color())
print('cookie two is: ', cookie_two.get_color())

# now we haev to change color

cookie_one.set_color('yellow')

print('cookie one is: ', cookie_one.get_color())
print('cookie two is: ', cookie_two.get_color())
