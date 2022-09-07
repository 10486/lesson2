from dataclasses import dataclass


@dataclass
class DataCollectionConfig:
    n_samples:int
    random_state:int
    noise:float
