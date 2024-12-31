#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
file_path = 'Online Retail 2.xlsx'
df = pd.read_excel(file_path)

# Step 1: Handle Missing Values - Drop rows with missing CustomerID
df_cleaned = df.dropna(subset=['CustomerID'])

# Step 2: Remove Outliers - Filter out negative Quantity and UnitPrice
df_cleaned = df_cleaned[(df_cleaned['Quantity'] > 0) & (df_cleaned['UnitPrice'] > 0)]

# Step 3: Convert InvoiceDate to datetime format
df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'])

# Step 4: Create TotalPrice
df_cleaned['TotalPrice'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']

# Step 5: Aggregate Data by CustomerID
customer_aggregation = df_cleaned.groupby('CustomerID').agg({
    'TotalPrice': 'sum',  # Total revenue
    'InvoiceNo': 'count',  # Purchase frequency
    'Quantity': 'sum'  # Total items purchased
}).rename(columns={
    'TotalPrice': 'TotalRevenue',
    'InvoiceNo': 'Frequency',
    'Quantity': 'TotalItems'
})

# Save the aggregated data to a CSV file for future use
customer_aggregation.to_csv('Customer_Aggregation.csv')

# Display the first few rows of the aggregated data
print(customer_aggregation.head())


# In[3]:


from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_aggregation[['TotalRevenue', 'Frequency', 'TotalItems']])

# Step 2: Determine optimal number of clusters using Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Step 3: Apply K-Means with the chosen number of clusters (e.g., 4)
optimal_clusters = 4  # You can adjust based on the Elbow Curve
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
customer_aggregation['Cluster'] = kmeans.fit_predict(scaled_data)

# Step 4: Analyze clusters
cluster_analysis = customer_aggregation.groupby('Cluster').mean()
print(cluster_analysis)

# Save the results
customer_aggregation.to_csv('Customer_Clusters.csv')


# In[4]:


# Scatter plot for visualizing clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='TotalRevenue', 
    y='Frequency', 
    hue='Cluster', 
    data=customer_aggregation, 
    palette='viridis', 
    s=100
)
plt.title('Customer Segments')
plt.xlabel('Total Revenue')
plt.ylabel('Purchase Frequency')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()


# In[ ]:




