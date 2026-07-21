import os
import glob
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# ==========================================
# STEP 1: PATH CONFIGURATION & COMBINE DATA
# ==========================================
print("📦 Finding and combining dataset pieces from data folder...")
MODEL_DIR = "models"

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# This looks into ALL folders and subfolders inside 'data' for any CSV files
csv_files = glob.glob("data/**/*.csv", recursive=True)
if not csv_files:
    print("❌ Error: No dataset files found in 'data/asl_alphabet_test/'!")
    exit()

# Read and combine only the files that are NOT empty
df_list = []
for file in csv_files:
    if os.path.getsize(file) > 0:
        try:
            temp_df = pd.read_csv(file)
            if not temp_df.empty:
                df_list.append(temp_df)
        except Exception as e:
            print(f"⚠️ Skipping corrupted file {file}: {e}")

if not df_list:
    print("❌ Error: All found CSV files were empty!")
    exit()

df = pd.concat(df_list, ignore_index=True)
print(f"✅ Combined {len(df_list)} files successfully! Total Rows: {df.shape[0]}, Columns: {df.shape[1]}")


# ==========================================
# STEP 2: SEPARATE FEATURES AND TARGETS
# ==========================================
X = df.drop(columns=['label'])
y = df['label']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


# ==========================================
# STEP 3: TRAIN-TEST SPLIT
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)


# ==========================================
# STEP 4: MODEL TRAINING
# ==========================================
from sklearn.ensemble import RandomForestClassifier

# Initialize a strong model
model = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42)
model.fit(X_train, y_train)


# ==========================================
# STEP 5: EVALUATION
# ==========================================
y_pred = model.predict(X_test)
print(f"\n✨ Validation Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred, labels=range(len(label_encoder.classes_)), target_names=label_encoder.classes_, zero_division=0))

# ==========================================
# STEP 6: EXPORT ARTIFACTS
# ==========================================
print("💾 Saving files to 'models/' directory...")
with open(os.path.join(MODEL_DIR, "sign_model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "wb") as f:
    pickle.dump(label_encoder, f)

# Save confusion matrix matrix chart
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_, cmap='Blues')
plt.title('SignBridge Performance Matrix')
plt.savefig(os.path.join(MODEL_DIR, "confusion_matrix.png"))

print("🎉 Training process fully finished!")