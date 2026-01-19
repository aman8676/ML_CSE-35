# =====================================
# IMPORT LIBRARIES
# =====================================
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


# =====================================
# LOAD DATASET
# =====================================
df = pd.read_csv("cancer_reg.csv")

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

print(df.head())


# =====================================
# CREATE CLASSIFICATION TARGET (NUMERIC)
# =====================================
df["death_rate_class"] = pd.qcut(
    df["target_deathrate"],
    q=3,
    labels=False   # <<< IMPORTANT FIX
)

# =====================================
# SELECT ONLY NUMERIC FEATURES
# =====================================
X = df.select_dtypes(include=[np.number]).drop(
    ["target_deathrate", "death_rate_class"], axis=1
)
y = df["death_rate_class"]


# =====================================
# TRAIN–TEST SPLIT (60% TRAIN)
# =====================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    train_size=0.6,
    random_state=42,
    stratify=y
)


# =====================================
# FEATURE SCALING (FOR KNN)
# =====================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# =====================================
# KNN CLASSIFIER
# =====================================
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train_scaled, y_train)
knn_pred = knn.predict(X_test_scaled)

print("\nKNN Accuracy:", accuracy_score(y_test, knn_pred))
print("KNN Confusion Matrix:\n", confusion_matrix(y_test, knn_pred))


# =====================================
# DECISION TREE CLASSIFIER
# =====================================
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

print("\nDecision Tree Accuracy:", accuracy_score(y_test, dt_pred))
print("Decision Tree Confusion Matrix:\n", confusion_matrix(y_test, dt_pred))


# =====================================
# NAIVE BAYES CLASSIFIER
# =====================================
nb = GaussianNB()
nb.fit(X_train, y_train)
nb_pred = nb.predict(X_test)

print("\nNaive Bayes Accuracy:", accuracy_score(y_test, nb_pred))
print("Naive Bayes Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))


# =====================================
# FINAL COMPARISON
# =====================================
print("\n====== FINAL MODEL COMPARISON ======")
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))
print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_pred))
