# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def main():
    print("=========================================================================================\n")

    print("Program started running...")

    # Load the dataset

    print("\033[34m" + "Reading data from the HW4-transaction-dataset.txt" + "\033[0m wait..")

    import pandas as pd

    mydata = pd.read_csv("HW4-transaction-dataset.txt", header=0, sep="|", na_values="?")

    print("\t Data read successfully")

    # Check for missing values

    print("\033[34m" + "Number" + "\033[0m of rows with missing values:", mydata.isnull().sum().sum())

    # Remove rows with missing values
    mydata = mydata.dropna()

    # Convert order values to 1s and 0s
    mydata["order"] = mydata["order"].map({"y": 1, "n": 0})

    # Split the dataset into training and testing with a 70-30 split ratio
    train, test = train_test_split(mydata, test_size=0.3, random_state=1)

    # Convert the order variable to a factor
    train["order"] = pd.factorize(train["order"])[0]
    test["order"] = pd.factorize(test["order"])[0]

    # Run decision tree using the variables duration, startHour, cCount, and bCount to predict order
    dtree = DecisionTreeClassifier(max_depth=4, random_state=1)

    # Run 10-fold cross-validation with decision tree
    dtree_scores = cross_val_score(dtree, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)

    print("\n\033[34m" + "Decision" + "\033[0m Tree 10-fold Cross Validation Scores:", dtree_scores)

    print("\tMean Score:", dtree_scores.mean())

    # Run Naïve Bayes, SVM (RBF Kernel), KNN, and Random Forest using 10-fold cross-validation
    nb = GaussianNB()
    svm = SVC(kernel='rbf')
    knn = KNeighborsClassifier()
    rf = RandomForestClassifier(n_estimators=100, random_state=1)

    nb_scores = cross_val_score(nb, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)
    svm_scores = cross_val_score(svm, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)
    knn_scores = cross_val_score(knn, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)
    rf_scores = cross_val_score(rf, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)

    print("\n\033[34m" + "Naive Bayes" + "\033[0m 10-fold Cross Validation Scores:", nb_scores)
    print("\tMean Score:=", nb_scores.mean())

    print("\n\033[34m" + "SVM" + "\033[0m 10-fold Cross Validation Scores:", svm_scores)

    print("\tMean Score:=", svm_scores.mean())

    print("\n\033[34m" + "KNN" + "\033[0m 10-fold Cross Validation Scores:", knn_scores)

    print("\tMean Score:=", knn_scores.mean())

    print("\n\033[34m" + "Random" + "\033[0m Forest 10-fold Cross Validation Scores:", rf_scores)

    print("\tMean Score:=", rf_scores.mean())

    # Run a bagging model with a decision tree and random forest using tenfold cross validation repeated three times
    bagging_dtree = BaggingClassifier(base_estimator=DecisionTreeClassifier(max_depth=4), n_estimators=10,
                                      random_state=1)
    bagging_rf = BaggingClassifier(base_estimator=RandomForestClassifier(n_estimators=100, random_state=1),
                                   n_estimators=10, random_state=1)

    bagging_dtree_scores = cross_val_score(bagging_dtree, mydata[["duration", "startHour", "cCount", "bCount"]],
                                           mydata["order"], cv=10, n_jobs=-1)
    bagging_rf_scores = cross_val_score(bagging_rf, mydata[["duration", "startHour", "cCount", "bCount"]],
                                        mydata["order"], cv=10, n_jobs=-1)

    print("\n\033[34m" + "Bagging" + "\033[0m with Decision Tree 10-fold Cross Validation Scores:",
          bagging_dtree_scores)

    print("\tMean Score:", bagging_dtree_scores.mean())

    print("\n\033[34m" + "Bagging" + "\033[0m with Random Forest 10-fold Cross Validation Scores:", bagging_rf_scores)

    print("\tMean Score:", bagging_rf_scores.mean())

    # Train a boosting method using gbm
    gbm = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=1)

    gbm_scores = cross_val_score(gbm, mydata[["duration", "startHour", "cCount", "bCount"]], mydata["order"], cv=10)
    print("\n##-- comparison test starting__##\n")
    print("\n\033[34m" + "Gradient" + "\033[0m Boosting 10-fold Cross Validation Scores:", gbm_scores)

    print("\tMean Score:", gbm_scores.mean())

    # Compare the mean scores of bagging and boosting
    print("\n\033[34m" + "Bagging" + "\033[0m  with Decision Tree Mean Score:", bagging_dtree_scores.mean())

    print("\tGradient Boosting Mean Score:", gbm_scores.mean())

    if gbm_scores.mean() > bagging_dtree_scores.mean():
        print("\n\nGradient Boosting performs better than Bagging with Decision Tree.")
    else:
        print( "\n\nBagging with Decision Tree performs better than Gradient Boosting. ")

    print("=========================================================================================\n")


if __name__ == "__main__":
    main()
