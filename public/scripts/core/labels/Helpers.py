import json
import os

class Helper(object):
    @classmethod
    def get_desc(cls, label):
        dir_path = os.path.dirname(os.path.realpath('tags.json'))
        result = {}
        with open(dir_path+'/public/scripts/meta/tags.json') as fh:
            data = json.load(fh)

        for tags in data:
            for tag in data[tags]:
                for props in label:
                    if tag == props.description:
                        result[tag] = round((props.score*100), 2)
        return result
