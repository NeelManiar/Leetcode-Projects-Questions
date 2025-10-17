import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    head = employees.head(3)
    return head