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

### Running the Scripts

Python code (.py files) will not be executable from Windows File Explorer unless you add Python to the PATH. This can be a tricky process, and we will not go into it. Instead, it is best to either execute the program from the *Anaconda Prompt*, by creating a Windows batch file (.bat), or by creating a standalone app with *pyinstaller*. The batch file and *pysinstaller* approach will be outlined in the [Alternative Execution Methods](#alternative-execution-methods) section. 

* To run from the *Anaconda Prompt*
  * Open *Anaconda Prompt*
  * Navigate to your current folder run the pump_control3.py code (example)
    ```sh
    cd C:\User\YourUserName\Documents\PumpProgram3
    python pump_control3.py
    ```
### Setting up the Pump(s)

#### Setting the COM port Number

The pumps need to be tethered together with ethernet cables which will eventually terminate into a COM port in the computer. Determine what COM port your pumps are connected to the computer with by opening the *Device Manager* on Windows. When you are positive of the COM port number that your devices are connected to the computer with, you will need to open both the pump_control3.py script and then set_pump_number3.py script and change the COM port number to that number. For example if your COM port number is **COM1**, then the line of code in the scripts that sets the COM port number should look like this: 
   ```sh
   serial_port = 'COM1'
   ```
#### Setting Individual Pump Numbers
    
While it is common in many applications to tether pumps together, the pump program requires that each of the pumps be named a unique single digit integer (0-9). Perform the following steps to name each pump:
1. Make sure that only one pump is connected to the computer
2. Run the **set_pump_number3.py** script, a windows command prompt will open and show you the current pump number assigned to the pump.
3. Enter a new pump number (0-9)
4. The program will assign the new pump number to the pump and confirm the new pump number.
5. Press enter to close the pump program
6. Label the pump with a piece of tape or a label maker so that you know which pump number is assigned to that pump from now on.
7. Repeat steps 1-6 with every pump, ensuring that you use a unique integer for every pump. 

It is probably most helpful to label to the pumps 1,2,3,4,5... and so on. At this time, the pump assignment script can only label the pumps with an integer 0-9, so if you have more than 10 pumps tethered together you will have to edit the script yourself.

### Using the Pump GUI

An overview of the Pump GUI is shown below. For every pump tethered into the system., a line appears with a drop down menu to select for a 1 mL, 3mL, 5 mL, or 10 mL syringe, an editable field to name the contents of the pump, an editable field to input a nominal (positive or negative integer) flowrate, a drop down menu to choose between units of uL/hr and mL/hour, its nominal current flow rate, the units of the current flow rate, and a **Prime** button, which will set the flow rate of that pump to 10,000 uL/hour. If the pump has a positive flow rate (out of the syringe), the flow will be shown as positive, if the pump has a negative flow rate (into the syringe), the flow will be shown as negative. At the top of the GUI are the **Run/Update** button and the **Stop** button. **Run/Update** will set the the flow rates of the connected pumps to the user-sepecified flowrates, **Stop** will set the flow rates of all pumps to 0. **IMPORTANT** In order to change the syringe size or units you need to **Stop** all pumps, then change the syringe size or units and then press **Run/Update** again. You **CANNOT** simply change the syringe size/units and press **Run/Update**. 

#### Assign Pump Fluid Names
Assign pump fluid names by clicking the edit field next pump and entering the name of the pump fluid (e.g. oil, buffer, etc.)

#### Change the Flow Rate

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

Double clicking this .bat file from any location should run the commands and open the pump program. You can now just leave this .bat on the desktop for you to click whenever you want to run the pump control program.

### Create an Executable Program on your Machine with Pyinstaller
If you have found that these programs work with your pumps and are connected to your COM port of choice, then feel free to create an executable program of the pump program on your machine by following these steps:
1. Install [Pyinstaller](https://www.pyinstaller.org/#) (we used version 3.6)
2. Open *Anaconda Prompt* as administrator as outlined above
   - Enter the command
     ```sh
     conda install -c pyinstaller
     ```
   - If prompted enter “**y**” to proceed with the installation
3. Reopen *Anaconda Prompt* as administrator
4. Navigate to the current directory of the pump programs (both new_era3.py and pump_control3.py must be in this folder) with the **cd** command. An example looks like this:
  ```sh
  cd C:\User\YourUserName\Documents\PumpProgram3
  ```
5. Execute the following line of code to create an executable Windows application (.exe file) for the pump program
  ```sh
  pyinstaller pump_control3.py
  ```
  
This will create a bundle in a subfolder named **dist**, which will contain the executable application named pump_control3.exe. This app can then be used to run pumps on any computer without the need of Python or any of the packages. **Please be warned that you will need to use the same COM port that you used in the code when you created the app with pyinstaller.**


