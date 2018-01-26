from google.cloud import vision
from google.cloud.vision import types
import io


class Vision(object):
    google_vision_client = vision.ImageAnnotatorClient()
    image_path = ''
    image = None
    data = None

    @staticmethod
    def get_data(path):
        with io.open(path, 'rb') as image_file:
            data = image_file.read()
        return data

    @classmethod
    def detect_labels(cls, img):
        cls.image_path = '{}'.format(img)
        data = cls.get_data(cls.image_path)
        vision_image = types.Image(content=data)
        label_detection = cls.google_vision_client.label_detection(image=vision_image)
        labels = label_detection.label_annotations
        safe_search = cls.google_vision_client.safe_search_detection(image=vision_image)
        safe_annotations = safe_search.safe_search_annotation
        likelihood = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        print('adult: {}'.format(likelihood[safe_annotations.adult]))
        print('medical: {}'.format(likelihood[safe_annotations.medical]))
        print('spoofed: {}'.format(likelihood[safe_annotations.spoof]))
        print('violence: {}'.format(likelihood[safe_annotations.violence]))
        for label in labels:
            print(label.description)