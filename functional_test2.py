from selenium import webdriver
import time
import py_gui_popup
import ssh1
import ssh2
import time_date
from rfmezz_serial import RfSerialFile
from universal_time import UniversalTime


# need to fix what time is being checked!!! same format
# Steps 14 of the functional test
class FunctionalTest2:
    name = 'AA-11751 Atlas Module Test Functional Test Starting at step 14'
    description = 'Automating the AA-11751 test, Steps 14-'

    # step 14 of functional test
    def set_up(self):
        # make driver variable global
        global driver
        # use the chrome webdriver so chrome websites and elements are accessible
        driver = webdriver.Chrome()
        # wait for driver to load
        time.sleep(3)
        # open the website
        # driver.get('http://192.168.0.10/#')
        driver.get('http://10.243.0.15/#')
        # screen opens as a full screen
        driver.maximize_window()
        # wait for full window
        time.sleep(20)

    def functional_test_2(self):
        click_module = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[2]/div[1]').click()
        time.sleep(2)
        click_atlas_board = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[3]/div[4]/div[1]').click()
        time.sleep(2)
        check_rf_serial = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div['
                                                       '2]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div['
                                                       '1]/input[5]').get_attribute('value')
        time.sleep(2)
        if check_rf_serial in RfSerialFile.read_file('cmd'):
            print('Correct RFMezz Serial Number')
        else:
            print('Incorrect RFMezz Serial Number')
            # ssh1.SSHConnect.ssh1_connect(self)
            # ssh1.SSHConnect.start_functional2(self)

        time.sleep(3)
        # scroll down on the modules window
        for i in range(80):
            driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[3]/div[3]/div[3]').click()
        # wait to scroll down
        time.sleep(3)
        click_spectral_net = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div/div/div[3]/div[59]/div[1]').click()
        time.sleep(3)
        click_system = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[2]/div['
            '1]/div/div/div[1]/div').click()
        for i in range(30):
            driver.find_element_by_xpath(
                '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div['
                '1]/div/div[2]/div[3]').click()
        time.sleep(3)

        check_time = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div['
            '1]/div/div[1]/div/div[4]/div[1]/input[2]').get_attribute('value')
        time.sleep(3)

        if time_date.TimeAndDate.get_time_date('date time') in check_time:
            print('Time is correct')
        else:
            time.sleep(20)
            # MAY BE CHECKING WRONG TIME OR TIME ON BOARD IS BROKEN?
            if time_date.TimeAndDate.get_time_date('date time') in check_time:
                print(time_date.TimeAndDate.get_time_date('date time'))
                print(check_time)
                print("Time is correct")
            # if time is still incorrect the test will reenter the commands to fix time
            else:
                print(time_date.TimeAndDate.get_time_date('date time'))
                print(check_time)
                print('Time is not correct')
                # ssh1.SSHConnect.ssh1_connect(self)
                # ssh1.SSHConnect.start_functional2(self)
                time.sleep(3)
                # py_gui_popup.PyGUIPopup.functional_rfmezz_test_3('fail time')

            driver.close()

    def ssh_command_2(self):
        ssh2.SSHConnect2.ssh2_connect(self)
        ssh2.SSHConnect2.open_gui_end_test(self)


if __name__ == "__main__":
    run2 = FunctionalTest2()
    run2.set_up()
    run2.functional_test_2()
    run2.ssh_command_2()
