# Automatic Metin Finder Bot

This repository contains a Python-based bot designed for testing and learning purposes. The bot automates the detection and interaction with "Metin" stones in the game *Metin2*. It leverages computer vision techniques and a deep learning model, trained with Roboflow and implemented using YOLOv8, to identify "Metin" stones on the game screen and automatically interact with them. Additionally, the bot includes features for automating in-game actions, such as key spamming and screenshot capturing.

## Features

- **Metin Detection**: Utilizes a YOLOv8 model trained on custom data via Roboflow to detect and locate "Metin" stones on the game screen.
- **Automated Interaction**: Moves the player character to the detected "Metin" stone and performs a right-click action.
- **Key Spamming**: Continuously presses a specified key (default: 'z') to automate certain in-game actions.
- **Screenshot Capture**: Periodically captures screenshots of the game for debugging or data collection purposes.
- **Multi-threaded Execution**: Runs detection, interaction, and key spamming in separate threads to optimize performance and responsiveness.

## How It Works

### YOLOv8 Model Loading
The bot loads a pre-trained YOLOv8 model (`best.pt`) that has been specifically trained to detect "Metin" stones within the game environment. YOLOv8 (You Only Look Once version 8) is a state-of-the-art object detection model that offers high speed and accuracy, making it ideal for real-time applications like this bot.

### Roboflow for Model Training
The model was trained using Roboflow, a powerful platform for managing and preprocessing datasets for computer vision tasks. Roboflow provides tools to annotate images, generate datasets, and export them in formats compatible with models like YOLOv8. This project utilizes a dataset specifically curated and labeled for detecting "Metin" stones.

### Screenshot Capturing and Detection
The `take_screenshot` function captures the game screen at regular intervals and uses the YOLO model to detect "Metin" stones. The detected locations are processed to find the closest "Metin" stone to the player character.

### Bot Decision Making
The bot calculates the distance between the player character and the detected "Metin" stones. It then moves the character to the closest "Metin" and performs a right-click action to interact with it.

### Automated Key Spamming
A separate thread continuously spams the 'z' key, which can be configured to automate certain actions in the game.

### Multi-threading for Efficiency
The bot uses multi-threading to run detection, interaction, and key spamming functions simultaneously. This ensures that the bot remains responsive and performs actions in real-time.

### Exit Mechanism
The bot continuously runs until the 'q' key is pressed, at which point it safely stops all threads and exits.

### Precision Demonstration
A screenshot is included in this repository, showcasing the bot’s precision when detecting and interacting with "Metin" stones. This image, found in the repository, illustrates the output of the `ImagePrediction.py` script, demonstrating how accurately the model identifies and locates the "Metin" within the game screen.

## File Overview

- **RunBot.py**: The main bot script that handles detection, interaction, and key spamming.
- **screenshots.py**: A script for capturing screenshots at regular intervals and saving them to the local file system.
- **ImagePrediction.py**: A script to test the YOLO model on individual images, with a screenshot provided to demonstrate "Metin" detection accuracy.
- **requirements.txt**: A list of all the Python dependencies required to run the bot.

## Requirements

- Python 3.8 or later
- Dependencies listed in `requirements.txt`

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/RautuA/Automatic-Metin-Finder-Bot
   cd automatic-metin-finder-bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python RunBot.py
   ```

5. To start capturing screenshots:
   ```bash
   python screenshots.py
   ```

The bot will run until you press the 'q' key.

## Important Notice

This project is intended solely for testing and learning purposes. It is not meant for use in a live game environment and should not be deployed in a manner that violates any game's terms of service. This project is meant only for testing YOLOv8.
