import numpy as np
import pickle


# loading the saved model

loaded_model = pickle.load(open("C:/Users/User/Machine Learning/Projects/Heart Disease Prediction/trained_model.sav", 'rb'))

input_data = np.array([41, 0, 1, 130, 204, 0,0,0, 172,0, 1.4, 2, 0])

data = input_data.reshape(1, -1)

prediction = loaded_model.predict(data)


if (prediction[0] == 0):
    print("The person doesn't have heart disease")
else:
    print("The person has a heart disease")