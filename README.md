## Group-2-week1

# Titanic Survival Prediction Analysis

## Project Overview
The objective of this project is to build a data processing and machine learning pipeline that takes raw Titanic passenger data, cleans it, performs exploratory data analysis (EDA), extracts useful features, trains a predictive model, and evaluates its performance. The pipeline is designed to be modular, ensuring efficient data handling and reusability.

## Dataset Information
The dataset contains information about passengers aboard the Titanic, one of the most famous datasets used in data science and machine learning. It was created to analyze and understand the factors that influenced survival rates during the tragic sinking of the RMS Titanic on April 15, 1912.

### Data Description
The dataset is widely used for predictive modeling and statistical analysis to determine which factors (such as socio-economic status, age, gender, etc.) were associated with a higher likelihood of survival. It contains **1,309 rows** and **14 columns**.

### Columns:
- **Pclass**: Ticket class indicating the socio-economic status of the passenger. It is categorized into three classes:
  - 1 = Upper
  - 2 = Middle
  - 3 = Lower
- **Survived**: A binary indicator that shows whether the passenger survived (1) or not (0) during the Titanic disaster. This is the target variable for analysis.
- **Name**: The full name of the passenger, including title (e.g., Mr., Mrs., etc.).
- **Sex**: The gender of the passenger, denoted as either male or female.
- **Age**: The age of the passenger in years.
- **SibSp**: The number of siblings or spouses aboard the Titanic for the respective passenger.
- **Parch**: The number of parents or children aboard the Titanic for the respective passenger.
- **Ticket**: The ticket number assigned to the passenger.
- **Fare**: The fare paid by the passenger for the ticket.
- **Cabin**: The cabin number assigned to the passenger, if available.
- **Embarked**: The port of embarkation for the passenger. It can take one of three values:
  - C = Cherbourg
  - Q = Queenstown
  - S = Southampton
- **Boat**: If the passenger survived, this column contains the identifier of the lifeboat they were rescued in.
- **Body**: If the passenger did not survive, this column contains the identification number of their recovered body, if applicable.
- **Home.dest**: The destination or place of residence of the passenger.

These descriptions provide a detailed understanding of each column in the Titanic dataset, offering insights into the demographic, travel, and survival-related information recorded for each passenger.

## Data Pipeline
The project follows a structured pipeline to process the data and build a predictive model:

1. **Data Cleaning:**
   - Handling missing values in critical columns (e.g., Age, Embarked).
     rows that had more than two values missing or null were dropped to prevent outliers.
     rows after cleaning were reduced to **608 rows** and **9 columns**
   - Encoding categorical variables for machine learning compatibility.
   - Creating new features from existing ones (e.g., family size from SibSp and Parch).
   - Scaling numerical features if necessary also applying encoding columns.

2. **Exploratory Data Analysis (EDA):**
   - **Loading and inspecting data:** Checking missing values, feature distributions, and basic statistics.
   - **Survival rate analysis:** Examining survival percentages by passenger class, gender, and other features.
   - **Feature correlations:** Using heatmaps to visualize relationships between numerical variables.
   - **Visualization of distributions:** Creating bar plots, histograms, and box plots for key features such as Age, Fare, and Pclass.

4. **Model Training:**
   - Training machine learning models (e.g., Logistic Regression, Random Forest) to predict survival.
   - Evaluating model performance using accuracy, precision, recall, and F1-score.

5. **Pipeline Automation:**
   - Integrating all steps into an automated script.
   - Ensuring reusability for different Titanic datasets.

## Running the Project
To execute the full pipeline, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/Em-White25/Grp2-Wk1-Project.git
   cd titanic-survival-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the preprocessing and model training script:
   ```sh
   python src/main.py
   ```
4. Run unit tests to validate functionality:
   ```sh
   pytest tests/
   ```

## Deliverables
- **Data Cleaning:** Processed dataset with handled missing values.
- **EDA:** Summary statistics and survival insights.
- **Machine Learning Model:** Trained classifier for survival prediction.
- **Model Evaluation:** Performance metrics (accuracy, precision, recall, F1-score).
- **Visualizations:** Key plots for data interpretation.
- **Documentation:** Full project workflow and test cases.
- **Automated Pipeline:** End-to-end script for data processing and prediction.
