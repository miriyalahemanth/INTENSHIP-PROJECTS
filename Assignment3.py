import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('company_sales_data.csv')
plt.plot(df['month_number'],df['facecream'],'bo-',color="b",label='Face cream Sales Data')
plt.plot(df['month_number'],df['facewash'],'bo-',color="k",label='Face wash Sales Data')
plt.plot(df['month_number'],df['toothpaste'],'bo-',color="g",label='ToothPaste Sales Data')
plt.plot(df['month_number'],df['bathingsoap'],'bo-',color="r",label='Bathing Soap Sales Data')
plt.plot(df['month_number'],df['shampoo'],'bo-',color="m",label='Shampoo Sales data')
plt.plot(df['month_number'],df['moisturizer'],'bo-',color="y",label='Moisturizer Sales data')

plt.xlabel('Month Number')
plt.ylabel('Sales unit in number')
plt.title('Company Sales data of last year')


plt.legend()

plt.show()
