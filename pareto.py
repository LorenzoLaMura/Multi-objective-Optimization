import pandas as pd


def pareto_optimal_options(data, directions):
    pareto_optimal_rows = []
    weak_pareto_optimal_rows = []
    for i, r1 in data.iterrows():
        if all(any(r1[c] > r2[c] if directions[c] == 'max' else r1[c] < r2[c] for c in data.columns[1:])
               for j, r2 in data.iterrows() if i != j):
            pareto_optimal_rows.append(r1[0])
            weak_pareto_optimal_rows.append(r1[0])
        elif all(any(r1[c] >= r2[c] if directions[c] == 'max' else r1[c] <= r2[c] for c in data.columns[1:])
                 for j, r2 in data.iterrows() if i != j):
            weak_pareto_optimal_rows.append(r1[0])
    return pareto_optimal_rows, weak_pareto_optimal_rows


if __name__ == '__main__':
    data_example = pd.DataFrame({
        'Billet': ['A', 'B', 'C', 'D', 'E'],
        'Temps': [10, 9, 8, 7.5, 6],
        'Price': [1400, 1700, 1500, 2000, 1900],
    })
    directions_example = {'Temps': 'min', 'Price': 'min'}
    print(pareto_optimal_options(data_example, directions_example))
