import os
import cv2
from cv2 import dnn_superres
 

WORKDIR = os.path.abspath(os.path.dirname(__file__))

def upscale(input_path: str, output_path: str, model_path: str = os.path.join(WORKDIR, 'EDSR_x2.pb')) -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    image = cv2.imread(input_path)
    result = scaler.upsample(image)
    cv2.imwrite(output_path, result)

def example():
    upscale(os.path.join(WORKDIR, 'lama_300px.png'), os.path.join(WORKDIR, 'lama_600px.png'))  