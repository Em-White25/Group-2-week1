from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score



predictions = logmodel.predict(X_test)
print('predictions')
accuracy=confusion_matrix(y_test,predictions)
accuracy=accuracy_score(y_test,predictions)

# Print accuracy
print(f'Accuracy: {accuracy}')

#Evaluation of model perfomance
print(classification_report(y_test,predictions))