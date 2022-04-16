import pandas as pd


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
