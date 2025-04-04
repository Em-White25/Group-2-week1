from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df_titanic_copy.drop('survived',axis=1)
df_titanic_copy['survived']

X_train, X_test, y_train, y_test = train_test_split(df_titanic_copy.drop('survived',axis=1), 
                                                    df_titanic_copy['survived'], test_size=0.30, 
                                                    random_state=101)
#Training and Test of predictions
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
