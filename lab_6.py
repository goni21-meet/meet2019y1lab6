#import turtle
#x = 0
#while x<300:
 #   y = x**2/300
  #  turtle.goto(x,y)
   # print( turtle.pos())

    #x = x+100
    



#turtle.mainloop()

import turtle
num_pts = 5
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()


