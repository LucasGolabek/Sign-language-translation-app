import torch.nn as nn


class ASLDeepNeuralNetwork(nn.Module):
    def __init__(self, _input_size, _output_size):
        super().__init__()
        # for linear_model.pth
        """self.network = nn.Sequential(
            nn.Linear(_input_size, 128),
            nn.ReLU(),
            nn.Linear(128, _output_size)
        )"""

        # for old_conv_model.pth
        """self.network = nn.Sequential(
            nn.Conv2d(3, 128, 3, padding="same"),
            nn.MaxPool2d((4, 4)),
            nn.ReLU(),
            nn.Conv2d(128, 10, 3, padding="same"),
            nn.MaxPool2d((2, 2)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(25*25*10, _output_size)
        )"""

        # for new_conv_model.pth
        self.network = nn.Sequential(
            nn.Conv2d(3, 128, 3, padding="same"),  # 3x3x3x128
            nn.MaxPool2d((4, 4)),
            nn.ReLU(),
            nn.Conv2d(128, 64, 3, padding="same"),
            nn.MaxPool2d((2, 2)),
            nn.ReLU(),
            nn.Conv2d(64, 10, 3, padding="same"),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(25 * 25 * 10, _output_size)
        )

    def forward(self, xb):
        return self.network(xb.view(xb.size(0), -1))
