 
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
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='live_phase_duration', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.live_phase_duration = FloatText(
          value=0.0075,
          step=0.001,
          style=style, layout=widget_layout)

        param_name3 = Button(description='init_cells_filename', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.init_cells_filename = Text(
          value='./config/init.txt',
          style=style, layout=widget_layout)

        param_name4 = Button(description='bnd_file', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.bnd_file = Text(
          value='./config/boolean_network/TNF_nodes.bnd',
          style=style, layout=widget_layout)

        param_name5 = Button(description='cfg_file', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.cfg_file = Text(
          value='./config/boolean_network/TNF_conf.cfg',
          style=style, layout=widget_layout)

        param_name6 = Button(description='maboss_time_step', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.maboss_time_step = FloatText(
          value=10.,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='tnf_uptake_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.tnf_uptake_rate = FloatText(
          value=0.6109,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='tnf_secretion_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.tnf_secretion_rate = FloatText(
          value=0.76032,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='duration_add_tnf', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.duration_add_tnf = IntText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='time_remove_tnf', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.time_remove_tnf = IntText(
          value=8000,
          step=100,
          style=style, layout=widget_layout)

        param_name11 = Button(description='time_add_tnf', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.time_add_tnf = IntText(
          value=150,
          step=10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='tnf_threshold', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.tnf_threshold = FloatText(
          value=0.25506,
          step=0.01,
          style=style, layout=widget_layout)

        param_name13 = Button(description='concentration_tnf', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.concentration_tnf = FloatText(
          value= 0.5 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='membrane_length', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.membrane_length = IntText(
          value= 470 ,
          step=10,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='fg/cell/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='ng/mL', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.live_phase_duration, units_button2, desc_button2] 
        row3 = [param_name3, self.init_cells_filename, units_button3, desc_button3] 
        row4 = [param_name4, self.bnd_file, units_button4, desc_button4] 
        row5 = [param_name5, self.cfg_file, units_button5, desc_button5] 
        row6 = [param_name6, self.maboss_time_step, units_button6, desc_button6] 
        row7 = [param_name7, self.tnf_uptake_rate, units_button7, desc_button7] 
        row8 = [param_name8, self.tnf_secretion_rate, units_button8, desc_button8] 
        row9 = [param_name9, self.duration_add_tnf, units_button9, desc_button9] 
        row10 = [param_name10, self.time_remove_tnf, units_button10, desc_button10] 
        row11 = [param_name11, self.time_add_tnf, units_button11, desc_button11] 
        row12 = [param_name12, self.tnf_threshold, units_button12, desc_button12] 
        row13 = [param_name13, self.concentration_tnf, units_button13, desc_button13] 
        row14 = [param_name14, self.membrane_length, units_button14, desc_button14] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
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
        self.live_phase_duration.value = float(uep.find('.//live_phase_duration').text)
        self.init_cells_filename.value = (uep.find('.//init_cells_filename').text)
        self.bnd_file.value = (uep.find('.//bnd_file').text)
        self.cfg_file.value = (uep.find('.//cfg_file').text)
        self.maboss_time_step.value = float(uep.find('.//maboss_time_step').text)
        self.tnf_uptake_rate.value = float(uep.find('.//tnf_uptake_rate').text)
        self.tnf_secretion_rate.value = float(uep.find('.//tnf_secretion_rate').text)
        self.duration_add_tnf.value = int(uep.find('.//duration_add_tnf').text)
        self.time_remove_tnf.value = int(uep.find('.//time_remove_tnf').text)
        self.time_add_tnf.value = int(uep.find('.//time_add_tnf').text)
        self.tnf_threshold.value = float(uep.find('.//tnf_threshold').text)
        self.concentration_tnf.value = float(uep.find('.//concentration_tnf').text)
        self.membrane_length.value = int(uep.find('.//membrane_length').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//live_phase_duration').text = str(self.live_phase_duration.value)
        uep.find('.//init_cells_filename').text = str(self.init_cells_filename.value)
        uep.find('.//bnd_file').text = str(self.bnd_file.value)
        uep.find('.//cfg_file').text = str(self.cfg_file.value)
        uep.find('.//maboss_time_step').text = str(self.maboss_time_step.value)
        uep.find('.//tnf_uptake_rate').text = str(self.tnf_uptake_rate.value)
        uep.find('.//tnf_secretion_rate').text = str(self.tnf_secretion_rate.value)
        uep.find('.//duration_add_tnf').text = str(self.duration_add_tnf.value)
        uep.find('.//time_remove_tnf').text = str(self.time_remove_tnf.value)
        uep.find('.//time_add_tnf').text = str(self.time_add_tnf.value)
        uep.find('.//tnf_threshold').text = str(self.tnf_threshold.value)
        uep.find('.//concentration_tnf').text = str(self.concentration_tnf.value)
        uep.find('.//membrane_length').text = str(self.membrane_length.value)
