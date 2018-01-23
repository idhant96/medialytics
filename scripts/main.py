from google.cloud import vision
from google.cloud.vision import types

class Main(object):
	def set_image(self, img):
        """
        set image instance with the given url
        :param img:
        :return:
        """
        self.image_path = '{}'.format(img)
        # set image instance
        self.image = cv2.imread(self.image_path,0)
