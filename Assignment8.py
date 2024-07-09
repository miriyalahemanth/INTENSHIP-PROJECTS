import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
monthlist = df ['month_number'].to_list()

labels = ['FaceCream','FaseWash','ToothPaste','Bathing soap','Shampoo','moisturizer']
salesData = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(),
              df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('SALES DATA')
plt.show()