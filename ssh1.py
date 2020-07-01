import sys

from paramiko import client
import paramiko
import time
import functional_test
import functional_test2
from rfmezz_serial import RfSerialFile
from universal_time import UniversalTime
from selenium import webdriver


class SSHConnect:
    def ssh1_connect(self):
        # connects to the client
        while True:
            print('Trying to connect')
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect('10.243.0.15', username='root', password=')98&YuiOKjhGVbnM')
                print('Connected to host')
                break
            except paramiko.AuthenticationException:
                print('Authentication failed when connecting to host')
                sys.exit(1)
            except:
                print('Could not connect to host')

        # get universal time
        univ_time = UniversalTime.real_time('utc')
        # get the most recent inputted serial number from the file to send the command 'fw_setenv RFMEZZSN' + serial_num
        serial_num = RfSerialFile.read_file('cmd')
        time.sleep(3)

        cmd_1 = 'fw_setenv RFMEZZSN ' + serial_num
        stdin, stdout, stderr = ssh.exec_command(str(cmd_1))
        print('sent 1 command ' + serial_num)
        time.sleep(3)

        cmd_2 = 'systemctl stop rtlogic-snl'
        stdin, stdout, stderr = ssh.exec_command(str(cmd_2))
        print('sent 2 command')
        time.sleep(3)

        cmd_3 = 'systemctl stop ntpd'
        stdin, stdout, stderr = ssh.exec_command(str(cmd_3))
        print('sent 3 command')
        time.sleep(3)

        cmd_4 = 'date - -set=' + univ_time
        stdin, stdout, stderr = ssh.exec_command(str(cmd_4))
        print('sent 4 command ' + univ_time)
        time.sleep(3)

        cmd_5 = 'hwclock - -systohc'
        stdin, stdout, stderr = ssh.exec_command(str(cmd_5))
        print('sent 5 command')
        time.sleep(3)

        cmd_6 = 'systemctl start rtlogic-snl'
        stdin, stdout, stderr = ssh.exec_command(str(cmd_6))
        print('sent 6 command')
        time.sleep(3)

        cmd_7 = 'sudo reboot'
        stdin, stdout, stderr = ssh.exec_command(str(cmd_7))
        print('sent 7 command')
        time.sleep(270)

    # open up the 2nd part of the functional test to check if the time is accurate
    def start_functional2(self):
        functional_test2.FunctionalTest2.set_up('setup')
        functional_test2.FunctionalTest2.functional_test_2('test2')
        functional_test2.FunctionalTest2.ssh_command_2('ssh2')


if __name__ == "__main__":
    ssh_run = SSHConnect()
    # ssh_run.set_GUI_timing()
    ssh_run.ssh1_connect()
    ssh_run.start_functional2()
