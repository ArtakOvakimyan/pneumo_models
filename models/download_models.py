#!pip install gdown
import gdown

urls = {
  "ResNet50V2": "https://drive.google.com/file/d/1zOyD3FFbaD-hvCHzWtZtJ2_d4uXz85av/view?usp=drive_link",
  "VGG16": "https://drive.google.com/file/d/1KGBA4QCZhiblB9CbuvqzVj8xYqBMh6IS/view?usp=drive_link",
  "VGG19": "https://drive.google.com/file/d/1GJt3vixNDD5WFkurpUN2p6j5BWDngo9P/view?usp=drive_link"
}

for k, v in urls.items():
  gdown.download(v, k, quiet=False)
