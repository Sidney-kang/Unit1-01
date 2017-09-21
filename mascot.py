#Created by : Sidney Kang
#Created on : 19 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit1-01
# This program displays the school name and their mascot

import ui

def st_mother_teresa_touch_up_inside(sender):
	  #This displays the school name and mascot of St. Mother Teresa High School
	  view['school_name_label'].text = 'St. Mother Teresa High school'
	  view['mascot_label'].text = 'Titans'

def st_joseph_touch_up_inside(sender):
	  #This displays the school name and mascot of St. Joseph High School
	  view['school_name_label'].text = 'St. Joseph High school'
	  view['mascot_label'].text = 'Jaguars'

def st_mark_touch_up_inside(sender):
	  #This displays the school name and mascot of St. Mark High School
	  view['school_name_label'].text = 'St. Mark High school'
	  view['mascot_label'].text = 'Lions'
	
view = ui.load_view()
view.present('sheet')
