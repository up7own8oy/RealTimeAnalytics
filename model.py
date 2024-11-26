import numpy as np
from sklearn.svm import OneClassSVM
import pickle

# Przykładowe dane treningowe: 1000 próbek, każda z 20 cechami
X_train = np.random.rand(1000, 20) 

# Trening modelu One-Class SVM
model = OneClassSVM(gamma='auto').fit(X_train)

# Zapisanie modelu pliku *.plk
with open('oc_svm_model.pkl', 'wb') as f:
    pickle.dump(model, f)
