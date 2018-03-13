from core.labels import Vision
from core.crypt import Aes
import sys
import pytest

# with pytest.raises(Exception) as excinfo:
Vision.detect_labels('{}'.format(sys.argv[1]))

# with pytest.raises(Exception) as excinfo:
# 	Aes.encrypt_file(in_filename='img/alcohol.jpg',out_filename='encrypted.jpg')
