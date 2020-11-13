import torch
import torchvision
import torch.nn as nn

batch = 4
channel = 1
h = 28
w = 28

inputs = torch.rand(batch, channel, h, w)