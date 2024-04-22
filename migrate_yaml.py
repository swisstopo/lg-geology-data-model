import yaml
import json
import yaml
from yaml.loader import SafeLoader

filename = 'datamodel.yaml'


import datetime
from json import JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

def set_description(obj, de):

    obj['de'] = obj.get('de')
    obj['fr'] = ''

    return obj
with open(f'{filename}', 'r') as f:

        data = yaml.load(f, Loader=SafeLoader)

        for theme in data.get('themes'):
            de = theme.get('description')
            for cls in theme.get('classes'):
                de = cls.get('description')
                cls['de'] = de
                cls['fr']= '-'

        print(json.dumps(data, indent=4, cls=DateTimeEncoder))
