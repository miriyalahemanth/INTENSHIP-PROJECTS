import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
x=np.random.normal(df['total_profit'],df['month_number'])
plt.hist(x)
plt.title('month data')
plt.show()
