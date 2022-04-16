"""
test on apply predict on new data set from build models
"""

import os
import json as js
import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

data_one_line = {
    "customerID": "7623-TRNQN",
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "Yes",
    "tenure": 1,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Mailed check",
    "MonthlyCharges": 49.9,
    "TotalCharges": "49.9",
}

data_two_lines = {
    "customerID": ["7010-BRBUU", "9688-YGXVR"],
    "gender": ["Male", "Female"],
    "SeniorCitizen": [0, 0],
    "Partner": ["Yes", "No"],
    "Dependents": ["Yes", "No"],
    "tenure": [72, 44],
    "PhoneService": ["Yes", "Yes"],
    "MultipleLines": ["Yes", "No"],
    "InternetService": ["No", "Fiber optic"],
    "OnlineSecurity": ["No internet service", "No"],
    "OnlineBackup": ["No internet service", "Yes"],
    "DeviceProtection": ["No internet service", "Yes"],
    "TechSupport": ["No internet service", "No"],
    "StreamingTV": ["No internet service", "Yes"],
    "StreamingMovies": ["No internet service", "No"],
    "Contract": ["Two year", "Month-to-month"],
    "PaperlessBilling": ["No", "Yes"],
    "PaymentMethod": ["Credit card (automatic)", "Credit card (automatic)"],
    "MonthlyCharges": [24.1, 88.15],
    "TotalCharges": ["1734.65", "3973.2"],
}


# requêtes
r_alice_random_forest_one_line = session.post(
    "http://my_api:8000/random_forest/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": False},
    data=js.dumps({"X_test": data_one_line}),
)

r_alice_gradient_boosting_one_line = session.post(
    "http://my_api:8000/gradient_boosting/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": False},
    data=js.dumps({"X_test": data_one_line}),
)

r_alice_logistic_regression_one_line = session.post(
    "http://my_api:8000/logistic_regression/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": False},
    data=js.dumps({"X_test": data_one_line}),
)


r_alice_random_forest_two_lines = session.post(
    "http://my_api:8000/random_forest/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": True},
    data=js.dumps({"X_test": data_two_lines}),
)

r_alice_gradient_boosting_two_lines = session.post(
    "http://my_api:8000/gradient_boosting/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": True},
    data=js.dumps({"X_test": data_two_lines}),
)

r_alice_logistic_regression_two_lines = session.post(
    "http://my_api:8000/logistic_regression/prediction",
    auth=HTTPBasicAuth("alice", "wonderland"),
    params={"dataset_has_more_than_one_individual": True},
    data=js.dumps({"X_test": data_two_lines}),
)

output = """
============================
    Get predict class
============================

request done at {route}
| username={username}
| password={password}
| params = {params}

predict_class = {predict_class}

"""


predict_class_random_forest_one_line = r_alice_random_forest_one_line.json()
predict_class_gradient_boosting_one_line = r_alice_gradient_boosting_one_line.json()
predict_class_logistic_regression_one_line = r_alice_logistic_regression_one_line.json()

predict_class_random_forest_two_lines = r_alice_random_forest_two_lines.json()
predict_class_gradient_boosting_two_lines = r_alice_gradient_boosting_two_lines.json()
predict_class_logistic_regression_two_lines = (
    r_alice_logistic_regression_two_lines.json()
)

# impression dans un fichier
if os.environ.get("LOG") == str(1):
    with open("logs/api_test_get_predict_test.log", "a", encoding="UTF-8") as file:
        file.write(
            output.format(
                route="/random_forest/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": False},
                predict_class=predict_class_random_forest_one_line,
            )
        )
        file.write(
            output.format(
                route="/gradient_boosting/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": False},
                predict_class=predict_class_gradient_boosting_one_line,
            )
        )
        file.write(
            output.format(
                route="/logistic_regression/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": False},
                predict_class=predict_class_logistic_regression_one_line,
            )
        )
        file.write(
            output.format(
                route="/random_forest/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": True},
                predict_class=predict_class_random_forest_two_lines,
            )
        )
        file.write(
            output.format(
                route="/gradient_boosting/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": True},
                predict_class=predict_class_gradient_boosting_two_lines,
            )
        )
        file.write(
            output.format(
                route="/logistic_regression/score",
                username="alice",
                password="wonderland",
                params={"dataset_has_more_than_one_individual": True},
                predict_class=predict_class_logistic_regression_two_lines,
            )
        )
