from torchvision.models.resnet import resnet34
from torchvision.models.segmentation.segmentation import FCNHead
import torch.nn as nn
import torch.nn.functional as F
import torch

class Resnet34(nn.Module):
    def __init__(self):
        super(Resnet34, self).__init__()
        self.model = resnet34(pretrained=False, progress=True)
        self.classifier = FCNHead(512, 3)
        self.conv1 = self.model.conv1
        self.bn1 = self.model.bn1
        self.relu = self.model.relu
        self.maxpool = self.model.maxpool
        self.down1 = self.model.layer1
        self.down2 = self.model.layer2
        self.down3 = self.model.layer3
        self.down4 = self.model.layer4

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x1 = self.maxpool(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x = self.classifier(x5)
        out = F.interpolate(x, (256, 256), mode='bilinear', align_corners=True)
        return out

if __name__ == '__main__':
    net = Resnet34()
    input = torch.randn(1, 3, 256, 256)
    out = net(input)
    print(out.shape)
