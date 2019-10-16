 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='initial_tumor_radius', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.initial_tumor_radius = FloatText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='distance_from_center', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.distance_from_center = FloatText(
          value=200,
          step=10,
          style=style, layout=widget_layout)

        param_name4 = Button(description='cell_relative_adhesion', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.cell_relative_adhesion = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.apoptosis_rate = FloatText(
          value=0.0027777777777,
          step=0.0001,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='micrometer', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='micrometer', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.initial_tumor_radius, units_button2, desc_button2] 
        row3 = [param_name3, self.distance_from_center, units_button3, desc_button3] 
        row4 = [param_name4, self.cell_relative_adhesion, units_button4, desc_button4] 
        row5 = [param_name5, self.apoptosis_rate, units_button5, desc_button5] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.initial_tumor_radius.value = float(uep.find('.//initial_tumor_radius').text)
        self.distance_from_center.value = float(uep.find('.//distance_from_center').text)
        self.cell_relative_adhesion.value = float(uep.find('.//cell_relative_adhesion').text)
        self.apoptosis_rate.value = float(uep.find('.//apoptosis_rate').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//initial_tumor_radius').text = str(self.initial_tumor_radius.value)
        uep.find('.//distance_from_center').text = str(self.distance_from_center.value)
        uep.find('.//cell_relative_adhesion').text = str(self.cell_relative_adhesion.value)
        uep.find('.//apoptosis_rate').text = str(self.apoptosis_rate.value)
