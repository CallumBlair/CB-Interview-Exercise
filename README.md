# Callum Blair
## _Met Office interview Exercise_

Pre-Interview Coding Exercise for the Junior DevOps Engineer (Tech01295) graduate Dev Ops role.
This exercise includes two solutions:

- A local solution
- A cloud based solution

##  Cloning the repository and initial setup

To use this application please clone the repository by navigating to your chosen folder and using:
```sh
git clone https://github.com/CallumBlair/CB-Interview-Exercise.git
```
Please ensure you have [Python](https://www.python.org/) setup on your machine.
**Library Installation**
Please ensure you have the requests module installed.
This can be done in a command prompt window after installing Python by running:
```
pip install requests
```
## Using the local solution
> Navigate to the: `/LocalVersion` folder.

If you have a personal IDE please open the localApp.py file in your personal IDE, or IDLE which may be included in your Python installation.
Otherwise please navigate to the given folder in Command Prompt and use the following command to run the application:
```
python localApp.py
```
You will be prompted for your API key, please type this and press enter.
Following this you will be prompted for your city choice.
The application will request the information from the API and save it in the /LocalVersion folder in the minMaxTemperatures.JSON file.
If an error with the key occurs the following message will be displayed in the console:
```
Access forbidden - please check the entered key
```
Please check your API access key and re-run the application
## Using the cloud based solution
> Navigate to the repository root folder.

If you have a personal IDE please open the localApp.py file in your personal IDE, or IDLE which may be included in your Python installation.
Otherwise please navigate to the given folder in Command Prompt and use the following command to run the application:
```
python client.py
```
You will be prompted for your city choice, please type this and press enter.
The application will request the information from the Cloud API and save it in the repository root folder in the minMaxTemperatures.JSON file.

**Cloud based funtionality**
The cloud function utilises a GitHub continuous deployment pipeline which deploy the contents of the Server folder to Google App Engine.
This improves the security of the application by storing the given API access key as a GitHub secret, which is then deployed to the Google App Engine instance as an Enviroment Variable.
The local client application fires a request to the App Engine deployment which then uses the key to request the information from the given API before returning it to the original client.


