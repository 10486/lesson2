from sklearn.datasets import make_moons
from src.config.data_collection import DataCollectionConfig
import pandas as pd


def main_actions(config: DataCollectionConfig):
    X, y = make_moons(n_samples=int(config.n_samples), random_state=config.random_state, noise=config.noise)
    return X,y

def main():
    config = DataCollectionConfig(n_samples=150, random_state=33, noise=0.2)
    X, y = main_actions(config=config)
    pd.Series(X).to_csv("data.csv")
    pd.Series(y).to_csv("labels.csv")

if __name__ == "__main__":
    main()