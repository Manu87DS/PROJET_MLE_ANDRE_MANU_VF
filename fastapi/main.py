import pickle
from pickletools import anyobject
import secrets
import pandas as pd
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from pretraitement import prepare_data, predict_class

with open("model_logistic_regression.pkl", "rb") as model_file:
    model_logistic_regression = pickle.load(model_file)

with open("model_gradient_boosting.pkl", "rb") as model_file:
    model_gradient_boosting = pickle.load(model_file)

with open("model_random_forest.pkl", "rb") as model_file:
    model_random_forest = pickle.load(model_file)

data_test = pd.read_csv("test.csv")

final_data_test = prepare_data(raw_data=data_test)

y_test = final_data_test["Churn"]
X_test = final_data_test.drop(["Churn"], axis=1)


users = {"alice": "wonderland", "bob": "builder", "clementine": "mandarine"}

api = FastAPI(
    title="My API",
    description="API that builds score dectection churn.",
    version="1.0.0",
)

security = HTTPBasic()


def get_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = credentials.username in users.keys()

    if not correct_username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user",
            headers={"WWW-Authenticate": "Basic"},
        )

    correct_password = secrets.compare_digest(
        credentials.password, users[credentials.username]
    )
    if not correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials


class NewData(BaseModel):
    X_test: dict


@api.get("/status", name="status")
def get_status():
    return 1


@api.get("/", name="Welcome")
def get_index():
    """
    - Returns greetings
    - Explains the goal of the API
    - Explains how to access to others API's roads
    """
    return {
        "Greeting": "Welcome !",
        "Goal": "This API is used to build score to detect customer's churn",
        "Info": "To access to others API's road, you need to create an account. Please go check the API's doc to have more informations",
    }


@api.get("/random_forest/score", tags=["model score on test data"])
def get_random_forest_score(
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    score_rf = model_random_forest.score(X_test, y_test)
    return score_rf


@api.get("/gradient_boosting/score", tags=["model score on test data"])
def get_gradient_boosting_score(
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    score_gb = model_gradient_boosting.score(X_test, y_test)
    return score_gb


@api.get("/logistic_regression/score", tags=["model score on test data"])
def get_logistic_regression_score(
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    score_lr = model_logistic_regression.score(X_test, y_test)
    return score_lr


@api.post("/random_forest/prediction", tags=["apply predict on new dataset"])
def get_random_forest_prediction(
    new_data: NewData,
    dataset_has_more_than_one_individual: bool,
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    predict_classe = predict_class(
        new_data=new_data,
        dataset_has_more_than_one_individual=dataset_has_more_than_one_individual,
        X_test=X_test,
        model=model_random_forest,
    )
    return predict_classe


@api.post("/gradient_boosting/prediction", tags=["apply predict on new dataset"])
def get_gradient_boosting_prediction(
    new_data: NewData,
    dataset_has_more_than_one_individual: bool,
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    predict_classe = predict_class(
        new_data=new_data,
        dataset_has_more_than_one_individual=dataset_has_more_than_one_individual,
        X_test=X_test,
        model=model_gradient_boosting,
    )
    return predict_classe


@api.post("/logistic_regression/prediction", tags=["apply predict on new dataset"])
def get_logistic_regression_prediction(
    new_data: NewData,
    dataset_has_more_than_one_individual: bool,
    credentials: HTTPBasicCredentials = Depends(get_credentials),
):
    predict_classe = predict_class(
        new_data=new_data,
        dataset_has_more_than_one_individual=dataset_has_more_than_one_individual,
        X_test=X_test,
        model=model_logistic_regression,
    )
    return predict_classe
