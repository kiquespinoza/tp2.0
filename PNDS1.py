import pandas as pd   

df1 = pd.DataFrame(r'C:\Users\eespice\Desktop\tp2\tp2.0')
df2 = pd.DataFrame(r'C:\Users\eespice\Desktop\tp2\tp2.0')
df3 = pd.DataFrame(r'C:\Users\eespice\Desktop\tp2\tp2.0')
df4 = pd.DataFrame(r'C:\Users\eespice\Desktop\tp2\tp2.0')
df5 = pd.DataFrame(r'C:\Users\eespice\Desktop\tp2\tp2.0')

df1.set_index('customer_id', inplace = True)
df2.set_index('order_id', inplace = True) 
df3.set_index('order_payment', inplace = True)
df4.set_index('order_dataset', inplace = True)
df5.set_index('product-dataset', inplace = True)
