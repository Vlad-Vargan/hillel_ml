import pandas as pd
import matplotlib.pyplot as plt
import double_grade_svm_utility as svm_utility
import sklearn.svm as sk_svm

qualifications_double_grade = pd.read_csv("8_class/data/double_grade_small.csv")

X = qualifications_double_grade[["technical_grade", "english_grade"]]
y = qualifications_double_grade["qualifies"]

svm_utility.plot_values(qualifications_double_grade)

svm_hard_linear_classifier = sk_svm.SVC(kernel="linear")
svm_hard_linear_classifier.fit(X, y)

svm_utility.plot_model(svm_hard_linear_classifier)

plt.show()