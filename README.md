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

## How to get best.pt from roboflow?
To get the `best.pt` model file for YOLOv8 using **Roboflow** for dataset management, follow this detailed step-by-step guide:

---


#### Prerequisites

1. **Roboflow Account**  
   - If you don’t have a Roboflow account, sign up at [Roboflow.com](https://roboflow.com/).
   - Roboflow simplifies dataset annotation, preparation, and export for use with machine learning models like YOLOv8.

2. **Install YOLOv8 and Other Dependencies**  
   Install YOLOv8 and its dependencies via the `ultralytics` package:
   ```bash
   pip install ultralytics
   ```

---

### Step 1: Upload and Annotate Your Dataset on Roboflow

1. **Upload Your Dataset**  
   - Go to the [Roboflow dashboard](https://app.roboflow.com/).
   - Click on **Create New Project** and choose the type of model you’re building (e.g., "Object Detection").
   - Upload your images and, if you already have them, upload your annotations. If you don’t have annotations yet, you can label them using Roboflow’s labeling tools.

2. **Annotate (if needed)**  
   - If your dataset is not annotated, Roboflow provides an interface where you can manually draw bounding boxes around objects in your images and assign classes to them.

3. **Organize Dataset**  
   After uploading and annotating, Roboflow organizes the dataset into training, validation, and test sets. It automatically splits your dataset (e.g., 70% training, 20% validation, 10% test). You can customize this split as needed.

---

### Step 2: Export Dataset in YOLOv8 Format

1. **Generate Dataset Version**  
   - After organizing and splitting your dataset, click **Generate** to create a new dataset version.
   
2. **Export in YOLOv8 Format**  
   - Once the dataset is generated, click **Export**.
   - In the format dropdown, select **YOLOv8 PyTorch**.
   - Choose the image resolution you prefer (e.g., `640x640`), which is the input size for YOLO.
   - Download the dataset export link, or copy the download code snippet (useful if you want to download the dataset directly to your training machine).

   You will get a code snippet like this:
   ```bash
   !curl -L "https://universe.roboflow.com/dataset-name/download/yolov8" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
   ```

---

### Step 3: Download the Dataset for Training

1. **Prepare the Dataset**  
   - Run the command (shown above) to download the dataset directly to your working directory. This will unzip the dataset into folders with images and corresponding label files in YOLO format.

   The folder structure will look like this:
   ```
   dataset/
   ├── train/
   │   ├── images/
   │   └── labels/
   ├── valid/
   │   ├── images/
   │   └── labels/
   └── data.yaml
   ```

   The `data.yaml` file, which Roboflow provides, includes:
   - The number of classes (`nc`).
   - The paths to the training and validation sets.
   - The list of class names.

---

### Step 4: Train YOLOv8 Model

1. **Launch YOLOv8 Training**  
   Now you are ready to train your YOLOv8 model. Use the command below to start training:
   ```bash
   yolo task=detect mode=train data=path/to/data.yaml model=yolov8n.pt epochs=100 imgsz=640
   ```
   
   **Explanation of the command:**
   - `task=detect`: Indicates this is an object detection task.
   - `mode=train`: Specifies the mode to train the model.
   - `data=path/to/data.yaml`: Path to the `data.yaml` file in the dataset.
   - `model=yolov8n.pt`: The base YOLOv8 model to start with (`yolov8n.pt` for YOLOv8 Nano, adjust as needed for small, medium, large models).
   - `epochs=100`: Number of epochs for training (you can adjust this).
   - `imgsz=640`: Size of input images (can adjust based on your dataset size).

2. **Training Logs**  
   As training progresses, you’ll see the model’s performance metrics, such as training/validation losses, mAP (mean average precision), and more, displayed in the console.

---

### Step 5: Retrieve the `best.pt` File

1. **Locate the `best.pt` File**  
   Upon completion of training, YOLOv8 saves the model checkpoints in the `runs/train/exp/` directory (the folder name might increment if you run multiple experiments like `exp1`, `exp2`, etc.).

   - **`best.pt`**: This is the model checkpoint with the best performance on the validation set during training.
   - **`last.pt`**: This is the model checkpoint from the final epoch.

   The file will be located here:
   ```
   runs/train/exp/best.pt
   ```

2. **Using `best.pt` for Inference or Fine-Tuning**  
   Once you have the `best.pt` model, you can use it for inference (detecting objects in new images) or continue fine-tuning. For inference, you can run:
   ```bash
   yolo task=detect mode=predict model=runs/train/exp/best.pt source=path/to/image.jpg
   ```

---


## Important Notice

This project is intended solely for testing and learning purposes. It is not meant for use in a live game environment and should not be deployed in a manner that violates any game's terms of service. This project is meant only for testing YOLOv8.
