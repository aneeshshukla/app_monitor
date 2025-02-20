# <p align="center">**Instruction**</p>
# Getting Started

## 1. Install Python

Before using App Tracker, you'll need to install Python.  
- [Here is a link to the Python downloads page.](https://www.python.org/downloads)  
- [Here is a helpful guide to installing Python on various operating systems.](https://wiki.python.org/moin/BeginnersGuide/Download)
> [!TIP]
> *Later in this guide, you will use the Package Installer for Python (pip), which may require you to add Python to your system PATH.<br/>(See image below for reference)*
<br/>

![win_installer](https://github.com/user-attachments/assets/f49fde3b-f940-41d5-a1ee-4fdad125a611)<br/>
> [!NOTE]
> Image shown maybe of a older version but you will have the same option for your version.


## 2. Install Python Packages using *pip*

  1. Open run dialog by pressing `Win` + `R` on your keyboard.
  2. Write `cmd` and press `Enter` key on your keyboard. This will open Command Prompt.
  3. Write command
     ```
     pip install pynput
     ```
  5. Rest of the packages should be pre-installed, else you need to install them too like in step 3.
     
     List of required packages:
       - `time`
       - `datetime`
       - `win32gui`
       - `os`
       - `pynput`
       - `threading`
## 3. Download *App_Monitor* file
  
  1. Goto file -> <a href='https://github.com/aneeshshukla/app_monitor/blob/main/app_tracker%20(no%20console%20app).pyw'>Click here</a>.
  2. Click on *Download Raw File* button.<br/>
     ![download](/docs/images/download.png)
  3. Save the file in your desired location.
## 4. Create File Shortcut
  1. `Right Click` on the file, then click `Create shortcut`.<br/>
     If you can't see the option, then click on `show more option` and then on `Create shortcut`.<br/>
## 5. Make the file run on startup
  1. Open run dialog by pressing `Win` + `R` on your keyboard.
  2. Write the following path and press `Enter` key on your keyboard. This will open `Startup folder`.
     ```
     %appdata%\Microsoft\Windows\Start Menu\Programs\Startup
     ```
  3. Move the created shortcut file here.


___
<br>

# Accessing the *app_log* file

1. Open the `Documents` folder.
2. Find the file named `app_usage_log_[YYYY-MM-DD]`.
3. There you have it

> [!NOTE]
> By default the *app_log* file will be saved in `Documents` folder.
> You can change it by changing the file path in the main file.
>   Change the file path on line `48` and line `71`.

___
<br>
