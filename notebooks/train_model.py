import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.utils import image_dataset_from_directory
import os

# -----------------------------
# CONFIG
# -----------------------------
DATASET_PATH = "data/raw/combined_dataset"
IMG_SIZE = (160, 160)
BATCH_SIZE = 32
EPOCHS = 5

# -----------------------------
# LOAD DATASET
# -----------------------------
print("Loading dataset...")

dataset = image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

class_names = dataset.class_names
num_classes = len(class_names)

print("Classes:", class_names)
print("Total batches:", len(dataset))

# -----------------------------
# SPLIT TRAIN / VALIDATION
# -----------------------------
dataset_size = len(dataset)
train_size = int(0.8 * dataset_size)

train_dataset = dataset.take(train_size)
val_dataset = dataset.skip(train_size)

print("Training batches:", len(train_dataset))
print("Validation batches:", len(val_dataset))

# Prefetch for performance
AUTOTUNE = tf.data.AUTOTUNE
train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
val_dataset = val_dataset.prefetch(buffer_size=AUTOTUNE)

# -----------------------------
# BUILD MODEL
# -----------------------------
print("Building model...")

base_model = MobileNetV2(
    input_shape=(160, 160, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False  # Freeze base layers

model = models.Sequential([
    layers.Rescaling(1./127.5, offset=-1),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Build model explicitly before summary
model.build(input_shape=(None, 160, 160, 3))
model.summary()

# -----------------------------
# TRAIN MODEL
# -----------------------------
print("Starting training...")

history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS
)

# -----------------------------
# SAVE MODEL
# -----------------------------
os.makedirs("models", exist_ok=True)
model.save("models/food_classifier.h5")

print("Model saved successfully!")