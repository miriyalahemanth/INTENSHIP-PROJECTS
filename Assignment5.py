import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
plt.bar(df['month_number'],df['facecream'],color="b",label='Face Cream Sales Data',width=-0.3,align='edge')
plt.bar(df['month_number'],df['facewash'],color="r",label='Face Wash Sales Data',width=0.3,align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.title('Facewash and Facecream Sales data')
plt.grid(True)
plt.legend()
plt.show()