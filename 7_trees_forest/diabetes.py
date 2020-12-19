import pandas as pd
import matplotlib.pyplot as plt
import sklearn.tree as sk_tree
import sklearn.model_selection as sk_model_selection
import sklearn.metrics as sk_metrics


plt.figure(figsize=(18, 10))

diabets_df = pd.read_csv(r"https://raw.githubusercontent.com/AndriiLatysh/ml_4/master/data/pima-indians-diabetes.csv")

column_names = diabets_df.columns.values

X = diabets_df[column_names[:-1]]
y = diabets_df[column_names[-1]]

X_train, X_test, y_train, y_test = sk_model_selection.train_test_split(X, y)

diabetes_tree_model = sk_tree.DecisionTreeClassifier()
diabetes_tree_model.fit(X_train, y_train)

tree_y_prediction = diabetes_tree_model.predict(X_test)

print("Accurance: {}".format(sk_metrics.accuracy_score(y_test, tree_y_prediction)))

tree_confusion_matrix = sk_metrics.confusion_matrix(y_test, tree_y_prediction)
print(tree_confusion_matrix)

sk_tree.plot_tree(
    diabetes_tree_model, feature_names=column_names, 
    class_names=["low", "high"], filled=True, rounded=True)
plt.show()
