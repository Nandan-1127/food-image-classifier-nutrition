# 🍽 Food Image Classifier with Nutrition Analysis

A deep learning based web application that **classifies food images and provides nutritional insights**.
The system uses a **MobileNetV2 convolutional neural network** to identify food items from images and displays **nutrition information and health advice** through a simple Flask web interface.

---

# 📌 Project Overview

This project combines **Computer Vision and Web Development** to create an intelligent food analysis system.

Users can upload an image of food, and the system will:

1. Identify the food item using a trained deep learning model
2. Display the prediction confidence
3. Show nutritional information
4. Provide health suggestions like:

   * Best time to eat
   * Recommended serving
   * Who should avoid it

The project demonstrates the use of:

* Deep Learning
* Transfer Learning
* Image Classification
* Flask Web Applications

---

# 🚀 Features

* 🍕 Classifies **20 different food categories**
* 🧠 Uses **MobileNetV2 transfer learning**
* 📊 Displays **prediction confidence**
* 🥗 Shows **nutritional information**
* 💡 Provides **health recommendations**
* 🌐 Interactive **Flask web interface**
* 📂 Modular project structure

---

# 🧠 Model Architecture

The model is built using **MobileNetV2**, a lightweight deep convolutional neural network designed for efficient image classification.

### Why MobileNetV2?

* Efficient for small datasets
* Pretrained on **ImageNet**
* Faster training
* Good accuracy for image classification tasks

### Model Details

| Component           | Description                     |
| ------------------- | ------------------------------- |
| Base Model          | MobileNetV2                     |
| Input Image Size    | 160 × 160                       |
| Training Method     | Transfer Learning               |
| Base Model Training | Frozen                          |
| Output Layer        | Softmax                         |
| Number of Classes   | 20                              |
| Optimizer           | Adam                            |
| Loss Function       | Sparse Categorical Crossentropy |

### Model Pipeline

1. Image Upload
2. Image Preprocessing
3. Deep Learning Prediction
4. Food Classification
5. Nutrition Data Display

---

# 📊 Dataset

The model was trained on a **custom dataset of 20 food categories**.

### Dataset Details

* **Total Classes:** 20
* **Images per Class:** 200 – 500
* **Total Images:** ~6000+ images
* **Image Size:** Resized to 160 × 160

### Food Categories

* Idli
* Biryani
* Burger
* Cheesecake
* Chole Bhature
* Crispy Chicken
* Donut
* Fries
* Gulab Jamun
* Ice Cream
* Kadai Paneer
* Masala Dosa
* Momos
* Pani Puri
* Pav Bhaji
* Pizza
* Samosa
* Sushi
* Taco
* Vada Pav

### Dataset Structure Used for Training

```
data/raw/combined_dataset/

├── idli
├── biryani
├── burger
├── cheesecake
├── chole_bature
├── crispy_chicken
├── donut
├── fries
├── gulab_jamun
├── ice_cream
├── kadai_paneer
├── masala_dosa
├── momos
├── pani_puri
├── pav_bhaji
├── pizza
├── samosa
├── sushi
├── taco
└── vada_pav
```

Due to GitHub size limitations, the dataset is **not included in this repository**.

---

# 🖥 Web Application

The web application is built using **Flask** and allows users to interact with the trained model.

### Workflow

1. Upload food image
2. Model predicts food category
3. Nutrition information is displayed
4. Health suggestions are shown

---

# 📂 Project Structure

```
food-image-classifier-nutrition
│
├── app.py
├── model_utils.py
├── nutrition.py
├── predict.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models
│   └── food_classifier.h5
│
├── static
│   ├── css
│   │   └── style.css
│   └── uploads
│
├── templates
│   ├── index.html
│   └── result.html
│
├── notebooks
│   └── train_model.py
│
├── data
│   ├── raw
│   └── processed
│
└── screenshots
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Nandan-1127/food-image-classifier-nutrition.git
```

Navigate into the project folder:

```
cd food-image-classifier-nutrition
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 📦 Requirements

Main libraries used in the project:

* TensorFlow
* Flask
* NumPy
* Pillow
* Scikit-learn
* Matplotlib

Install using:

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

Upload a food image and view prediction results.

---


# 🔮 Future Improvements

Possible enhancements for the project:

* Increase dataset size
* Improve model accuracy
* Add more food categories
* Use real-time nutrition APIs
* Deploy the application online
* Add mobile-friendly UI
* Add calorie tracking system

---

# 👨‍💻 Author

Nandan Sunkara
B.Tech Student
Indian Institute of Information Technology Design and Manufacturing Jabalpur(IIITDMJ)

GitHub:
https://github.com/Nandan-1127

---

# ⭐ If You Like This Project

If you found this project useful, please consider giving it a **star ⭐ on GitHub**.
