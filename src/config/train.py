from dataclasses import dataclass
from typing import Type
from torch import nn
from torch.utils.data import Dataset
import torch

@dataclass
class TrainConfig:
    dataset: Type[Dataset]
    net: nn.Module
    epoch_amount: int 
    learning_rate: float
    early_stopping: int
    loss_f: nn.Module
    optim: Type[torch.optim.Optimizer]