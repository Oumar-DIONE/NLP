from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def knn_model(n_neighbors, x, y, p=2, metric_="minkowski"):

    model = KNeighborsClassifier(
        n_neighbors, p=p, metric=metric_
    )  # by default n_neighbors= 5
    model.fit(x, y)
    return model


def make_prediction(x, model):
    y = model.predict(x)
    return y


def evaluate(y1, y2):
    cm = confusion_matrix(y1, y2)
    accurace_ = accuracy_score(y1, y2)
    print(f"{accurace_:.1%} de bonnes réponses sur les données de test pour validation")
    print("matrice de confusion")
    print(cm)
