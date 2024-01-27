# Rain-alert-application
This Python project is a Rain Alert Application that utilizes OpenWeatherMap API to fetch weather data and Twilio API for sending SMS alerts. The application checks the forecast and sends a notification if rain is expected.

Features

    Weather Forecast: Utilizes OpenWeatherMap API to get the weather forecast data.

    Rain Alert: Sends an SMS alert using Twilio if rain is expected in the specified location.

    Customizable Location: The user can customize the location by providing latitude and longitude coordinates.

Prerequisites

    OpenWeatherMap API Key: Obtain a free API key from OpenWeatherMap to access weather data.

    Twilio Account: Sign up for a Twilio account to get the Account SID, Auth Token, and a Twilio phone number for sending SMS.

How to Use

    Clone the repository to your local machine.

    bash

    git clone https://github.com/rohanindaragi/Rain-alert-application.git

    Install the required Python libraries.

    bash

    pip install requests twilio

    Set up your API keys and Twilio credentials.

    Replace your_openweathermap_api_key with your OpenWeatherMap API key in the api_key variable.
    Replace your_twilio_account_sid, your_twilio_auth_token, and your_twilio_phone_number with your Twilio credentials.

    Run the Python script.

    bash

    python rain_alert.py

    Receive SMS alerts when rain is expected!

Contributing

    Contributions are welcome! If you have any ideas, bug fixes, or improvements, feel free to open an issue or create a pull request.
License

    This project is licensed under the MIT License
