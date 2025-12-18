# Gesture Controlled Chrome Dino Game

A real time hand gesture based controller for the Chrome Dino game using computer vision.
The game can be played hands free, without using a keyboard or mouse.

## Overview

This project uses a webcam to detect hand gestures and maps finger movements to game actions in real time.
MediaPipe is used for accurate hand landmark detection, while OpenCV handles video processing.
Virtual key events are sent to the browser to control the Dino game seamlessly.

## Features

- Touch free gameplay using hand gestures
- Start the game by pointing the index finger
- Jump by moving the finger upward
- Duck by moving the finger downward
- Smooth gesture detection with minimal jitter
- Low latency real time performance
- No modification to the Chrome Dino game required

## Tech Stack

- Python
- OpenCV
- MediaPipe Hands
- PyAutoGUI
- NumPy

## Project Structure

```
gesture-dino-controller/
├── src/
│   └── gesture_dino.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sidharthprem310/TouchlessDinoRunner.git
cd TouchlessDinoRunner
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the Chrome Dino game

- Open Google Chrome
- Navigate to chrome://dino
- Or disconnect from the internet and refresh a tab

Ensure the Dino game window remains focused while playing.

### 4. Run the application

```bash
python src/gesture_dino.py
```

Press Q to exit the application.

## Gesture Mapping

| Gesture | Action |
|------|------|
| Index finger pointed | Start game |
| Finger moves upward | Jump |
| Finger moves downward | Duck |
| Neutral position | No action |

## How It Works

1. Webcam captures live video frames
2. MediaPipe detects 21 hand landmarks in real time
3. Index finger vertical movement is tracked
4. Temporal smoothing reduces noise and jitter
5. Gesture actions are mapped to virtual key presses
6. The Chrome Dino game responds instantly

## Performance Notes

- Works best at 30 to 60 FPS
- Good lighting improves detection accuracy
- Single hand tracking is used for low latency
- Webcam resolution is optimized for real time processing

## Limitations

- Requires local execution on a personal computer
- Chrome window must stay in focus
- Full game control is not supported on Google Colab due to system restrictions

## Future Enhancements

- Automatic gameplay mode
- Dynamic gesture threshold adaptation
- Multi gesture support
- Score tracking and performance metrics
- Cross platform gesture control for other games

## License

This project is licensed under the MIT License.
