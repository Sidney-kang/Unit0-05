#Created by : Sidney Kang
#Created on : 18 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit0-05
# This program calculates the area and the perimeter of rectangle

import ui

def perimeter_and_area_of_rectangle_touch_up_inside(sender):
	  #This displays the perimeter and area of the rectangle
	  view['perimeter_of_rectangle_label'].text ="Perimeter ="+str(5*3)+" cm"
	  view['area_of_rectangle_label'].text = "Area ="+str(2*3+2*5)+" cm^2"  
	  
view = ui.load_view()
view.present('sheet')
