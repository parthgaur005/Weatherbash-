Weatherbash Weather App

A simple desktop application built with Python and Tkinter to fetch and display current weather information for various locations in India using the OpenWeatherMap API.

Features

GUI Interface: Uses Tkinter for a native desktop look and feel.

Location Selection: Allows users to select a city/state from a predefined list of Indian states and Union Territories via a dropdown (Combobox).

Real-time Data: Fetches the following current weather data:

Weather Climate (e.g., Clear, Clouds)

Weather Description (e.g., overcast clouds)

Temperature (in Celsius)

Pressure (in hPa)

Prerequisites

To run this application, you need Python installed on your system. This app uses the following dependencies:

Python 3.x

requests: For making HTTP requests to the weather API.

tkinter: The standard Python interface to the Tk GUI toolkit (usually included with Python installation).

Installation and Setup

Clone the repository (or save the script):

# If you save the file as weather_app.py
# No cloning needed, just ensure you have the file.


Install the required Python library:

pip install requests


API Key Configuration:
The application uses the OpenWeatherMap API.

⚠️ SECURITY WARNING: The API key is currently hardcoded directly in the script. For best practices and security, you should replace the placeholder key (3daf7fb98ac4f7b004cdd1a86118ca5e) with your own API key obtained from OpenWeatherMap, and ideally, load it from an environment variable rather than storing it directly in the source code.

Usage

Run the script:
Open your terminal or command prompt, navigate to the directory where the file is saved, and execute:

python weather_app.py


(Assuming the file is named weather_app.py)

Use the Application:

The application window will open.

Select a location from the Combobox dropdown menu.

Click the "Done" button.

The weather data will be fetched and displayed in the corresponding labels below.

Code Structure

The application's logic is contained within the data_get() function:

It retrieves the selected city name.

It performs a GET request to the OpenWeatherMap API.

It handles the JSON response, converts the temperature from Kelvin to Celsius, and updates the Tkinter labels with the results.

Contributing

Feel free to suggest improvements, such as:

Adding proper error handling (e.g., catching connection errors or invalid city names).

Implementing a user input field for any city, rather than a fixed list.

Switching the temperature display unit (Fahrenheit/Celsius).

Cleaning up the API key usage for better security.
