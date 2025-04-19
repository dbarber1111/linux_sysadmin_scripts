#!/usr/bin/python3
##########################################################################
# Scriptname    : linux_admin_menu.py
# Description   : Linux CLI Administration Assistant: Utility to assist with common
#               : command line tasks within Ubuntu (22.04)
#
# Author        : dbarber
# Creation Date : 20240306
##########################################################################
# Revision History: 
##########################################################################
import sys
import socket
import subprocess
import time
from datetime import datetime


now = datetime.now()
hostname = socket.gethostname()

# Style Class
class style:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   # ORANGE = '\033[0,33m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   OFF = '\033[0m'


# def command(param):
#    result = subprocess.run(), stdout=subprocess.PIPE


header = """
{}
{}
{}: {}: {}
{}
{}
""".format('#'*70, '#'*2, f'## {style.DARKCYAN}Linux CLI Administration Assistant{style.OFF}', hostname,  now, '#'*2, '#'*70)


def print_menu():
    subprocess.run('clear', shell=True, executable="/bin/bash")
    print(header)
    for key in menu_definitions.keys():
        formatted_key = f'{key}'
        print(style.DARKCYAN + formatted_key.ljust(4) + style.OFF + menu_definitions[key][1] )


def endTask():
    print(input("\n\nPress Enter to return to the main menu."))
    # time.sleep(10)


def memUsage():
    print(f'\nMemory usage on {hostname} is: \n')
    result = subprocess.run(['free', '-h'])
    result.stdout
    endTask()


def cpuLoad():
    print(f'\nCPU Load on {hostname} is: \n')
    result = subprocess.run(['uptime'])
    result.stdout
    endTask()


def tcpConn():
    print(f'\nNumber of TCP Connections on {hostname}: \n')
    command = "cat  /proc/net/tcp | grep -v 'uid' | wc -l"
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    endTask()


def kernelVersion():
    print(f'\nCPU Load on {hostname} is: \n')
    result = subprocess.run(['uname', '-r'])
    result.stdout
    endTask()


def checkAll():
    print(f'\nAll checks being run on {hostname}: \n')
    memUsage()
    cpuLoad()
    tcpConn()
    kernelVersion()


def rmOldKernelsDry():
    print(f'\nRemoving old Ubuntu kernels (dry run) on {hostname}: \n')
    command = "dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r` | cut -f1,2 -d'-' | grep -e [0-9] | grep -P '(image|headers)' | xargs sudo apt --dry-run remove"
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    endTask()


def rmOldKernels():
    print(f'\nRemoving old Ubuntu kernels on {hostname} (no turning back with this one!!!!): \n')
    command = "dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r` | cut -f1,2 -d"-"` | grep -e [0-9] | grep -P '(image|headers)' | xargs sudo apt remove"
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    endTask()


def showUfwRules():
    print(f'\nShowing ouput of raw UFW Rules on {hostname}: \n')
    command = "sudo ufw show raw"
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    endTask()


def supportedPackages():
    print(f'\nDisplaying Supported/Unsupported Packages on {hostname}: \n')
    print('Running \'ubuntu-support-status\' with no arguments')
    print('Run ubuntu-support-status with --show-unsupported, --show-supported or --show-all to see more details')
    command = "ubuntu-support-status"
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    endTask()


def lsPci():
    print(f'\nDisplaying PCI Components on {hostname} (sudo is required): \n')
    print(subprocess.getoutput('lspci'))
    selected_pci_slot = input('\n\n\nEnter device number from above to inspect further (xx:xx.x)? ')
    command = f'lspci -s {selected_pci_slot} -v'
    print(subprocess.getoutput(command))
    endTask()


def lsUsb():
    print(f'\nDisplaying USB Components on {hostname} (sudo is required): ')
    print(f'\nRun \'lsusb -t\' to view hierarchical tree and view matching module (attached drivers). \n')
    print(subprocess.getoutput('lsusb'))
    selected_usb_slot = input('\n\n\nEnter device number from above to inspect further (xxxx:xxxx)? ')
    command = f'sudo lsusb -v -d {selected_usb_slot}'
    print(subprocess.getoutput(command))    
    print("")
    time.sleep(50)


def recoveryUpdate():
    print(f'\nUpdating the OS Recovery Partition to the most current version on {hostname}: \n')
    command = 'pop-upgrade recovery upgrade from-release'
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout   
    endTask()


def listModuleCommands():
    print('lsmod | fgrep <module name>')
    print('modinfo <module name> (ex. modinfo nvme)')
    print('modinfo -p <module name> (list only parameters)')
    endTask()


def syncTimeDate():
    print(f'\nSyncing time and date on {hostname}: \n')
    command = "sudo chronyc makestep"
    command2 = subprocess.getoutput('/usr/bin/timedatectl')
    print(f'\nPre-sync date and time:\n{command2}\n')
    print('\nSyncing now...\n')
    result = subprocess.run(command, shell=True, executable="/bin/bash")
    result.stdout
    print(f'\nPost-sync date and time:\n{command2}\n')
    endTask()


def ipAddressInfo():
    print(f'\nRetrieving your server\'s public and private IP address information on {hostname}: \n')
    command = ["sudo", "bash", "/home/dbarber/Documents/Scripts/Linux_System_Admin_Scripts/ip_address_information.sh"]
    result = subprocess.run(command)
    result.stdout   
    endTask()


def quit():
    print('Quitting...\n')
    exit()


def imposter_syndrome(type, value, traceback):
    print("I am a bad coder ☹️")
    print(f"{type} error has occurred, the value: {value}, and you can see traceback: {traceback}")


menu_definitions = {
    1 : [memUsage, 'Memory Usage'],
    2 : [cpuLoad, 'CPU Load'],
    3 : [tcpConn, 'Number of TCP Connections'],
    4 : [kernelVersion, 'Kernel Version'],
    5 : [checkAll, 'Check All'],
    6 : [rmOldKernelsDry, 'Remove Old Kernels (dry run - no changes)'],
    7 : [rmOldKernels, 'Remove old kernels (for reals!!!)'],
    8 : [showUfwRules, 'Show Raw UFW Rules'],
    9 : [supportedPackages, 'Display Supported/Unsupported Packages (Ubuntu Only)'],
    10: [lsPci, 'Display PCI Components'],
    11: [lsUsb, 'Display USB Components ()'],
    12: [recoveryUpdate, 'Update the OS Recovery Partition to the most current version (this will first check if an update exist.)'],
    13: [listModuleCommands, 'Display a list of module commands'],
    14: [syncTimeDate, 'Sync the time and date using chronyd'],
    15: [ipAddressInfo, 'Retrieve your server\'s public and private IP address information'],
    0 : [quit, 'Quit']
}


if __name__=='__main__':
    while(True):
        print_menu()
        try:
            selection = int(input('\nEnter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
            sys.excepthook = imposter_syndrome
        if selection <= len(menu_definitions) - 1:
            menu_definitions[selection][0]()
        else:
            print(f'{style.RED} Invalid option. Please enter a number between 1 and {len(menu_definitions) - 1} or 0 to quit.{style.OFF}')
            time.sleep(10)
        