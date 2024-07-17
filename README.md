# Capstone-Project
In this project we have used Selenium to scrap the data from the Redbus website and used MySql for storing the scrapted data, we have done Data Analysis/Filtering using Streamlit and displayed the filtered data for the user. 


**Pre-Requisites**
1. Ensure You Have Python and pip Installed

    First, make sure you have Python installed on your system. You can check this by running:

       python --version
   
2. pip is usually installed automatically with Python. You can check its version by running:

        pip --version
3. Install Selenium using pip

    Once Python and pip are installed, you can install Selenium by running the following command in your terminal or command prompt:

         pip install selenium

4. Install Mysql using pip:

      Download MySQL Installer:

               MySQL Installation
               Download MySQL Installer:
               
               Visit the MySQL Community Downloads page.
               Select the appropriate MySQL Community Server version for your operating system (e.g., Windows, macOS, Linux).
               Download the installer package.
               Run the Installer:
               
               Windows:
               
               MySQL Installation
               Download MySQL Installer:
               
               Visit the MySQL Community Downloads page.
               Select the appropriate MySQL Community Server version for your operating system (e.g., Windows, macOS, Linux).
               Download the installer package.
               Run the Installer:
               
               Windows:
               
               Double-click the downloaded installer (.msi file).
               Follow the prompts in the MySQL Installer wizard.
               During installation, you'll be prompted to choose components to install (MySQL Server, MySQL Workbench, etc.). Select MySQL Server and any other components you need.
               Set up a root password when prompted. Remember this password, as it will be required to access MySQL.
               Complete the installation process.
               
               macOS:
               
               Download the macOS DMG file from the MySQL Community Downloads page.
               Double-click the DMG file to open it.
               Drag the MySQL installer package to the Applications folder.
               Open the MySQL installer package and follow the prompts to install MySQL Server.
               Set up a root password when prompted.
               Follow any additional instructions provided during installation.

               Linux:

               On Linux systems, MySQL can often be installed using the package manager specific to your distribution (e.g., apt for Ubuntu/Debian, yum for CentOS/RHEL).

5. Install mysql.connector:

      You can install mysql.connector using pip, which is the recommended package installer for Python:

         pip install mysql-connector-python

6. Install StreamLit using pip

       pip install streamlit
   
7. Running Your Streamlit App:

   To run your Streamlit app, use the following command in your terminal or command prompt:

          streamlit run app.py

**Clone the repository**

Using the below command to clone the project:

        git clone https:https://github.com/harivelmurugan15/Capstone-Project.git cd {file path}


Once you coloned the repository and installed the prerequistes you are ready to go,follow the below steps:
                 
                 1. Update the 'hostname','username','password','database name'(If created) on the SQL Handeling.py file,streamlit_demo.py file,Clear databse.py.
                 
                 2. Run the SQL Handeling.py file - This will call the web_scrapping.py and scrap the data redbus appilication and store it in your database.
                 
                 3. Run the streamlit application and Use filter to obtain the required data.
                 
                 4. Always clear the database by running Clear databse.py which will clear all the data and ready the database for the future use.
   
