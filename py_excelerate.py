from pyexcelerate import Workbook
import pandas as pd
import numpy as np

#pyexcelerate r/w performance is much better than  StyleFrame

def df_to_excel(df):
    return [df.columns.tolist(), ] + df.values.tolist()


data = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
		    columns=['a', 'b', 'c', 'd', 'e'])
data = df_to_excel(data)

wb = Workbook()
wb.new_sheet("pyexcelerate", data=data)
wb.save("output.xlsx")

