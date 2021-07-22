# GUI to run NEW ERA NE-500 OEM One Channel Syringe Pumps

## About the Project

These programs provide a GUI to run New Era NE-500 OEM One Channel Syringe Pumps in Python. The interface includes the ability to set both syringe size and forward/reverse flow, pump labeling, pump priming, and the ability to easily stop or update flow settings.  

This code was originally written in the Abate Lab at UC San Francisco by Phil Romero. It was resurrected by John Halliburton for use with Python 3 and updated into its present form by Kevin Joslin and Sakshi Shah while rotating in the Clark lab. We hope you find it useful. Versions for Py2.7 and Qt4 can be found at https://github.com/RomeroLab/syringe-pump-controller. 

### Built With

* [Python](https://www.python.org/)
* [PyQt5](https://pypi.org/project/PyQt5/)

## Getting Started

This software has only been tested on PC desktops running Windows 10. Any adaptations to other operating systems will need to be done by the user. The following workflow will assume you have a PC desktop running Windows 10. We are currently working on creating a standalone Windows application for the pump programs, but we can only demonstrate the use of running the GUI through Python code at this time.

### Prerequisites

* [Anaconda](https://www.anaconda.com/)

We recommend that you use Anaconda to install the latest version of Python 3 as well for installing required packages. Detailed instructions for installing Anaconda on windows can be found [here](https://docs.anaconda.com/anaconda/install/windows/). In most cases you will be installing the 64-Bit Graphical Installer. We recommend that you do **not** check "Add Anaconda3 to my PATH environmental variable" at this time. Once you have Anaconda downloaded and installed you can proceed to the installation of the programs.

### Installation

1. Installing [PyQt5](https://pypi.org/project/PyQt5/)
   - **Note**: If you installed Anaconda then PyQt should already be within your usable packages and there is no need to install PyQt5 separately. If this is the case you may skip this step. If not, execute the following steps to install PyQt5.
     - Open *Anaconda Prompt* as administrator 
       - Right click Anaconda Prompt and select **Run as Administrator >** **Yes**
     - Enter the command
       ```sh
       conda install -c anaconda PyQt5
       ```
     - If prompt enter “**y**” to proceed with the installation
2. Installing [Pyserial](https://pythonhosted.org/pyserial/index.html) (we use version 3.4)
   - Open *Anaconda Prompt* as administrator 
     - Right click Anaconda Prompt and select **Run as Administrator >** **Yes**
   - Enter the command
     ```sh
     conda install -c anaconda pyserial
     ```
   - If prompted enter “**y**” to proceed with the installation
3. Download the Pump Program Files from GitHub
   - Navigate to the GitHub page [here](https://github.com/ClarkLabUCB/NewEraPumps_Python3)
   - Click the green button that says **Code** and select **Download ZIP**
   - Download and extract the file and move it into your documents or destination of choice.

## Usage

Python code (.py files) will not be executable from Windows File Explorer unless you add Python to the PATH. This can be a tricky process, and we will not go into it. Instead, it is best to either execute the program from the *Anaconda Prompt*, by creating a Windows batch file (.bat), or by creating a standalone app with *pyinstaller* The batch file and *pysinstaller* approach will be outlined in the [Alternative Execution Methods](#alternative-execution-methods) section. 

* To run from the *Anaconda Prompt*
  * Open *Anaconda Prompt*
  * Navigate to your current folder run the pump_control3.py code (example)
    ```sh
    cd C:\User\YourUserName\Documents\PumpProgram3
    python pump_control3.py
    ```

## Alternative Execution Methods

### Create a Batch File to Run a Python Script

A batch file is a file that will execute execute whatever script is written within it in the Windows command prompt. This can be used to create a file that will run the code necessary to launch the python script for the pump program. 

1. Locate the address of the activate.bat that activates the anaconda directory. This should be in the Scripts folder within the Anaconda3 folder on your computer. You may need to click view, then check “Hidden Items” in the Show/hide tab. An example location of this is: 
   ```sh
      C:\Users\YourUserName\anaconda3\Scripts\activate.bat
   ```
	Or
   ```sh
      C:\ProgramData\Anaconda3\Scripts\activate.bat
   ```
2. Locate the address of the folder that the pump control execution .py file **pump_control3.py** is located
3. Open the *Notepad* app on Windows
4. On the first line **call** the Anaconda activate.bat file, on the second line, use the command **cd** and to change the directory to the folder address, and on the third line run the pump control program with python pump_control3.py. An example looks like this:
   ```sh
      call C:\Users\YourUserName\anaconda3\Scripts\activate.bat
	   cd C:\User\YourUserName\Documents\PumpProgram3
	   Python pump_control3.py
   ```
 5. When you have written those three lines, and those three lines only. Select **File > Save As**
 6. In the **Save** menu select **Save as Type > ALL Files**
 7. Name your batch file whatever you want, like Run_pump_control.bat, as long as it ends in ".bat"
    - **Note:** It is the .bat extension that will save this file as a Windows Batch file that will run those commands in the windows prompt. The first line changes the windows prompt to the anaconda prompt, the second line changes the directory to your pump program folder location, and the last line runs the pump program.
8. Double clicking this .bat file from any location should run the commands and open the pump program. You can now just leave this .bat on the desktop for you to click whenever you want to run the pump control program.

### Create an Executable Program on your Machine with Pyinstaller
If you have found that these programs work with your pumps and are connected to your COM port of choice, then feel free to create an executable program of the pump program on your machine by following these steps:
- Install [Pyinstaller](https://www.pyinstaller.org/#) (we used version 3.6)
  - Open *Anaconda Prompt* as administrator as outlined above
    - Enter the command
      ```sh
      conda install -c pyinstaller
      ```
    - If prompted enter “**y**” to proceed with the installation
- Reopen *Anaconda Prompt* as administrator
- Navigate to the current directory of the pump programs (both new_era3.py and pump_control3.py must be in this folder) with the **cd** command. An example looks like this:
  ```sh
  cd C:\User\YourUserName\Documents\PumpProgram3
  ```
- Execute the following line of code to create an executable Windows application (.exe file) for the pump program
  ```sh
  pyinstaller pump_control3.py
  ```
- This will create a bundle in a subfolder named **dist**, which will contain the executable application named pump_control3.exe. This app can then be used to run pumps on any computer without the need of Python or any of the packages. **Please be warned that you will need to use the same COM port that you used in the code when you created the app with pyinstaller.**


