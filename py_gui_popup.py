import PySimpleGUI as sg
import sys
import functional_test
import ssh1


class PyGUIPopup:
    name = 'GUI Popups'
    description = 'Opens a GUI for each section of the test if it passed or failed'

    def functional_rfmezz_test_1(self):
        layout_4 = [[sg.Text('Functional RFMezz Test Pt.1', text_color='white',
                             background_color='Dark Red')],
                    [sg.Text('Overall Execution Status: FAILED', text_color='white', background_color='Dark Red')],
                    [sg.Text('Results Filename:', text_color='white', background_color='Dark Red')],
                    [sg.Text('file', text_color='white', background_color='Dark Red')],
                    [sg.Button('Done', button_color=('white', 'black'))]]
        sg.theme('Dark Red')
        window4 = sg.Window('KRATOS', layout_4, icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest'
                                                     r'\favicon.ico')
        # Event loop
        while True:
            event, values = window4.read()
            if event in (None, 'Done'):
                sys.exit()

    def functional_rfmezz_test_2(self):
        layout_5 = [[sg.Text('Functional RFMezz Test Pt.2', text_color='white',
                             background_color='Dark Red')],
                    [sg.Text('Overall Execution Status: FAILED', text_color='white', background_color='Dark Red')],
                    [sg.Text('Results Filename:', text_color='white', background_color='Dark Red')],
                    [sg.Text('file', text_color='white', background_color='Dark Red')],
                    [sg.Button('Done', button_color=('white', 'black'))]]
        sg.theme('Dark Red')
        window5 = sg.Window('KRATOS', layout_5, icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest'
                                                     r'\favicon.ico')
        # Event loop
        while True:
            event, values = window5.read()
            if event in (None, 'Done'):
                sys.exit()

    def functional_rfmezz_test_3(self):
        layout_6 = [[sg.Text('Functional Test, Incorrect Time', text_color='white',
                             background_color='Dark Red')],
                    [sg.Text('file', text_color='white',
                             background_color='Dark Red')],
                    [sg.Button('Done', button_color=('white', 'black'))]]
        sg.theme('Dark Red')
        window6 = sg.Window('KRATOS', layout_6, icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest'
                                                     r'\favicon.ico')
        # Event loop
        while True:
            event, values = window6.read()
            if event in (None, 'Done'):
                # ssh1.SSHConnect.ssh1_connect(self)
                # ssh1.SSHConnect.start_functional2(self)
                sys.exit()

    def functional_test_done(self):
        layout_7 = [[sg.Text('Functional Test Passed, test is done.', text_color='white',
                             background_color='Dark Red')],
                    [sg.Text('Results File', text_color='white',
                             background_color='Dark Red')],
                    [sg.Button('Done', button_color=('white', 'black'))]]
        sg.theme('Dark Red')
        window7 = sg.Window('KRATOS', layout_7, icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest'
                                                     r'\favicon.ico')
        # Event loop
        while True:
            event, values = window7.read()
            if event in (None, 'Done'):
                sys.exit()


if __name__ == "__main__":
    run_gui_pop = PyGUIPopup()
    # run_gui_pop.functional_rfmezz_test_1()
    # run_gui_pop.functional_rfmezz_test_2()
    # run_gui_pop.functional_rfmezz_test_3()
    run_gui_pop.functional_test_done()
