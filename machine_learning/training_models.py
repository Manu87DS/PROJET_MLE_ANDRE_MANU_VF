import pandas as pd
from pretraitement import prepare_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import pickle

raw_data_churn = pd.read_csv("data/churn.csv")

y_raw = raw_data_churn["Churn"]
X_raw = raw_data_churn.drop(["Churn"], axis=1)

X_train_raw, X_test_raw, y_train_raw, y_test_raw = train_test_split(
    X_raw, y_raw, train_size=0.7, test_size=0.3, stratify=y_raw, random_state=42
)

data_test_raw = pd.concat([X_test_raw, y_test_raw], axis=1)
data_test_raw.to_csv("data/test.csv", index=False)

raw_data_train = pd.concat([X_train_raw, y_train_raw], axis=1)
final_data_train = prepare_data(raw_data=raw_data_train)

y_train = final_data_train["Churn"]
X_train = final_data_train.drop(["Churn"], axis=1)


model_logistic_regression = LogisticRegression().fit(X_train, y_train)

model_gradient_boosting = GradientBoostingClassifier().fit(X_train, y_train)

model_random_forest = RandomForestClassifier().fit(X_train, y_train)

with open("trained_models/model_logistic_regression.pkl", "wb") as model_file:
    pickle.dump(model_logistic_regression, model_file)

with open("trained_models/model_gradient_boosting.pkl", "wb") as model_file:
    pickle.dump(model_gradient_boosting, model_file)

with open("trained_models/model_random_forest.pkl", "wb") as model_file:
    pickle.dump(model_random_forest, model_file)
