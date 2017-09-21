#Created by : Sidney Kang
#Created on : 18 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit0-05
# This program does basic math

import ui

def equation1_touch_up_inside(sender):
	  #This displays the answer to the equation 5+2^3
	  view['answer_of_equation_1_label'].text = str(5+2^3)

def equation2_touch_up_inside(sender):
	  #This displays the answer to the equation 4/2+5
	  view['answer_of_equation_2_label'].text = str(4/2+5)
	  
def equation3_touch_up_inside(sender):
	  #This displays the answer to the equation 3+4*2
	  view['answer_of_equation_3_label'].text = str(3+4*2)
	 
def equation4_touch_up_inside(sender):
	  #This displays the answer to the equation 7-3+2
	  view['answer_of_equation_4_label'].text = str(7-3+2)
	  
view = ui.load_view()
view.present('sheet')
