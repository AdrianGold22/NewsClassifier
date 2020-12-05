from imblearn.over_sampling import RandomOverSampler
from sklearn import metrics


def generate_metrics(dict_classifiers, x_train, y_train, x_test, y_test, list_model):
    data_results = []
    for classifier in dict_classifiers:
        clf = dict_classifiers[classifier]
        clf = clf.fit(x_train, y_train)
        y = clf.predict(x_test)
        model_name = list_model['lexical']
        classifier_name = classifier
        f1 = metrics.f1_score(y_test, y)
        accuracy = metrics.accuracy_score(y_test, y)
        recall = metrics.recall_score(y_test, y)
        precision = metrics.precision_score(y_test, y)
        log_loss = metrics.log_loss(y_test, y)
        data_results.append(
            {'model_name': model_name, 'classifier_name': classifier_name, 'f1': f1, 'accuracy': accuracy,
             'recall': recall, 'precision': precision, 'log_loss': log_loss, 'classifier': classifier})

    return data_results


def oversampling(x_train, y_train, x_test, y_test):
    ros = RandomOverSampler(random_state=1000)
    x_tr, y_tr = ros.fit_resample(x_train, y_train)
    x_te, y_te = ros.fit_resample(x_test, y_test)
    return x_tr, y_tr, x_te, y_te
