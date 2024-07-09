import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
plt.bar(df['month_number'],df['bathingsoap'])
plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.title('Bathingsoap Sales data')
plt.grid(True)
plt.legend()
plt.show()