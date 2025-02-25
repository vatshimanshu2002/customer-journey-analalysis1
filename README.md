# customer-journey-analalysis1# Customer-Journey-Analysis-Using-Clustering-and-Dimensionality-Reduction-Enhancing-User-Experience-
This project analyzes customer behavior patterns using K-Means Clustering and UMAP Dimensionality Reduction to segment users based on their interaction with travel-related platforms. It helps identify high-value customers, casual browsers, and frequent travelers for personalized marketing strategies.
📊 Customer Journey Analysis Using Clustering and Dimensionality Reduction

🌟 Project Overview

The Customer Journey Analysis (CJA) project aims to analyze user behavior patterns on travel-related platforms. By leveraging K-Means Clustering and UMAP Dimensionality Reduction, this project segments customers based on their browsing habits, check-ins, and time spent on travel pages.

This segmentation helps businesses identify high-value customers, casual browsers, and frequent travelers, enabling personalized marketing and user experience improvements.

🚀 Key Features
	1.	Data Upload: Upload customer behavior datasets via an interactive Streamlit interface.
	2.	Feature Selection: Choose relevant features for clustering, like yearly views, check-ins, and comments.
	3.	Dimensionality Reduction: Use UMAP to simplify complex datasets while retaining meaningful patterns.
	4.	Customer Clustering: Apply K-Means clustering to segment users into behavioral groups.
	5.	Visualization: Display clusters with scatter plots, bar charts, and funnel visualizations.
	6.	Downloadable Results: Export the segmented dataset as a CSV or Pickle file for further analysis.
 
 🛠 Tech Stack
	•	Programming Language: Python
	•	Data Analysis: Pandas, NumPy
	•	Machine Learning: Scikit-Learn
	•	Dimensionality Reduction: UMAP
	•	Visualization: Seaborn, Matplotlib
	•	Web App Interface: Streamlit
 
 📂 Project Structure
  📦 CJA_Project
├─ 📄 CJA.ipynb               # Jupyter Notebook with project code
├─ 📄 UI.ipynb                # Jupyter Notebook for Streamlit UI
├─ 📄 CJA_main_ui.py          # Streamlit app for real-time analysis
├─ 📄 Customer behaviour Tourism.csv  # Sample dataset
├─ 📄 README.md               # Project documentation (this file)

⚙ Setup Instructions
	
 1.	Clone the Repository: git clone https://github.com/yourusername/Customer-Journey-Analysis.git
cd Customer-Journey-Analysis.
	
 2.	Create Virtual Environment (Optional but Recommended):
 python3 -m venv cja_env
source cja_env/bin/activate  # Mac/Linux
cja_env\\Scripts\\activate   # Windows
	
 3.	Install Required Packages:pip install -r requirements.txt
 4.	Run the Streamlit App:streamlit run CJA_main_ui.py

📊 Sample Output
Here’s what the Streamlit interface looks like:
	•	📤 Upload CSV file
	•	📈 Visualize customer clusters
	•	📥 Download segmented results
