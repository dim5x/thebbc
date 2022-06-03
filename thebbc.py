# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res': './res/'})

    def idle(self):
        # idle function called every update cycle
        pass

    def main(self):
        return untitled.construct_ui(self)

    @staticmethod
    def construct_ui(self):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        vbox0 = VBox()
        vbox0.attr_class = "VBox"
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "center"
        vbox0.css_align_self = "center"
        vbox0.css_background_color = "rgb(146,197,159)"
        vbox0.css_border_style = "solid"
        vbox0.css_border_width = "0px"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "100%"
        vbox0.css_justify_content = "space-around"
        vbox0.css_left = "0px"
        vbox0.css_position = "absolute"
        vbox0.css_top = "0px"
        vbox0.css_width = "100%"
        vbox0.variable_name = "vbox0"
        hbox0 = HBox()
        hbox0.attr_class = "HBox"
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = "center"
        hbox0.css_background_color = "rgb(146,197,159)"
        hbox0.css_border_style = "solid"
        hbox0.css_border_width = "0px"
        hbox0.css_display = "flex"
        hbox0.css_flex_direction = "row-reverse"
        hbox0.css_height = "50%"
        hbox0.css_justify_content = "space-around"
        hbox0.css_order = "-1"
        hbox0.css_position = "static"
        hbox0.css_top = "0px"
        hbox0.css_visibility = "visible"
        hbox0.css_width = "100%"
        hbox0.variable_name = "hbox0"
        container1 = Container()
        container1.attr_class = "Container"
        container1.attr_editor_newclass = False
        container1.css_align_content = "inherit"
        container1.css_align_items = "baseline"
        container1.css_align_self = "inherit"
        container1.css_border_radius = "5px"
        container1.css_border_style = "solid"
        container1.css_border_width = "1px"
        container1.css_flex = "-1"
        container1.css_flex_direction = "column-reverse"
        container1.css_flex_flow = "inherit"
        container1.css_flex_wrap = "wrap-reverse"
        container1.css_float = "none"
        container1.css_height = "100%"
        container1.css_justify_content = "space-around"
        container1.css_order = "0"
        container1.css_position = "static"
        container1.css_top = "0px"
        container1.css_width = "49%"
        container1.variable_name = "container1"
        hbox1 = HBox()
        hbox1.attr_class = "HBox"
        hbox1.attr_editor_newclass = False
        hbox1.css_align_items = "center"
        hbox1.css_background_color = "rgb(255,255,255)"
        hbox1.css_display = "flex"
        hbox1.css_flex_direction = "row"
        hbox1.css_height = "50%"
        hbox1.css_justify_content = "space-around"
        hbox1.css_left = "0px"
        hbox1.css_position = "inherit"
        hbox1.css_top = "0px"
        hbox1.css_visibility = "visible"
        hbox1.css_width = "100%"
        hbox1.variable_name = "hbox1"
        textinput0 = TextInput()
        textinput0.attr_editor_newclass = False
        textinput0.attr_maxlength = "499"
        textinput0.attr_title = "Input link here."
        textinput0.css_height = "30px"
        textinput0.css_order = "-1"
        textinput0.css_position = "static"
        textinput0.css_top = "154.5749969482422px"
        textinput0.css_width = "75%"
        textinput0.text = ""
        textinput0.variable_name = "textinput0"
        hbox1.append(textinput0, 'textinput0')
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.attr_title = "Push me!"
        button0.css_height = "30px"
        button0.css_order = "-1"
        button0.css_position = "static"
        button0.css_top = "132.5749969482422px"
        button0.css_width = "100px"
        button0.text = "Send"
        button0.variable_name = "button0"
        hbox1.append(button0, 'button0')
        container1.append(hbox1, 'hbox1')
        hbox0.append(container1, 'container1')
        container2 = Container()
        container2.attr_class = "Container"
        container2.attr_editor_newclass = False
        container2.css_border_radius = "5px"
        container2.css_border_style = "solid"
        container2.css_border_width = "1px"
        container2.css_height = "100%"
        container2.css_order = "-1"
        container2.css_position = "static"
        container2.css_top = "0px"
        container2.css_width = "49%"
        container2.variable_name = "container2"
        hbox0.append(container2, 'container2')
        vbox0.append(hbox0, 'hbox0')
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_background_color = "rgb(176,177,169)"
        container0.css_border_color = "rgb(28,0,0)"
        container0.css_border_radius = "5px"
        container0.css_border_style = "solid"
        container0.css_border_width = "1px"
        container0.css_color = "rgb(0,0,0)"
        container0.css_height = "47%"
        container0.css_order = "-1"
        container0.css_position = "static"
        container0.css_top = "49%"
        container0.css_width = "99%"
        container0.variable_name = "container0"
        tablewidget0 = TableWidget()
        tablewidget0.attr_class = "TableWidget"
        tablewidget0.attr_editor_newclass = False
        tablewidget0.column_count = 4
        tablewidget0.css_display = "table"
        tablewidget0.css_float = "none"
        tablewidget0.css_height = "100px"
        tablewidget0.css_left = "75.0px"
        tablewidget0.css_position = "inherit"
        tablewidget0.css_top = "345.0px"
        tablewidget0.css_width = "100%"
        tablewidget0.row_count = 4
        tablewidget0.use_title = True
        tablewidget0.variable_name = "tablewidget0"
        container0.append(tablewidget0, 'tablewidget0')
        vbox0.append(container0, 'container0')

        self.vbox0 = vbox0
        return self.vbox0


# Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081,
                 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True,
                 'config_resourcepath': './res/'}
if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'],
          multiple_instance=configuration['config_multiple_instance'],
          enable_file_cache=configuration['config_enable_file_cache'],
          start_browser=configuration['config_start_browser'])
