# pyAI
A Voice Assistant Tool Created Using Python 

# Overview
I learned this project from YouTube and am regularly enhancing its functionality to make it more enjoyable to use. By adding exciting features and updating the code over time, I aim to create a more interactive experience. 

# Voice Assistant: Zira

Zira is a voice assistant built using Python, capable of performing various tasks through voice commands. It can play music, answer queries, tell jokes, provide weather updates, and more.

## Features

- Voice recognition and text-to-speech capabilities
- Play music on YouTube
- Fetch information from Wikipedia
- Provide weather updates
- Note-taking functionality
- Tell random facts and jokes
- Support for multiple commands

## Requirements

Before running the voice assistant, ensure you have the following packages installed:

- SpeechRecognition
- pyttsx3
- pywhatkit
- wikipedia
- randfacts
- requests
- psutil
- pyjokes
- pyaudio

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/gbdvdgu/pyAI
   cd pyAI
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install these packages from requirements.txt file** 
   ```plaintext
   SpeechRecognition==3.8.1
   pyttsx3==2.90
   pywhatkit==5.4
   wikipedia==1.5.0
   randfacts==0.20
   requests==2.31.0
   psutil==5.9.5
   pyjokes==0.6.0
   pyaudio==0.2.11
   ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   - **Installing PyAudio** (if you encounter issues):
     - **Windows Users**:
       - Download the appropriate `PyAudio` wheel file from [Christoph Gohlke's Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
       - Install the downloaded wheel using:
         ```bash
         pip install PyAudio‑<version>.whl
         ```
     - **macOS Users**:
       ```bash
       brew install portaudio
       pip install pyaudio
       ```
     - **Linux Users**:
       ```bash
       sudo apt-get install portaudio19-dev python3-pyaudio
       pip install pyaudio
       ```

5. **Run the Voice Assistant**:
   ```bash
   python zira.py
   ```

## Usage

Once the voice assistant is running, you can use the following commands:

- **Play Music**: Say "play [song name]" to play a song on YouTube.
- **Tell Time**: Say "time" to get the current time.
- **Tell Date**: Say "date" to get today's date.
- **Check Weather**: Say "temperature" or "weather" to get the current weather in New Delhi.
- **Ask Wikipedia**: Say "what is [topic]" to get a brief summary from Wikipedia.
- **Tell a Joke**: Say "joke" to hear a random joke.
- **Tell a Fact**: Say "fact" to learn a random fact.
- **Take a Note**: Say "note" to write down something.
- **Say Hello**: Say "hello" to get a greeting response.
- **Exit**: Say "exit" to close the assistant.

## Commands Overview

| Command                   | Description                          |
|---------------------------|--------------------------------------|
| `play [song name]`        | Plays the specified song on YouTube. |
| `time`                    | Tells the current time.              |
| `date`                    | Tells today's date.                  |
| `temperature` / `weather` | Provides weather information.        |
| `what is [topic]`         | Searches for the topic on Wikipedia.  |
| `joke`                    | Tells a random joke.                 |
| `fact`                    | Shares a random fact.                |
| `note`                    | Takes a note based on voice input.   |
| `hello`                   | Greets the user.                     |
| `exit`                    | Closes the voice assistant.          |

# What Problems I Am Solving Right Now In This
1. News fucntion not working properly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thank you to the contributors of the libraries used in this project.
- Special thanks to the OpenWeather API for weather data.

## Contact

For any queries or contributions, feel free to reach out to me at [harshcursed@gmail.com].
