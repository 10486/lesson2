from dataclasses import dataclass


@dataclass
class DataPreproccesingConfig:
    test_size:float
    random_state:int