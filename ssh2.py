import paramiko

# last test to run for the functional test
import py_gui_popup


class SSHConnect2:

    # connect to module and send last commands
    def ssh2_connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('10.243.0.15', username='root', password=')98&YuiOKjhGVbnM')

        # send command
        stdin, stdout, stderr = ssh.exec_command('systemctl start ntpd')
        print('sent last command')

    def open_gui_end_test(self):
        print('open gui')
        py_gui_popup.PyGUIPopup.functional_test_done(self)


if __name__ == "__main__":
    ssh_run2 = SSHConnect2()
    ssh_run2.ssh2_connect()
    ssh_run2.open_gui_end_test()
