import sys
import pandas as pd
import numpy as np

def w_norm(data, weight):
    norm = data.copy()
    for col in data.columns[1:]:
        norm[col] = data[col] / np.sqrt(np.sum(data[col]**2))

    wnorm = norm.copy()
    for col, w in zip(data.columns[1:],weight.split(',')):
        wnorm[col] = norm[col]*float(w)
    
    return wnorm       

def get_id_sol(w_norm_matrix, impact):
    best = np.zeros(len(impact.split(',')))
    worst = np.zeros(len(impact.split(',')))
    
    for i, imp in enumerate(impact.split(',')): 
        if imp == '+':
            best[i] = np.max(w_norm_matrix.iloc[:, i + 1])
            worst[i] = np.min(w_norm_matrix.iloc[:, i + 1])
        elif imp == '-':
            best[i] = np.min(w_norm_matrix.iloc[:, i + 1])
            worst[i] = np.max(w_norm_matrix.iloc[:, i + 1])

    return best, worst

def get_score(w_norm_matrix, best, worst):
    sn = np.sqrt(np.sum((w_norm_matrix.iloc[:, 1:] - worst)**2, axis=1))
    sp = np.sqrt(np.sum((w_norm_matrix.iloc[:, 1:] - best)**2, axis=1))
    
    pi = sn / (sn + sp)
    
    return pi

def topsis(inputfile, weight, impact):
    try:
        
        data = pd.read_csv(inputfile)
        #check no of columns
        if len(data.columns)<3:
            print("Input file must have more than 3 columns")
            return
        #check for non numerical columns
        non_numerical_columns = data.iloc[:, 1:].select_dtypes(exclude='number').columns
        if not non_numerical_columns.empty:
            print("Data has non-numerical columns")
            return
        #check weight, impact and no of columns
        if len(weight.split(','))!=len(impact.split(',')) or len(weight.split(','))!=len(data.columns)-1:
            print("Number of weights, impacts and columns should be equal")
            return
        
        if not all(imp in ['+', '-'] for imp in impact.split(',')):
            print("Error: Impacts must be either +ve or -ve.")
            return
        
        w_norm_matrix=w_norm(data, weight)
        best, worst=get_id_sol(w_norm_matrix, impact)
        score=get_score(w_norm_matrix,best, worst)
        
        rank = pd.Series(score, name='Topsis_Score').rank(ascending=False)

        result_data = pd.concat([data.iloc[:, 0], pd.Series(score, name='Topsis_Score'), rank], axis=1)
        
        print(result_data)

    except FileNotFoundError:
        print(f"Error: File not found - {inputfile}")

if __name__ == "__main__":
    # Check for correct number of parameters
    if len(sys.argv) != 4:
        print("Valid input: topsis <InputDataFile> <Weights> <Impacts>")
    else:
        inputfile, weight, impact = sys.argv[1], sys.argv[2], sys.argv[3]
        topsis(inputfile, weight, impact)
