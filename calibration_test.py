import selenium
from selenium import webdriver
import time


class CalibrationTest:
    name = 'Calibration Test'
    description = 'Automationing the Calibration test portion of the AA-11751 test'

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
        time.sleep(10)

    def calibration_test(self):
        # open modules
        click_module = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[2]/div[1]').click()
        # scroll down on the modules window
        for i in range(60):
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/div[3]/div[3]').click()
        # wait to scroll down
        time.sleep(3)

        # click the network configurations
        network_config = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[3]/div[43]/div[1]').click()
        time.sleep(2)

        # click the ip address and change it
        click_ip = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div/div[1]/div[1]/div[2]/input[1]')
        click_ip.clear()
        click_ip.send_keys('10.243.68.110 ')
        time.sleep(2)

        # click the gaetway and change the ip address
        click_gateway = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div/div[1]/input[1]')
        click_gateway.clear()
        click_gateway.send_keys('10.243.68.1')
        time.sleep(3)

        # click_apply = driver.find_element_by_xpath(
        #   '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div')

        for i in range(60):
            scroll_up = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]').click()
        time.sleep(3)

        click_eprom = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div/div/div[3]/div[5]/div[1]').click()
        time.sleep(3)

        # figure out how to check the duplex
        check_duplex = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[2]/div['
            '2]/div/div/div/div/div[2]/div[1]/div[7]').get_attribute('value')
        print(check_duplex)


if __name__ == "__main__":
    cal_run = CalibrationTest()
    cal_run.set_up()
    cal_run.calibration_test()
