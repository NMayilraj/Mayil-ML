from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assuming you have two datasets with text and labels: old_data_text, old_data_labels

# Combine the datasets if needed
old_data_text = old_data_text_1 + old_data_text_2
old_data_labels = old_data_labels_1 + old_data_labels_2

# Convert text data to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(old_data_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, old_data_labels, test_size=0.2, random_state=42)

# Choose a model (Logistic Regression in this case)
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on the test set: {accuracy}")

# Now, you can use the trained model to predict new text
new_text = ["This is a new text."]
new_text_features = vectorizer.transform(new_text)
prediction = model.predict(new_text_features)
print(f"Predicted class for the new text: {prediction}")
