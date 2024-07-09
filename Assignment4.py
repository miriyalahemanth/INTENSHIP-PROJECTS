import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')

plt.plot(df['month_number'],df['toothpaste'],'bo',color="b",label='ToothPaste Sales Data')

plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.title('Tooth paste sales data')
plt.grid(True)

plt.legend()

plt.show()