This project demonstrates basic sales data analysis using Python and Pandas in a Jupyter Notebook environment.
The process involves creating a sample CSV file, reading it into a Pandas DataFrame, performing aggregation with groupby() and sum(), and visualizing the results using Pandas built-in plotting functions.

⚙ Tools Used
Python 3
Pandas (for data handling and analysis)
Matplotlib (for data visualization)
Jupyter Notebook / Google Colab (for interactive coding)

📂 Steps Performed
Create CSV File
A sample sales dataset (sales_data.csv) was generated using Pandas and saved locally.

Load CSV File
The dataset was read into a Pandas DataFrame using pd.read_csv().

Explore the Data
Checked the first few records using .head()
Displayed data statistics with .describe()

Data Aggregation
Grouped sales by category using groupby("Category").sum() to get total sales for each category.

Data Visualization
Created bar and line charts using Pandas .plot()
Showed visual insights into category-wise sales

🎯 Outcome
Learned how to create, read, and analyze CSV files using Pandas.
Generated meaningful insights from the dataset.
Created visual charts to better understand the sales data.

This project is appropriate for novices learning Python since it provides an introduction to data manipulation and visualization.
