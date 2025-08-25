import pandas as pd

def to_csv(results, path):
    df = pd.DataFrame(results)
    df.to_csv(path, index=False)
    print(f"Saved results to {path}")