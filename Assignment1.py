import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
plt.plot(df['month_number'],df['total_profit'])
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Company Profit Per Month")
plt.show()