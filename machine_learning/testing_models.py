import pickle
import pandas as pd
from pretraitement import prepare_data

data_test = pd.read_csv("data/test.csv")

final_data_test = prepare_data(raw_data=data_test)

y_test = final_data_test["Churn"]
X_test = final_data_test.drop(["Churn"], axis=1)


with open("trained_models/model_logistic_regression.pkl", "rb") as model_file:
    model_logistic_regression = pickle.load(model_file)

with open("trained_models/model_gradient_boosting.pkl", "rb") as model_file:
    model_gradient_boosting = pickle.load(model_file)

with open("trained_models/model_random_forest.pkl", "rb") as model_file:
    model_random_forest = pickle.load(model_file)


pred_lr = model_logistic_regression.predict(X_test)
score_lr = model_logistic_regression.score(X_test, y_test)

pred_gb = model_gradient_boosting.predict(X_test)
score_gb = model_gradient_boosting.score(X_test, y_test)

pred_rf = model_random_forest.predict(X_test)
score_rf = model_random_forest.score(X_test, y_test)

print({"score_lr" : score_lr, "score_gb" : score_gb, "score_rf" : score_rf})
