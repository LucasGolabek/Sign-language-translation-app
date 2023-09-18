from torchvision import transforms
from PIL import Image
import torch
import pathlib
import math
import cv2
import os
import glob

from .model import ASLDeepNeuralNetwork
from .get_configuration import get_model_conf, get_images_conf


def predict(image_list: list, window_step=50):
    def predict_big_image(tensor):
        current_classes = list()
        with torch.no_grad():
            for y in range(0, len(tensor[0])-200, window_step):
                for x in range(0, len(tensor[0][0])-200, window_step):
                    current_tensor = tensor[:, y:y+200, x:x+200]
                    current_classes.append(model.network(current_tensor.contiguous().view(1, 3, image_conf['image_edge'], image_conf['image_edge']))[0])

        best_class = (-math.inf, None)
        for window in current_classes:
            possible_class = torch.max(window, dim=0)
            if possible_class[1] < 0:
                continue
            else:
                if possible_class[0] > best_class[0]:
                    best_class = (possible_class[0], possible_class[1])
        return best_class[1]

    model_conf = get_model_conf()
    image_conf = get_images_conf()

    model = ASLDeepNeuralNetwork(model_conf['input_size'], model_conf['output_size'])
    model.load_state_dict(torch.load(f"{pathlib.Path(__file__).parent.resolve()}/prediction_models/{model_conf['file_name']}"))
    model = model.eval()

    convert_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(image_conf['mean'], image_conf['std'])
    ])

    classes = model_conf['classes']
    predicted_classes = list()

    for image in image_list:
        current_img = Image.open(image)
        try:
            image_tensor = convert_tensor(current_img)
        except RuntimeError:
            predicted_classes.append(None)
            continue
        if current_img.size[0] < 200 or current_img.size[1] < 200:
            predicted_classes.append(None)
        elif current_img.size == (200, 200):
            predicted_classes.append(classes[int(torch.max(model.network(image_tensor.view(1, 3, image_conf['image_edge'], image_conf['image_edge']))[0], dim=0)[1])])
        else:
            predicted_classes.append(classes[int(predict_big_image(image_tensor))])

    return predicted_classes


def predict_video(video_path):
    temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")

    video = cv2.VideoCapture(video_path)

    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    to_predict = list()
    count = 1
    while True:
        success, image = video.read()
        if count % 10:
            count += 1
            continue

        if not success:
            break
        cv2.imwrite(fr"{temp_path}/frame_{count}.jpg", image)
        to_predict.append(f"{temp_path}/frame_{count}.jpg")
        count += 1

    predicted = predict(to_predict, window_step=100)
    single_letter_predicted = [predicted[0] if predicted else "Not a video"] # in case of a photo instead of a video
    for i in range(1, len(predicted)):
        if predicted[i] != predicted[i-1]:
            single_letter_predicted.append(predicted[i])

    files_to_remove = glob.glob(f'{temp_path}/*')
    for f in files_to_remove:
        os.remove(f)

    return "".join(single_letter_predicted).replace("space", " ")


if __name__ == "__main__":
    result = predict(["tests/A_test.jpg",
             "tests/B_test.jpg",
             "tests/C_test.jpg",
             "tests/D_test.jpg",
             "tests/E_test.jpg",
             "tests/F_test.jpg",
             "tests/G_test.jpg",
             "tests/H_test.jpg",
             "tests/I_test.jpg",
             "tests/J_test.jpg",
             "tests/K_test.jpg",
             "tests/L_test.jpg",
             "tests/M_test.jpg",
             "tests/N_test.jpg",
             "tests/O_test.jpg",
             "tests/P_test.jpg",
             "tests/Q_test.jpg",
             "tests/R_test.jpg",
             "tests/S_test.jpg",
             "tests/T_test.jpg",
             "tests/U_test.jpg",
             "tests/V_test.jpg",
             "tests/W_test.jpg",
             "tests/X_test.jpg",
             "tests/Y_test.jpg",
             "tests/Z_test.jpg",
             "tests/space_test.jpg"])

    print(result)