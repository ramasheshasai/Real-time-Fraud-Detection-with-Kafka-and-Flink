import xgboost as xgb
import numpy as np
import pickle

X = np.random.rand(500, 3)
y = (X[:, 0] + X[:, 1] + X[:, 2] > 1.5).astype(int)

model = xgb.XGBClassifier()
model.fit(X, y)

pickle.dump(model, open("fraud_model.pkl", "wb"))
print("Model Saved")
