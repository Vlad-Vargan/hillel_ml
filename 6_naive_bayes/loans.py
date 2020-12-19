import pandas as pd
import sklearn.naive_bayes as sk_naive_bayes


def convert_to_numeric_values(df):
    covnerted_df = df.copy()
    covnerted_df = covnerted_df.replace(
        {
            "history": {"bad": 0, "fair": 1, "excellent": 2},
            "income": {"low": 0, "high": 1},
            "term": {3: 0, 10: 1},
            "risk": {"low": 0, "high": 1}
        }
    )
    return covnerted_df


loans_df = pd.read_csv("9_class/data/loans.csv")
numeric_loans_df = convert_to_numeric_values(loans_df)

print(numeric_loans_df)

feature_names = loans_df.columns.values[:-1]
X = numeric_loans_df[feature_names]
y = numeric_loans_df["risk"]

naive_bayes_model = sk_naive_bayes.CategoricalNB()
naive_bayes_model.fit(X, y)

X_probalities = naive_bayes_model.predict_proba(X)[:,1]
X_probalities_log = naive_bayes_model.predict_log_proba(X)[:,1]

loans_df["probability"] = X_probalities
loans_df["log_probability"] = X_probalities_log

print(loans_df)

