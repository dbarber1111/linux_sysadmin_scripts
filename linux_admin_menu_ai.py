#!/usr/bin/python3
##########################################################################
# Scriptname    : linux_admin_menu_ai.py
# Description   : Linux CLI Administration Assistant (OOP Version): Utility to assist with common
#               : command line tasks within Ubuntu (22.04)
#
# Author        : dbarber
# Creation Date : 20250502
##########################################################################
import sys
import socket
import subprocess
import time
from datetime import datetime

class LinuxAdminMenu:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.now = datetime.now()
        self.menu_definitions = {
            1: [self.mem_usage, 'Memory Usage'],
            2: [self.cpu_load, 'CPU Load'],
            3: [self.tcp_conn, 'Number of TCP Connections'],
            4: [self.kernel_version, 'Kernel Version'],
            5: [self.check_all, 'Check All'],
            6: [self.rm_old_kernels_dry, 'Remove Old Kernels (dry run - no changes)'],
            7: [self.rm_old_kernels, 'Remove old kernels (for reals!!!)'],
            8: [self.show_ufw_rules, 'Show Raw UFW Rules'],
            9: [self.supported_packages, 'Display Supported/Unsupported Packages (Ubuntu Only)'],
            10: [self.ls_pci, 'Display PCI Components'],
            11: [self.ls_usb, 'Display USB Components'],
            12: [self.recovery_update, 'Update the OS Recovery Partition to the most current version (this will first check if an update exists.)'],
            13: [self.list_module_commands, 'Display a list of module commands'],
            14: [self.sync_time_date, 'Sync the time and date using chronyd'],
            15: [self.ip_address_info, 'Retrieve your server\'s public and private IP address information'],
            16: [self.vmware_networks_status, 'View VMware Networks Status'],
            0: [self.quit, 'Quit']
        }

    def get_style(self):
        self.PURPLE = '\033[95m'
        self.CYAN = '\033[96m'
        self.DARKCYAN = '\033[36m'
        self.BLUE = '\033[94m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        # self.ORANGE = '\033[0,33m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.OFF = '\033[0m'

    def print_menu(self):
        self.get_style() # Initialize style attributes
        subprocess.run('clear', shell=True, executable="/bin/bash")
        header = self.get_header()
        print(header)
        for key in self.menu_definitions.keys():
            formatted_key = f'{key}'
            print(f'{self.DARKCYAN}{self.BOLD}{formatted_key.ljust(4)}{self.OFF}{self.menu_definitions[key][1]}')

    def get_header(self):
        self.get_style()
        return """
{}
{}
{}: {}: {}
{}
{}
        """.format('#' * 70, '#' * 2, f'## {self.DARKCYAN}Linux CLI Administration Assistant{self.OFF}', self.hostname, self.now, '#' * 2, '#' * 70)

    
    def end_task(self):
        input("\n\nPress Enter to return to the main menu.")

    def mem_usage(self):
        print(f'\nMemory usage on {self.hostname} is: \n')
        result = subprocess.run(['free', '-h'], capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def cpu_load(self):
        print(f'\nCPU Load on {self.hostname} is: \n')
        result = subprocess.run(['uptime'], capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def tcp_conn(self):
        print(f'\nNumber of TCP Connections on {self.hostname}: \n')
        command = "cat /proc/net/tcp | grep -v 'uid' | wc -l"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def kernel_version(self):
        print(f'\nKernel Version on {self.hostname} is: \n')
        result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def check_all(self):
        print(f'\nAll checks being run on {self.hostname}: \n')
        self.mem_usage()
        self.cpu_load()
        self.tcp_conn()
        self.kernel_version()

    def rm_old_kernels_dry(self):
        print(f'\nRemoving old Ubuntu kernels (dry run) on {self.hostname}: \n')
        command = "dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r` | cut -f1,2 -d'-' | grep -e [0-9] | grep -P '(image|headers)' | xargs sudo apt --dry-run remove"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def rm_old_kernels(self):
        print(f'\nRemoving old Ubuntu kernels on {self.hostname} (no turning back with this one!!!!): \n')
        command = "dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r` | cut -f1,2 -d'-' | grep -e [0-9] | grep -P '(image|headers)' | xargs sudo apt remove"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def show_ufw_rules(self):
        print(f'\nShowing output of raw UFW Rules on {self.hostname}: \n')
        command = "sudo ufw show raw"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def supported_packages(self):
        print(f'\nDisplaying Supported/Unsupported Packages on {self.hostname}: \n')
        print('Running \'ubuntu-support-status\' with no arguments')
        print('Run ubuntu-support-status with --show-unsupported, --show-supported or --show-all to see more details')
        command = "ubuntu-support-status"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def ls_pci(self):
        print(f'\nDisplaying PCI Components on {self.hostname} (sudo is required): \n')
        print(subprocess.getoutput('lspci'))
        selected_pci_slot = input('\n\n\nEnter device number from above to inspect further (xx:xx.x)? ')
        command = f'lspci -s {selected_pci_slot} -v'
        print(subprocess.getoutput(command))
        self.end_task()

    def ls_usb(self):
        print(f'\nDisplaying USB Components on {self.hostname} (sudo is required): ')
        print(f'\nRun \'lsusb -t\' to view hierarchical tree and view matching module (attached drivers). \n')
        print(subprocess.getoutput('lsusb'))
        selected_usb_slot = input('\n\n\nEnter device number from above to inspect further (xxxx:xxxx)? ')
        command = f'sudo lsusb -v -d {selected_usb_slot}'
        print(subprocess.getoutput(command))
        self.end_task()

    def recovery_update(self):
        print(f'\nUpdating the OS Recovery Partition to the most current version on {self.hostname}: \n')
        command = 'pop-upgrade recovery upgrade from-release'
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def list_module_commands(self):
        print('lsmod | fgrep <module name>')
        print('modinfo <module name> (ex. modinfo nvme)')
        print('modinfo -p <module name> (list only parameters)')
        self.end_task()

    def sync_time_date(self):
        print(f'\nSyncing time and date on {self.hostname}: \n')
        command = "sudo chronyc makestep"
        command2 = subprocess.getoutput('/usr/bin/timedatectl')
        print(f'\nPre-sync date and time:\n{command2}\n')
        print('\nSyncing now...\n')
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        print(f'\nPost-sync date and time:\n{command2}\n')
        self.end_task()

    def ip_address_info(self):
        print(f'\nRetrieving your server\'s public and private IP address information on {self.hostname}: \n')
        command = ["sudo", "bash", "/home/dbarber/Documents/Scripts/Linux_System_Admin_Scripts/ip_address_information.sh"]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def vmware_networks_status(self):
        print(f'\nRetrieving VMware Networks Status on {self.hostname}: \n')
        print('If networks are not starting run \'sudo vmware-netcfg\'.\n')
        command = "sudo vmware-networks --status --verbose"
        result = subprocess.run(command, shell=True, executable="/bin/bash", capture_output=True, text=True)
        print(result.stdout)
        self.end_task()

    def quit(self):
        print('Quitting...\n')
        exit()

    def run(self):
        while True:
            self.print_menu()
            try:
                selection = int(input('\nEnter your choice: '))
            except ValueError:
                print('Wrong input. Please enter a number ...')
                continue
            if selection in self.menu_definitions:
                self.menu_definitions[selection][0]()
            else:
                print(f'Invalid option. Please enter a number between 1 and {len(self.menu_definitions) - 1} or 0 to quit.')
                time.sleep(2)


if __name__ == '__main__':
    menu = LinuxAdminMenu()
    menu.run()