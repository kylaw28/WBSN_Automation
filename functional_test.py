from selenium import webdriver
import time
import py_gui_popup
import ssh1


# Steps 3-8 of the functional test
class FunctionalTest:
    name = 'AA-11751 Atlas Module Test Functional Test'
    description = 'Automating the AA-11751 test, Steps 1 - 8'

    # step 3 of functional test
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

    def check_health(self):
        # check module is connected
        check_connected = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[4]/div[3]')
        # grab the text
        is_connected = check_connected.text
        # check if the text says test paused so the test can continue, this means there are no fails if this text shows
        if "Connected" in is_connected:
            print('Yes, Connected')
        else:
            time.sleep(15)

    def functional_test(self):
        click_module = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[2]/div[1]').click()
        time.sleep(2)
        # scroll down on the modules window
        for i in range(80):
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[3]/div[3]/div[3]').click()
        # wait to scroll down
        time.sleep(3)

        # click scripted self test
        scripted_self_test = driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[3]/div[1]/div/div/div[3]/div[58]/div[1]').click()
        # wait for scripted self test to open
        time.sleep(3)

        # locate the definition file
        definition_file = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[1]/div[1]/input[2]')
        # clear the text in the definition file
        definition_file.clear()
        # wait for the text to be deleted
        time.sleep(3)
        # click the definition file
        definition_file.click()
        # insert rfMezz.txt into the definition file box
        definition_file.send_keys('rfMezz.txt')
        # wait for the rfMezz.txt to be inserted into the box
        time.sleep(3)

        # click apply
        click_apply = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div').click()
        # wait for the rfMezz.txt to turn from blue to black
        time.sleep(5)

        # click run
        click_run = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[1]/div[1]/div[2]').click()

        time.sleep(5)

        # scroll down on the script selftest page
        for i in range(55):
            scroll_script_selftest = driver.find_element_by_xpath(
                '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div['
                '2]/div/div/div[2]/div[3]').click()
            print("scrolled down")

        # wait for the tests to be run
        time.sleep(240)

        # location of the text
        check_test_paused = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div')
        print(check_test_paused)
        # grab the text then going to check if it says test paused
        is_this_test_paused = check_test_paused.text
        # check if the text says test paused so the test can continue, this means there are no fails if this text shows
        if "Test Paused: Connect a cable from RF OUT to RF IN; Press RUN to continue the test." in is_this_test_paused:
            print('Continue Test, No Fails')
        elif "PASSED" in is_this_test_paused:
            print('Continue Test, No Fails')
        else:
            py_gui_popup.PyGUIPopup.functional_rfmezz_test_1('fail')
            print("Test over, go to file to see results: " + is_this_test_paused)

        time.sleep(2)

        # check overall execution status
        check_overall_execution = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[2]/div[1]/input[9]').get_attribute('value')
        time.sleep(3)
        if 'FAILED' in check_overall_execution:
            print("Overall Execution Status: " + check_overall_execution)
            py_gui_popup.PyGUIPopup.functional_rfmezz_test_1('fail')
            # time.sleep(100000)
        else:
            print("Overall Execution Status: " + check_overall_execution)

        # scroll up on the screen so run can be clicked
        for i in range(40):
            scroll_up = driver.find_element_by_xpath(
                '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
                '2]/div[1]').click()

        time.sleep(2)

        # click run to test rf in to out
        run_to_test_rf = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[1]/div[1]/div[2]').click()

        time.sleep(240)

        # check if the results file has any fails
        check_overall_execution = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div['
            '1]/div/div[2]/div[1]/input[9]').get_attribute('value')

        # print the overall execution and print if needed the results file path if tests over
        if 'FAILED' in check_overall_execution:
            print("Overall Execution Status: " + check_overall_execution)
            # get the results file
            get_results_file = driver.find_element_by_xpath(
                '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div['
                '2]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div')
            results = get_results_file.text
            print("Check the results file here: " + results)
            py_gui_popup.PyGUIPopup.functional_rfmezz_test_2('fail')
        else:
            print("Overall Execution Status: " + check_overall_execution)
            ssh1.SSHConnect.ssh1_connect(self)
            print('sending commands')
            time.sleep(100)
            ssh1.SSHConnect.start_functional2(self)

        driver.close()

    # gets the results file
    def ssh_test(self):
        get_results_file = driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div[4]/div[3]/div[3]/div[2]/div/div/div/div/div[2]/div['
            '2]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div')
        results = get_results_file.text
        return results


if __name__ == "__main__":
    run = FunctionalTest()
    run.set_up()
    run.check_health()
    run.functional_test()
    run.get_result_file()
    run.ssh_test()
