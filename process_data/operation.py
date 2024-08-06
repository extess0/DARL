import numpy as np


def sqrt(feature):
    sqrt_feature = np.sqrt(np.abs(feature))
    return sqrt_feature


def power3(feature):
    new_feature = np.power(np.array(feature), 3)
    return new_feature


def reciprocal(feature):
    feature = np.array(feature)
    new_feature = np.where(feature != 0, 1 / feature, feature)
    return new_feature


def square(feature):
    new_feature = np.square(np.array(feature))
    return new_feature


def rabs(feature):
    new_feature = np.abs(np.array(feature))
    return new_feature


def log(feature):
    log_feature = np.where(np.abs(feature) > 0, np.log(np.abs(feature)), np.log(1))
    return log_feature


def add(feature1, feature2):
    return np.array(feature1) + np.array(feature2)


def multiply(feature1, feature2):
    return np.array(feature1) * np.array(feature2)


def subtract(feature1, feature2):
    return np.abs(np.array(feature1) - np.array(feature2))


def divide(feature1, feature2):
    feature1 = np.array(feature1)
    feature2 = np.array(feature2)
    feature_d1 = np.where(feature2 != 0, feature1 / feature2, 1)
    return feature_d1


def get_nunique_feature(feature1, feature2):
    new_fe = []
    feature1 = np.array(feature1).reshape(-1, 1)
    feature2 = np.array(feature2).reshape(-1, 1)
    feature = np.concatenate([feature1, feature2], axis=1)
    for each in feature:
        x = each[0] + each[1]
        new_fe.append(x)
    new_fe = np.array(new_fe)
    return new_fe


def generate_cross_fe(ori_feature1, ori_feature2):
    all_value = {}
    i = 0
    for x in np.unique(ori_feature1):
        for y in np.unique(ori_feature2):
            all_value[str(int(x)) + str(int(y))] = i
            i += 1
    k = len(ori_feature1)
    new_features = np.zeros(k)
    for i in range(k):
        combined_value = str(int(ori_feature1[i])) + str(int(ori_feature2[i]))
        feature_index = all_value.get(combined_value, -1)
        new_features[i] = feature_index
    return new_features

