import time
import random
from flask import Flask, jsonify
from sklearn.datasets import fetch_openml
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Histogram


tuning_metric = Histogram('tuning_latency_seconds', "Tuning latency")
training_metric = Histogram('training_latency_seconds', "Training latency")
evaluate_metric = Histogram('evaluate_latency_seconds', "Evaluate latency")

SAMPLE_SIZE = 8000

X,y = fetch_openml(
    name="mnist_784",
    version=1,
    as_frame=False,
    return_X_y=True,
    cache=True)

X = X[:SAMPLE_SIZE]
y = y[:SAMPLE_SIZE]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

params = {
    "svm__C": [1, 10, 100],
    "svm__gamma": [0.001, 0.01]
}

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf"))
])

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
    """Exposes Prometheus metrics in the correct format."""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route("/api/classify", methods=["POST"])
def api_classify():



    # -------------------------
    # TUNING
    # -------------------------


    with tuning_metric.time():
        grid = GridSearchCV(
            pipeline,
            params,
            cv=cv,
            refit=False,
            n_jobs=1
        )

        grid.fit(X_train, y_train)
        best_params = grid.best_params_


    # -------------------------
    # TRAINING
    # -------------------------
    
    with training_metric.time():
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("svm", SVC(
                kernel="rbf",
                C=best_params["svm__C"],
                gamma=best_params["svm__gamma"]
            ))
        ])

        model.fit(X_train, y_train)


    # -------------------------
    # EVALUATION
    # -------------------------

    with evaluate_metric.time():
        accuracy = model.score(X_test, y_test)

        response = jsonify({
            "accuracy": accuracy,
            "best_params": best_params
        })

    return response


if __name__ == "__main__":
    print("Starting SVM server on port 5002 …")
    app.run(host="0.0.0.0", port=5002)