import pandas as pd
import numpy as np


def preference_degree(data, direction, weights, threshold):
    pref_matrix = pd.DataFrame(
        np.zeros((len(data), len(data))), index=data.index, columns=data.index)
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                pref = 0
                for col, w in weights.items():
                    diff = data.loc[i, col] - data.loc[j, col] if direction[col] == 'max' \
                        else data.loc[j, col] - data.loc[i, col]
                    if diff > threshold[col]:
                        pref += w
                    elif diff > 0:
                        pref += w * diff / threshold[col]
                pref_matrix.iloc[i, j] = pref / sum(weights.values())
    return pref_matrix


def promethee1(pref_matrix, data):
    phi_plus = pref_matrix.sum(axis=1)
    phi_minus = pref_matrix.sum()
    phi_plus_ranking = phi_plus.argsort()[::-1]  # descending order
    phi_plus_ranking = data.iloc[phi_plus_ranking].iloc[:, 0].tolist()
    phi_minus_ranking = phi_minus.argsort()
    phi_minus_ranking = data.iloc[phi_minus_ranking].iloc[:, 0].tolist()
    return phi_plus.tolist(), phi_minus.tolist(), phi_plus_ranking, phi_minus_ranking


def promethee2(phi_plus, phi_minus, data):
    phi_net = np.array(phi_plus) - np.array(phi_minus)
    phi_net_ranking = phi_net.argsort()[::-1]  # descending order
    phi_net_ranking = data.iloc[phi_net_ranking].iloc[:, 0].tolist()
    return phi_net.tolist(), phi_net_ranking


if __name__ == '__main__':
    data_example = pd.DataFrame({
        'house': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
        'C1': [80, 65, 83, 40, 52, 94],
        'C2': [90, 58, 60, 80, 72, 96],
        'C3': [600, 200, 400, 1000, 600, 700],
        'C4': [5.4, 9.7, 7.2, 7.5, 2.0, 3.6],
        'C5': [8, 1, 4, 7, 3, 5],
        'C6': [5, 1, 7, 10, 8, 6],
    })
    directions_example = {'C1': 'min', 'C2': 'max',
                          'C3': 'min', 'C4': 'min', 'C5': 'min', 'C6': 'max'}
    weights_example = {'C1': 0.1, 'C2': 0.2,
                       'C3': 0.2, 'C4': 0.1, 'C5': 0.2, 'C6': 0.2}
    threshold_example = {'C1': 20, 'C2': 10,
                         'C3': 200, 'C4': 4, 'C5': 2, 'C6': 2}
    pref_matrix_example = preference_degree(
        data_example, directions_example, weights_example, threshold_example)
    phi_plus_example, phi_minus_example,  phi_plus_example_ranking, phi_minus_example_ranking = \
        promethee1(pref_matrix_example, data_example)
    print(promethee2(phi_plus_example, phi_minus_example, data_example))
