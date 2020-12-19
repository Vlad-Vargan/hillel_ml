import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as sk_linear_models
import sklearn.metrics as sk_metrics


qualifies_single_grade = pd.read_csv(r'https://raw.githubusercontent.com/AndriiLatysh/ml_4/master/data/single_grade.csv')
qualifies_single_grade.sort_values(by=["grade", "qualifies"], inplace=True)

X = qualifies_single_grade[["grade"]]
y = qualifies_single_grade["qualifies"]
plt.scatter(X, y)

qualification_model = sk_linear_models.LogisticRegression()
qualification_model.fit(X, y)

modeled_qualification = qualification_model.predict(X)
modeled_qualification_probability = qualification_model.predict_proba(X)[:, 1]

qualifies_single_grade["modeled probability"] = modeled_qualification_probability
print(qualifies_single_grade)

plt.plot(X, modeled_qualification, color="k")
plt.plot(X, modeled_qualification_probability, color="g")

confusion_matrix = sk_metrics.confusion_matrix(y, modeled_qualification)
print(confusion_matrix)

print(f"Accuracy: {sk_metrics.accuracy_score(y, modeled_qualification)}")
print(f"Recall: {sk_metrics.recall_score(y, modeled_qualification)}")
print(f"Precision: {sk_metrics.precision_score(y, modeled_qualification)}")
print(f"Error: {1 - sk_metrics.accuracy_score(y, modeled_qualification)}")




plt.show()
