import pandas as pd


def weighted_sum(data, weights, directions):
    weighted_sums = []
    for _, row in data.iterrows():
        sum_weight = sum(weights[col] * (-row[col] if directions[col] == 'min' else row[col])
                         for col in data.columns[1:])
        weighted_sums.append(sum_weight)
    return weighted_sums


def normalize_data(data):
    cols_to_normalize = [col for col in data.columns[1:] if data[col].dtype != object]
    for col in cols_to_normalize:
        data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
    return data


def get_ranking(data, weighted_sums):
    tuples = list(zip(data.iloc[:, 0], weighted_sums))
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
    return [t[0] for t in sorted_tuples]


if __name__ == '__main__':
    data_example = pd.DataFrame({
        'house': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
        'C1': [80, 65, 83, 40, 52, 94],
        'C2': [90, 58, 60, 80, 72, 96],
        'C6': [5, 1, 7, 10, 8, 6],
    })
    directions_example = {'C1': 'min', 'C2': 'max', 'C6': 'max'}
    weights_example = {'C1': 0.2, 'C2': 0.4, 'C6': 0.4}
    normalized_data = normalize_data(data_example)
    weighted_sum_example = weighted_sum(normalized_data, weights_example, directions_example)
    print(weighted_sum_example)
    print(get_ranking(data_example, weighted_sum_example))
