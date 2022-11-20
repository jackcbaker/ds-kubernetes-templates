# Attribution: example modified from scikit-learn quickstart
# url: https://scikit-learn.org/stable/getting_started.html
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


def main():
    # create a pipeline object
    pipe = make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=0)
    )

    # load the iris dataset and split it into train and test sets
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # fit the whole pipeline
    print("Fitting model...")
    pipe.fit(X_train, y_train)


    # we can now use it like any other estimator
    score = confusion_matrix(pipe.predict(X_test), y_test)
    print(f"Training finished with confusion matrix:\n{score}")


if __name__ == '__main__':
    main()