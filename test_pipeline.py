import unittest
#from titanic_pipeline import clean_data, load_data

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.df = load_data('cleaned_titanic.csv')
    
    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertFalse(cleaned_df.isnull().sum().any(), "There should be no missing values.")
        self.assertIn('sex', cleaned_df.columns, "Sex column should exist.")

if __name__ == "__main__":
    unittest.main()