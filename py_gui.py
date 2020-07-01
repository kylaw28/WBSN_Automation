import PySimpleGUI as sg
import functional_test
import rfmezz_serial


class PyGUI:
    name = 'GUI'
    description = 'Opens a GUI for the user to insert the rfmezz card serial number and start the AA-11751 Automation ' \
                  'test '

    def GUI_elements(self):
        # layout definition
        layout = [[sg.Text('Please enter the RFMezz Serial Number.', text_color='white',
                           background_color='Dark Red')],
                  [sg.InputText('RT-19150210', key='addr')],
                  [sg.Button('Submit', button_color=('white', 'black')), sg.Button('Cancel', button_color=('white',
                                                                                                           'black'))]]

        # create window
        sg.theme('Dark Red')
        window = sg.Window('KRATOS', layout,
                           icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest\favicon.ico')

        window_2 = False
        window_3 = False
        window_set = False

        event, values = window.read()
        print(event, values)
        text_input = values['addr']

        # Event loop
        while True:

            if event in (None, 'Cancel'):
                break
            if event in (None, 'Submit'):
                window.close()
                window_2 = True

                # layout definition of window 2
                layout_2 = [[sg.Text('Is this the correct RFMezz card Serial Number?', text_color='white',
                                     background_color='Dark Red')],
                            [sg.Text(text_input, text_color='white')],
                            [sg.Button('Yes', button_color=('white', 'black')),
                             sg.Button('No', button_color=('white', 'black'))]]

                # create window 2
                window2 = sg.Window('KRATOS', layout_2, icon=r'C:\Users\kyla.waguespack\PycharmProjects'
                                                             r'\automationTest\favicon.ico')
            # condition when 'Yes' is clicked on window 2, confirms correct serial and saves it to a file
            if window_2:
                event, values = window2.read()
                if event in (None, 'No'):
                    window = True
                    layout = [[sg.Text('Please enter the RFMezz Serial Number.', text_color='white',
                                       background_color='Dark Red')],
                              [sg.InputText('RT-191502109', text_color='black', background_color='white')],
                              [sg.Button('Submit', button_color=('white', 'black')),
                               sg.Button('Cancel', button_color=('white',
                                                                 'black'))]]

                    # create window
                    sg.theme('Dark Red')
                    window = sg.Window('KRATOS', layout,
                                       icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest\favicon.ico')
                    if event in (None, 'Cancel'):
                        break
                    if event in (None, 'Submit'):
                        window.close()
                    # break
                if event in (None, 'Yes'):
                    # saving the serial to a file
                    rfmezz_serial.RfSerialFile.write_to_file(text_input)
                    rfmezz_serial.RfSerialFile.read_file(text_input)

                    window_set = True

                    layoutt = [[sg.Text('Check...', text_color='white', background_color='Dark Red')],
                               [sg.Text('•  AC Power to PS1 and PS2', text_color='white', background_color='Dark Red')],
                               [sg.Text('•  Lower Atlas module ENET (GbE)  to Test PC ENET', text_color='white',
                                        background_color='Dark Red')],
                               [sg.Text('•  IRIG/1PPS In to Out', text_color='white', background_color='Dark Red')],
                               [sg.Text('•  10MHz In to Out', text_color='white', background_color='Dark Red')],
                               [sg.Text('•  Chassis serial to Test PC serial ', text_color='white',
                                        background_color='Dark Red')],
                               [sg.Text('•  RF-In to RF-Out ', text_color='white', background_color='Dark Red')],
                               [sg.Image(r'C:\Users\kyla.waguespack\PycharmProjects\automationTest\atlas_pic.png', size=(1500,500))],
                               [sg.Button('Confirm', button_color=('white', 'black')), sg.Button('Cancel',
                                                                                                   button_color=('white', 'black'))]]

                    window_set = sg.Window('KRATOS', layoutt,
                                           icon=r'C:\Users\kyla.waguespack\PycharmProjects\automationTest\favicon.ico')
            if window_set:
                event, values = window_set.read()
                if event in (None, 'Cancel'):
                    break
                if event in (None, 'Confirm'):
                    window_set.close()
                    window_3 = True

                    # layout definition of window 3
                    layout_3 = [[sg.Text('Click "Start" to begin the Automated Atlas Module Test (AA-11751)',
                                         text_color='white', background_color='Dark Red')],
                                [sg.Button('Start', button_color=('white', 'black')),
                                 sg.Button('Cancel', button_color=('white', 'black'))]]

                    # creates window 3
                    window3 = sg.Window('KRATOS', layout_3, size=(500, 100), icon=r'C:\Users\kyla.waguespack'
                                                                                  r'\PycharmProjects\automationTest'
                                                                                  r'\favicon.ico')
            # when start is clicked the automated test will begin
            if window_3:
                event, values = window3.read()
                if event in (None, 'Cancel'):
                    break
                if event in (None, 'Start'):
                    try:
                        print('functional')
                        functional_test.FunctionalTest.set_up('setup')
                        functional_test.FunctionalTest.check_health('health')
                        functional_test.FunctionalTest.functional_test('automation')
                        functional_test.FunctionalTest.get_result_file('result file')
                        functional_test.FunctionalTest.ssh_test('ssh')
                    except Exception as e:
                        pass


if __name__ == "__main__":
    run_gui = PyGUI()
    run_gui.GUI_elements()
