from google.cloud import storage
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

from website import PROJECT_ROOT
from website.dog_classes import classes as breeds

upload_folder = PROJECT_ROOT / "website/static/uploads"
num_dog_breeds = 120

client = storage.Client()
bucket = client.get_bucket("dognet")
blob = bucket.blob("dognet-convnext_large.pth")

blob = bucket.blob("dognet-convnext_large.pth")
blob.download_to_filename("/models/dognet-convnext_large.pth")

model_path = "/models/dognet-convnext_large.pth"


def generate_dog(file):
    file_path = upload_folder / file.filename

    model = models.convnext_large(pretrained=True)
    model.classifier[-1] = torch.nn.Linear(
        model.classifier[-1].in_features, num_dog_breeds
    )
    model.load_state_dict(torch.load(model_path), map_location=torch.device("cpu"))
    image_path = str(file_path)
    image = Image.open(image_path)

    # transfrom image into tensor
    transform = transforms.Compose(
        [
            transforms.RandomResizedCrop(224),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
    input_tensor = transform(image).unsqueeze(0)
    # evaluate tensor
    model.eval()
    # Perform inference
    with torch.no_grad():
        output = model(input_tensor)

    probabilities = torch.nn.functional.softmax(output, dim=1)
    top3_probs, top3_indices = torch.topk(probabilities, 3)

    results = ""
    for i in range(3):
        results += f"  {breeds[top3_indices[0][i].item()][10:]}, Probability: {str(top3_probs[0][i].item() * 100)[:5]}%\n"

    return results
