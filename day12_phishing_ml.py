from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd


print("=" * 65)
print("       DAY 12 - PHISHING EMAIL DETECTION WITH ML")
print("=" * 65)


# ============================================================
# 50-SAMPLE DATASET
# 1 = PHISHING
# 0 = LEGITIMATE
# ============================================================

phishing_emails = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Urgent update your bank details",
    "Your account has been locked verify now",
    "Confirm your password immediately",
    "Security alert verify your account",
    "Your payment failed click the link",
    "Urgent login required to restore account",
    "Claim your reward now",
    "Update your banking information immediately",
    "Verify your PayPal account",
    "Your account will be closed today",
    "Click here to verify your identity",
    "Urgent security verification required",
    "You have won a prize click here",
    "Confirm your billing information",
    "Your password expires today verify now",
    "Unusual activity detected login immediately",
    "Update your account details urgently",
    "Click the link to avoid account suspension",
    "Immediate action required verify your security account",
    "Your online banking access needs urgent verification",
    "Confirm your account information to prevent suspension",
    "Security warning click the verification link now",
    "Your payment account requires immediate confirmation"
]

legitimate_emails = [
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Meeting notes from yesterday",
    "Please find the project report attached",
    "The team meeting is scheduled for tomorrow",
    "Here is the monthly sales report",
    "Please review the attached document",
    "Your appointment is scheduled for Monday",
    "The project deadline has been extended",
    "Please attend the department meeting",
    "The training session starts at 10am",
    "Here are the minutes from today's meeting",
    "Please submit your assignment by Friday",
    "The office will remain closed on Sunday",
    "Your leave request has been approved",
    "The quarterly report is ready",
    "Please review the presentation",
    "The team lunch is scheduled for Friday",
    "Your document has been received",
    "Please check the updated project schedule",
    "Please review the agenda before the team meeting",
    "The project documentation has been updated",
    "Your monthly statement is available for review",
    "Please attend the scheduled training session",
    "The development team shared the latest project update"
]


# Combine the two classes
emails = phishing_emails + legitimate_emails
labels = [1] * len(phishing_emails) + [0] * len(legitimate_emails)


# ============================================================
# DATASET VALIDATION
# ============================================================

print("\nDataset Information")
print("-" * 65)
print("Total emails :", len(emails))
print("Phishing     :", len(phishing_emails))
print("Legitimate   :", len(legitimate_emails))

if len(emails) != len(labels):
    raise ValueError(
        f"Dataset error: {len(emails)} emails but {len(labels)} labels"
    )

print("Dataset validation : PASSED")


# ============================================================
# DATAFRAME
# ============================================================

data = pd.DataFrame({
    "email": emails,
    "label": labels
})


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)


# ============================================================
# NAIVE BAYES MODEL
# ============================================================

model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])


print("\nTraining Naive Bayes model...")

model.fit(X_train, y_train)

print("Training complete.")


# ============================================================
# MODEL EVALUATION
# ============================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Performance")
print("-" * 65)
print(f"Training samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")
print(f"Accuracy         : {accuracy * 100:.2f}%")


# ============================================================
# CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix")
print("-" * 65)
print(cm)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report")
print("-" * 65)

print(
    classification_report(
        y_test,
        predictions,
        target_names=["Legitimate", "Phishing"],
        zero_division=0
    )
)


# ============================================================
# CUSTOM TEST EMAILS
# ============================================================

test_emails = [
    "Please verify your PayPal login",
    "Meeting notes from yesterday",
    "Urgent update your bank account",
    "Please review the project report"
]

print("\nCustom Email Predictions")
print("-" * 65)

for email in test_emails:

    prediction = model.predict([email])[0]

    result = "PHISHING" if prediction == 1 else "LEGITIMATE"

    print(f"{result:10} : {email}")


# ============================================================
# SAVE RESULTS
# ============================================================

results = {
    "total_dataset": len(data),
    "phishing_samples": len(phishing_emails),
    "legitimate_samples": len(legitimate_emails),
    "training_samples": len(X_train),
    "testing_samples": len(X_test),
    "accuracy": round(accuracy * 100, 2),
    "confusion_matrix": cm.tolist()
}

pd.DataFrame([results]).to_csv(
    "day12_ml_results.csv",
    index=False
)

print("\nResults saved to: day12_ml_results.csv")

print("=" * 65)
print("                 ANALYSIS COMPLETE")
print("=" * 65)