import pandas as pd


def pareto_optimal_options(data, directions):
    pareto_optimal_rows = []
    for i, r1 in data.iterrows():
        if all(any(r1[c] > r2[c] if directions[c] == 'max' else r1[c] < r2[c] for c in data.columns[1:])
               for j, r2 in data.iterrows() if i != j):
            pareto_optimal_rows.append(r1[0])
    return pareto_optimal_rows


if __name__ == '__main__':
    data_example = pd.DataFrame({
        'house': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
        'C2': [90, 58, 60, 80, 72, 96],
        'C6': [5, 1, 7, 10, 8, 6],
    })
    directions_example = {'C2': 'max', 'C6': 'max'}
    print(pareto_optimal_options(data_example, directions_example))
