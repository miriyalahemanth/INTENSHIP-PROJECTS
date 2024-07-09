import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
plt.plot(df['month_number'],df['total_profit'],'bo-',color="r",linestyle='--',label='profit data of last year')


plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Sales data of last year')


plt.legend()

plt.show()