import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# ==============================
# Configuration
# ==============================
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

JUMP_THRESHOLD = 25
DUCK_THRESHOLD = 25

SMOOTHING_FRAMES = 5
ACTION_COOLDOWN = 0.3

# ==============================
# MediaPipe Initialization
# ==============================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# ==============================
# Webcam Setup
# ==============================
cap = cv2.VideoCapture(CAMERA_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# ==============================
# Runtime Variables
# ==============================
y_history = []
reference_y = None
last_action_time = 0
game_started = False

# ==============================
# Helper Functions
# ==============================
def cooldown_over():
    return time.time() - last_action_time > ACTION_COOLDOWN

def smooth(history, value):
    history.append(value)
    if len(history) > SMOOTHING_FRAMES:
        history.pop(0)
    return int(np.mean(history))

# ==============================
# Main Loop
# ==============================
print("Gesture Dino Controller Running")
print("Point index finger to start")
print("Move finger up to jump, down to duck")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]

        h, w, _ = frame.shape
        index_tip = hand.landmark[8]
        index_base = hand.landmark[5]

        index_y = int(index_tip.y * h)
        base_y = int(index_base.y * h)

        smooth_y = smooth(y_history, index_y)

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        cv2.circle(frame, (int(index_tip.x * w), smooth_y), 8, (0, 255, 0), -1)

        finger_extended = abs(index_y - base_y) > 40

        if not game_started and finger_extended:
            pyautogui.press("space")
            game_started = True
            reference_y = smooth_y
            last_action_time = time.time()

        if game_started and reference_y is not None and cooldown_over():
            delta_y = smooth_y - reference_y

            if delta_y < -JUMP_THRESHOLD:
                pyautogui.press("space")
                last_action_time = time.time()
                cv2.putText(frame, "JUMP", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif delta_y > DUCK_THRESHOLD:
                pyautogui.keyDown("down")
                time.sleep(0.1)
                pyautogui.keyUp("down")
                last_action_time = time.time()
                cv2.putText(frame, "DUCK", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Gesture Dino Controller", frame)

    if cv2.waitKey(1) & 0xFF in [ord("q"), ord("Q")]:
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
