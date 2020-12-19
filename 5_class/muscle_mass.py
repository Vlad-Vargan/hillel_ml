import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as sk_preprocessing
import sklearn.linear_model as sk_linear_model



muscle_mass_df = pd.read_csv("7_class/data/muscle_mass.csv")
muscle_mass_df.sort_values(by="training_time", inplace=True)
# muscle_mass_df.sort_values(by="muscle_mass", inplace=True)


X = muscle_mass_df[["training_time"]]
y = muscle_mass_df[["muscle_mass"]]

plt.scatter(X, y, label="muscle")
plt.xlabel("training_time")
plt.ylabel("muscle_mass")

polynomial_transformer = sk_preprocessing.PolynomialFeatures(degree=5)
X_transformer = polynomial_transformer.fit_transform(X)
print(X_transformer)

muscle_mass_model = sk_linear_model.LinearRegression()
muscle_mass_model.fit(X_transformer, y)

print(muscle_mass_model.coef_)
print(muscle_mass_model.intercept_)


modeled_muscle_mass = muscle_mass_model.predict(X_transformer)
plt.plot(X, modeled_muscle_mass, color="r")

plt.show()
