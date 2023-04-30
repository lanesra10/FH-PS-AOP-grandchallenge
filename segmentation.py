import logging
import torch
from tqdm import tqdm

# todo import your network structure
from model.resnet34 import Resnet34

class MySegmentation:
    def __init__(self, path_model):
        # network parameters
        self.model = Resnet34()
        self.path_model = path_model
        self.mean = None
        self.std = None
        self.device = torch.device('cpu' if not torch.cuda.is_available() else 'cuda')

    def load_model(self):
        self.mean = torch.FloatTensor([0.7481, 0.5692, 0.7225]).to(self.device)
        self.std = torch.FloatTensor([0.1759, 0.2284, 0.1792]).to(self.device)

        if torch.cuda.is_available():
            print("Model loaded on CUDA")
            self.model.load_state_dict(torch.load(self.path_model))
        else:
            print("Model loaded on CPU")
            self.model.load_state_dict(torch.load(self.path_model, map_location='cpu'))

        self.model.to(self.device)

        logging.info("Model loaded. Mean: {} ; Std: {}".format(self.mean, self.std))
        return True

    def process_image(self, input_image):
        device = torch.device('cpu' if not torch.cuda.is_available() else 'cuda')
        self.model.eval()
        # todo Image preprocessing
        image = input_image
        image = image.to(device=device, dtype=torch.float32)

        # Putting images into the network
        output = self.model(image)

        # todo  Post processing of predicted images

        return output


