# Linux Sysadmin Scripts

This project contains scripts to assist with common command line tasks within Ubuntu (22.04).

## Files

### linux_admin_menu.py

This file contains the original script that performs various Linux administration tasks using procedural programming. It includes functions for checking memory usage, CPU load, TCP connections, kernel version, and more.

### linux_admin_menu_ai.py

This file contains the object-oriented version of the original script. It defines a class `LinuxAdminMenu` that encapsulates all the functionality of the original script. The class includes methods for each task and manages the menu and user interactions.

## Features

- Memory Usage: Displays current memory usage on the system.
- CPU Load: Shows the current CPU load.
- TCP Connections: Lists the number of TCP connections.
- Kernel Version: Displays the current kernel version.
- Remove Old Kernels: Options for dry run and actual removal of old kernels.
- Show UFW Rules: Displays raw UFW rules.
- Supported Packages: Shows supported and unsupported packages.
- Display PCI and USB Components: Lists hardware components and allows for further inspection.
- Sync Time and Date: Syncs the system time using chronyd.
- VMware Networks Status: Retrieves the status of VMware networks.

## Usage

To run the object-oriented version of the script, execute `linux_admin_menu_ai.py` using Python 3. Ensure you have the necessary permissions for certain tasks that require `sudo`.

```bash
python3 linux_admin_menu_ai.py
```

Follow the on-screen prompts to navigate through the menu and select the desired tasks
