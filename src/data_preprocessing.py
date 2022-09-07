from sklearn.model_selection import train_test_split
from src.config.data_prerpocessing import DataPreproccesingConfig

def main_actions(X, y, config: DataPreproccesingConfig):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.test_size, random_state=config.random_state)
    return X_train, X_test, y_train, y_test

def main():
    config = DataPreproccesingConfig(test_size=0.4, random_state=33)
    with np.load("data.csv") as file:
        data = file['data']
    with np.load("labels.csv") as file:
        labels = file['labels']
    main_actions(data, labels, config=config)

if __name__ == "__main__":
    main()
