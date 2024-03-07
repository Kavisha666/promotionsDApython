#!/usr/bin/env python
# coding: utf-8

# # Import the fact_events.csv file

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("C:\\Users\\kirtik\\Desktop\\power-bi-course-resources-main\\C9 DATASET\\fact_events.csv")
df


# In[60]:


##Display first n rows and last n rows.


# In[3]:


df.head()


# In[4]:


df.tail()


# In[63]:


##display the overall information of data


# In[5]:


df.info()


# In[6]:


df.dtypes                            ##Display datatypes of a column in a table


# In[7]:


df.index                           ##Display the index of  a table


# In[8]:


df.values                          ##Display only values in a table


# In[9]:


df.axes                            ##Display index  & columns in a table


# In[10]:


df.shape                  ##Display the no.of rows & columns ina table


# # import  dim_Products.csv

# In[11]:


import pandas as pd


# In[12]:


product=pd.read_csv("C:\\Users\\kirtik\\Desktop\\power-bi-course-resources-main\\C9 DATASET\\dim_products.csv")
product


# # Display the dim_stores.csv file

# In[13]:


stores=pd.read_csv("C:\\Users\\kirtik\\Desktop\\power-bi-course-resources-main\\C9 DATASET\\dim_stores.csv")
stores


# # import the Dim_campaigns.csv

# In[14]:


campaigns=pd.read_csv("C:\\Users\\kirtik\\Desktop\\power-bi-course-resources-main\\C9 DATASET\\dim_campaigns.csv")
campaigns


# In[15]:


df.columns            ##display  the columns ina table


# In[16]:


df.size


# # kpi Indicators

# In[17]:


df['pp']= dp = (
    np.where(
        df["promo_type"] == "50% OFF",
        df["base_price"] * 0.5,
        np.where(
            df["promo_type"] == "33% OFF",
            df["base_price"] * 0.33,   
            np.where(
                df["promo_type"] == "BOGOF",
                df["base_price"] * (1 - 0.5),                                  
                np.where(
                    df["promo_type"] == "25% OFF",
                    df["base_price"] * 0.25,                             
                    np.where(df["promo_type"] == "500 Cashback",
                        500,
                        df["base_price"]
                    )
                )
            )
        )
    )
)
dp 


# In[18]:


discounted_Prices=dp*df["quantity_sold(after_promo)"]
discounted_Prices


# In[19]:


discounted_Prices.sum()


# In[20]:


df.loc[df["promo_type"] == "BOGOF", "quantity_sold(after_promo)"] = df["quantity_sold(after_promo)"] * 2


# In[21]:


Units_soldADP= df["quantity_sold(after_promo)"].sum()
Units_soldADP


# In[22]:


Units_soldBDP=df["quantity_sold(before_promo)"].sum()
Units_soldBDP


# In[23]:


ISU=Units_soldADP - Units_soldBDP
ISU


# In[51]:


revenue_BDP=df["quantity_sold(before_promo)"]*df["base_price"]
revenue_BDP


# In[52]:


sum_Revenue_BDP=revenue_BDP.sum()
sum_Revenue_BDP


# In[53]:


revenue_ADP = (df["base_price"] * df["quantity_sold(after_promo)"])-discounted_Prices
revenue_ADP


# In[54]:


sum_Revenue_ADP=revenue_ADP.sum()
sum_Revenue_ADP


# In[33]:


IR=sum_Revenue_ADP - sum_Revenue_BDP
IR


# In[34]:


merged_df = pd.merge(df,stores, on='store_id', how='left')
merged_df


# In[35]:


merged_df1 = pd.merge(df,product, on='product_code', how='left')
merged_df1


# In[36]:


merged_df2 = pd.merge(df,campaigns, on='campaign_id', how='left')
merged_df2


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame

# Check DataFrame structure
print(df.head())  # Ensure 'promo_type', 'pp', and 'IR' columns are present

# Group by 'promo_type' and sum 'pp' and 'IR' separately
grouped_df = df.groupby('promo_type')['pp'].sum()
print(grouped_df)  # Check if grouping operation is returning the expected result

# Plot the bar chart
ax = grouped_df.plot(kind="bar")

# Add data labels
for i in ax.patches:
    ax.text(i.get_x() + i.get_width()/2, i.get_height(), 
            str(round(i.get_height(), 2)), 
            ha='center', va='bottom')

# Set labels and title
plt.xlabel('Promo Type')
plt.ylabel('Sum')
plt.title('Sum of pp by Promo Type')

# Show the plot
plt.show()


# In[72]:


import matplotlib.pyplot as plt

# Group by 'product_code' and sum 'IR'
grouped_df = df.groupby('product_code')[['ISU']].sum()

# Plot the line chart
grouped_df.plot(kind="line",marker='o')
print(grouped_df)

# Set labels and title
plt.xlabel('Product Code')
plt.ylabel('Sum of Isu')
plt.title('Sum of Isu by Product Code')

# Show the plot
plt.show()


# In[71]:


import matplotlib.pyplot as plt

# Group by 'product_code' and sum 'IR'
grouped_df = df.groupby('product_code')[['pp']].sum()

# Plot the line chart
grouped_df.plot(kind="barh")
print(grouped_df)

# Set labels and title
plt.xlabel('Product Code')
plt.ylabel('Sum of IR')
plt.title('Sum of IR by Product Code')

# Show the plot
plt.show()


# In[ ]:




