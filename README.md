# Customer-segmentation-and-Personalization
# Customer Segmentation Using Clustering Techniques

## Project Overview
This project focuses on customer segmentation using clustering techniques applied to transactional data from an online retail store. The goal is to group customers based on their purchasing behavior and demographics, enabling the development of personalized marketing strategies.

---

## Dataset
**Source**: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)

### Dataset Description:
- **InvoiceNo**: Unique identifier for transactions.
- **StockCode**: Product code.
- **Description**: Product description.
- **Quantity**: Number of items purchased.
- **InvoiceDate**: Date and time of the transaction.
- **UnitPrice**: Price per unit.
- **CustomerID**: Unique identifier for each customer.
- **Country**: Country of residence.

---

## Project Steps

### 1. Data Preprocessing
- Handled missing values by dropping rows with null `CustomerID`.
- Removed outliers by filtering out transactions with negative `Quantity` or `UnitPrice`.
- Converted `InvoiceDate` to datetime format.
- Created a new column `TotalPrice` as `Quantity * UnitPrice`.
- Aggregated data by `CustomerID` to calculate:
  - **TotalRevenue**: Total spend per customer.
  - **Frequency**: Number of purchases.
  - **TotalItems**: Total items purchased.

### 2. Clustering
- Used the K-Means algorithm to segment customers.
- Determined the optimal number of clusters using the **Elbow Method**.
- Standardized the features for clustering using `StandardScaler`.
- Added cluster labels to each customer.

### 3. Cluster Analysis
- Analyzed the characteristics of each cluster to label them, such as:
  - High Spenders
  - Frequent Buyers
  - Occasional Buyers

### 4. Visualization
- Created scatter plots to visualize customer segments.
- Recommended exporting data to Tableau or Power BI for advanced interactive dashboards.

---

## Results
- Customers were segmented into distinct groups based on revenue, purchase frequency, and items purchased.
- Insights derived from these clusters enabled tailored marketing strategies, such as:
  - Rewarding high spenders.
  - Re-engaging occasional buyers.

---

## Technologies Used
- **Python**:
  - Libraries: Pandas, Scikit-learn, Matplotlib, Seaborn
- **Jupyter Notebook**: For data analysis and visualization.
- **Tableau/Power BI**: For interactive visualizations (optional).

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your_username>/<repository_name>.git
   ```
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script to preprocess the data and perform clustering.
4. Visualize results in Python or export to Tableau/Power BI for further exploration.

---

## Folder Structure
```
├── data
│   └── Online_Retail.xlsx  # Raw dataset
├── notebooks
│   └── customer_segmentation.ipynb  # Analysis and clustering code
├── results
│   └── Customer_Clusters.csv  # Clustered data
├── visuals
│   └── cluster_plots.png  # Scatter plots of clusters
├── README.md  # Project documentation
```

---

## Future Enhancements
- Explore advanced clustering techniques (e.g., Hierarchical Clustering, DBSCAN).
- Incorporate additional features like customer demographics (if available).
- Automate report generation using Python or BI tools.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For questions or feedback, please contact:
- **Name**: Ashmeet Saluja
- **Email**: salujaashmeet179@gmail.com
- **GitHub**: ashmeet-saluja
