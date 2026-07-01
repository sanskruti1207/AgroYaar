import os
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Ensure directories exist
os.makedirs('model', exist_ok=True)
os.makedirs('static/uploads', exist_ok=True)

print("Starting asset generation...")

# -------------------------------------------------------------
# 1. Generate Crop Recommendation Model (Scikit-Learn Classifier)
# -------------------------------------------------------------
print("Training Maharashtra Crop Recommendation Model...")

# Define districts and talukas covering all regions of Maharashtra
districts_talukas = {
    'Pune': ['Haveli', 'Baramati', 'Indapur', 'Shirur', 'Khed', 'Junnar', 'Maval'],
    'Nashik': ['Nashik', 'Niphad', 'Yeola', 'Sinnar', 'Malegaon', 'Kalwan', 'Baglan'],
    'Nagpur': ['Nagpur', 'Saoner', 'Katol', 'Kalmeshwar', 'Ramtek', 'Umred'],
    'Kolhapur': ['Karveer', 'Hatkanangle', 'Shirol', 'Radhanagari', 'Kagal', 'Gadhinglaj'],
    'Jalgaon': ['Jalgaon', 'Bhusawal', 'Yawal', 'Raver', 'Pachora', 'Chalisgaon'],
    'Latur': ['Latur', 'Udgir', 'Nilanga', 'Ausa', 'Renapur', 'Ahmedpur'],
    'Ratnagiri': ['Ratnagiri', 'Lanja', 'Rajapur', 'Sangameshwar', 'Chiplun', 'Guhagar'],
    'Aurangabad': ['Aurangabad', 'Paithan', 'Gangapur', 'Vaijapur', 'Kannad', 'Sillod']
}

all_districts = list(districts_talukas.keys())
all_talukas = []
for taluka_list in districts_talukas.values():
    all_talukas.extend(taluka_list)

soils = ['Clayey', 'Sandy', 'Loamy', 'Black Cotton', 'Red Soil', 'Alluvial']
seasons = ['Kharif', 'Rabi', 'Summer']
crops = ['Tomato', 'Potato', 'Rice', 'Maize', 'Cotton', 'Sugarcane', 'Soybean']

# Programmatically generate expanded Maharashtra dataset
X_data = []
y_data = []

for dist, t_list in districts_talukas.items():
    for t in t_list:
        for s in soils:
            for se in seasons:
                # Custom regional crop logic based on actual crop behaviors in Maharashtra
                if dist == 'Ratnagiri': # Konkan - high rain
                    crop = 'Rice' if se == 'Kharif' else 'Tomato'
                elif dist == 'Kolhapur': # Western Maharashtra - Sugarcane belt
                    if s in ['Black Cotton', 'Clayey']:
                        crop = 'Sugarcane'
                    else:
                        crop = 'Soybean' if se == 'Kharif' else ('Maize' if se == 'Rabi' else 'Tomato')
                elif dist == 'Jalgaon': # Khandesh - Cotton
                    if s in ['Black Cotton', 'Clayey'] and se == 'Kharif':
                        crop = 'Cotton'
                    else:
                        crop = 'Maize' if se == 'Rabi' else ('Tomato' if se == 'Summer' else 'Soybean')
                elif dist == 'Latur': # Marathwada - Soybean
                    crop = 'Soybean' if se == 'Kharif' else ('Maize' if se == 'Rabi' else 'Tomato')
                elif dist == 'Nagpur': # Vidarbha - Cotton/Soybean
                    if s in ['Black Cotton', 'Clayey'] and se == 'Kharif':
                        crop = 'Cotton'
                    else:
                        crop = 'Soybean' if se == 'Kharif' else ('Maize' if se == 'Rabi' else 'Tomato')
                elif dist == 'Nashik': # Western Maharashtra - Potato/Tomato
                    if s in ['Loamy', 'Alluvial'] and se == 'Rabi':
                        crop = 'Potato'
                    else:
                        crop = 'Tomato' if se in ['Summer', 'Kharif'] else 'Maize'
                else: # Pune and others
                    if se == 'Kharif':
                        crop = 'Rice' if s in ['Loamy', 'Alluvial'] else 'Soybean'
                    elif se == 'Rabi':
                        crop = 'Potato' if s in ['Loamy', 'Alluvial'] else 'Sugarcane'
                    else:
                        crop = 'Tomato'
                
                X_data.append([dist, t, s, se])
                y_data.append(crop)

# Create and fit LabelEncoders
le_d = LabelEncoder().fit(all_districts)
le_t = LabelEncoder().fit(all_talukas)
le_s = LabelEncoder().fit(soils)
le_se = LabelEncoder().fit(seasons)
le_y = LabelEncoder().fit(crops)

X_encoded = np.array([
    [
        le_d.transform([x[0]])[0],
        le_t.transform([x[1]])[0],
        le_s.transform([x[2]])[0],
        le_se.transform([x[3]])[0]
    ]
    for x in X_data
])
y_encoded = le_y.transform(y_data)

# Fit classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_encoded, y_encoded)

# Save classifier and encoders
recommender_payload = {
    'model': clf,
    'encoder_district': le_d,
    'encoder_taluka': le_t,
    'encoder_soil': le_s,
    'encoder_season': le_se,
    'encoder_crop': le_y
}

with open('model/model.pkl', 'wb') as f:
    pickle.dump(recommender_payload, f)
print("Crop Recommendation model successfully saved to model/model.pkl.")

# -------------------------------------------------------------
# 2. Generate Disease Detection Model (TensorFlow/Keras CNN)
# -------------------------------------------------------------
print("Compiling TensorFlow/Keras Disease Model...")
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

class_names = [
    'tomato_early_blight', 'tomato_late_blight', 'tomato_leaf_mold', 
    'tomato_septoria_leaf_spot', 'tomato_yellow_leaf_curl_virus', 'tomato_healthy',
    'potato_early_blight', 'potato_late_blight', 'potato_healthy',
    'rice_brown_spot', 'rice_leaf_blast', 'rice_bacterial_leaf_blight', 'rice_healthy',
    'maize_common_rust', 'maize_gray_leaf_spot', 'maize_northern_leaf_blight', 'maize_healthy',
    'cotton_fusarium_wilt', 'cotton_leaf_curl', 'cotton_bacterial_blight', 'cotton_healthy',
    'sugarcane_red_rot', 'sugarcane_smut', 'sugarcane_yellow_leaf', 'sugarcane_healthy',
    'soybean_rust', 'soybean_downy_mildew', 'soybean_frogeye_leaf_spot', 'soybean_healthy'
]

model = Sequential([
    Conv2D(8, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(len(class_names), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.save('model/disease_model.h5')
print("TensorFlow model successfully saved to model/disease_model.h5.")

with open('model/class_names.pkl', 'wb') as f:
    pickle.dump(class_names, f)
print("Class names successfully saved to model/class_names.pkl.")

print("All assets successfully generated!")
