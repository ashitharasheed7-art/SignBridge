import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
import pickle
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from collections import Counter  # 🧠 Added for prediction smoothing

# ==========================================
# STEP 1: LOAD TRAINED ARTIFACTS
# ==========================================
MODEL_PATH = "models/sign_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
    print("❌ Error: Model or Label Encoder files not found in 'models/' folder!")
    print("💡 Please run 'python train.py' first to generate these files.")
    exit()

print("💬 Loading trained SignBridge model...")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

# ==========================================
# STEP 2: INITIALIZE WEBCAM & DETECTOR
# ==========================================
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2, detectionCon=0.8)

# 🔄 History queue to smooth out predictions (last 5 frames)
prediction_history = []

print("🎥 Webcam started! Press 'q' on your keyboard to exit.")

while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to grab frame from camera.")
        break

    # Find hands
    hands, img = detector.findHands(img, draw=True)

    # Initialize empty slots for 2 hands (63 coordinates each = 126 total features)
    hand1_features = np.zeros(63)
    hand2_features = np.zeros(63)

    if hands:
        for i, hand in enumerate(hands):
            lmList = hand["lmList"]  # List of 21 [x, y, z] landmarks
            
            # 🛠️ LANDMARK NORMALIZATION (Matches your new create_dataset.py)
            wrist = lmList[0]
            normalized_lm = []
            for lm in lmList:
                normalized_lm.append(lm[0] - wrist[0])  # Relative X
                normalized_lm.append(lm[1] - wrist[1])  # Relative Y
                normalized_lm.append(lm[2] - wrist[2])  # Relative Z
            
            flat_landmarks = np.array(normalized_lm)

            if i == 0:
                hand1_features = flat_landmarks
            elif i == 1:
                hand2_features = flat_landmarks

        # Concatenate features to hit exactly 126 features expected by the model
        features = np.concatenate([hand1_features, hand2_features]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)

        # Decode the raw instant prediction and confidence
        raw_label = label_encoder.inverse_transform(prediction)[0]
        confidence = np.max(prediction_proba) * 100

        # 🔄 Add current prediction to history queue
        prediction_history.append(raw_label)
        if len(prediction_history) > 5:
            prediction_history.pop(0)

        # 🧠 Get the most common prediction over the last 5 frames (Filters flickering!)
        predicted_label = Counter(prediction_history).most_common(1)[0][0]

        # 🛠️ FORCE PRINT TO THE TERMINAL
        print(f"🔮 Live Analysis -> Predicted: {predicted_label} (Instant: {raw_label}) | Confidence: {confidence:.2f}%")

        # Display on webcam window if confidence passes the filter
        if confidence > 40:  # Set to a comfortable 40% now that normalization improves reliability
            display_text = f"Sign: {predicted_label} ({confidence:.1f}%)"
            
            # Draw visual indicator box onto frame
            cv2.rectangle(img, (20, 20), (400, 75), (0, 128, 0), cv2.FILLED)
            cv2.putText(img, display_text, (35, 55), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (255, 255, 255), 2, cv2.LINE_AA)

    # Show live image
    cv2.imshow("SignBridge Live Inference", img)

    # Press 'q' to shut down window safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()