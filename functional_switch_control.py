import time


# should be running through the functional and calibration test
class FunctionalSwitchControl:
    name = 'Switch Control'
    description = 'Control which ports are on depending if the functional test or the calibration test is running'

    # driver1 controls one switch
    # driver2 controls another switch

    # set up the switch
    def switch_1(self):
        global driver1
        # use the chrome webdriver so chrome websites and elements are accessible
        driver1 = webdriver.Chrome()
        # wait for driver to load
        time.sleep(1)
        # open the website
        driver1.get('http://192.168.0.9/')
        # screen opens as a full screen
        driver1.maximize_window()
        time.sleep(1)
        # if functional test running driver1 port 2 on and driver2 port 2 on
        # port 2 ON
        driver1.find_element_by_id("ButtonPA2").click()
        time.sleep(10)

    def switch_2(self):
        global driver2
        # use the chrome webdriver so chrome websites and elements are accessible
        driver2 = webdriver.Chrome()
        # wait for driver to load
        time.sleep(1)
        # open the website
        driver2.get('http://192.168.0.9/')
        # screen opens as a full screen
        driver2.maximize_window()
        time.sleep(1)
        # if functional test running driver1 port 2 on and driver2 port 2 on
        # port 2 ON
        driver2.find_element_by_id("ButtonPA2").click()
        time.sleep(10)


if __name__ == "__main__":
    run = FunctionalSwitchControl()
    run.switch_1()
    run.switch_2()
