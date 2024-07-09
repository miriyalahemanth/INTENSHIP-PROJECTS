import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('company_sales_data.csv')
plt.subplot(2, 1, 1)  
plt.plot(df['month_number'],df['bathingsoap'],'ko-')
plt.title('Sales data of Bathing soap')


plt.subplot(2, 1, 2)  
plt.plot(df['month_number'],df['facewash'], 'ro-')
plt.title('Sales data of Facewash')
plt.xlabel('Month Number')
plt.ylabel('Sales Unit Number')
plt.tight_layout()
plt.show()