import pandas as pd
import numpy as np


def concordance_matrix_iv(data, direction, weights):
    conc_matrix = pd.DataFrame(
        np.zeros((len(data), len(data))), index=data.index, columns=data.index)
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                pref = 0
                for col, w in weights.items():
                    diff = data.loc[i, col] - data.loc[j, col] if direction[col] == 'max' \
                        else data.loc[j, col] - data.loc[i, col]
                    if diff >= 0:
                        pref += w
                conc_matrix.iloc[i, j] = pref / sum(weights.values())
    return conc_matrix


def non_veto_matrix(data, directions, veto):
    veto_matrix = pd.DataFrame(
        np.zeros((len(data), len(data))), index=data.index, columns=data.index)
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                veto_matrix.iloc[i, j] = 1
                for col, dire in directions.items():
                    diff = data.loc[j, col] - data.loc[i, col] if dire == 'max' \
                        else data.loc[i, col] - data.loc[j, col]
                    if diff >= veto[col]:
                        veto_matrix.iloc[i, j] = 0
                        break
    return veto_matrix


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
    veto_example = {'C1': 45, 'C2': 29,
                    'C3': 550, 'C4': 6, 'C5': 4.5, 'C6': 4.5}
    print(concordance_matrix_iv(data_example, directions_example, weights_example))
    print(non_veto_matrix(data_example, directions_example, veto_example))
