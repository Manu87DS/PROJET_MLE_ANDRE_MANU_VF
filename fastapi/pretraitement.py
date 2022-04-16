import pandas as pd
from fastapi import HTTPException


def prepare_data(raw_data, y=True):
    """ """

    try:
        all_variables = list(raw_data.columns)
        already_managed_variables = [
            "customerID",
            "SeniorCitizen",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
        ]
        if y:
            already_managed_variables.append("Churn")
        variables_to_transform_into_binary = list(
            set(all_variables) - set(already_managed_variables)
        )

        df_with_var_to_encode = raw_data[variables_to_transform_into_binary]
        clean_data = pd.get_dummies(
            df_with_var_to_encode, prefix=list(df_with_var_to_encode.columns)
        )

        variables_to_add = [
            "SeniorCitizen",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
        ]
        if y:
            variables_to_add.append("Churn")
        final_data = pd.concat(
            [
                clean_data,
                raw_data[variables_to_add],
            ],
            axis=1,
        )
        final_data["TotalCharges"] = pd.to_numeric(
            final_data.TotalCharges, errors="coerce"
        )
        final_data.dropna(subset=["TotalCharges"], inplace=True)
        return final_data
    except Exception as e:
        print(f"probleme dans les donnees")
        print(e)


def predict_class(new_data, dataset_has_more_than_one_individual, X_test, model):
    try:
        if dataset_has_more_than_one_individual:
            try:
                x_test = new_data.X_test
                x_test = pd.DataFrame(x_test)
                new_index = list(len(X_test) + x_test.index)
                x_test.index = new_index
                x_test = prepare_data(x_test, y=False)
                x_test = x_test.merge(X_test, how="left")
                x_test.fillna(0, inplace=True)
                predict_class = model.predict(x_test)
                return list(predict_class)

            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
        else:
            try:
                x_test = new_data.X_test
                x_test = pd.DataFrame(x_test, index=[len(X_test)])
                x_test = prepare_data(x_test, y=False)
                x_test = x_test.merge(X_test, how="left")
                x_test.fillna(0, inplace=True)
                predict_class = model.predict(x_test)
                return str(predict_class)
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
