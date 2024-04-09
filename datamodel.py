import yaml
import json
import pprint
import pandas as pd
import sys
import datetime


from loguru import logger

logger.add("datamodel.log", backtrace=False)


with open('coded_domains.json', 'r') as f:
    domains = json.load(f)
    
    
df = pd.read_csv('../data/GeolCodeText_Trad_230317.csv', sep=';')


df = df.set_index(['GeolCodeInt'])





def get_coded_values(value):

        if value in domains.keys():

            domain = domains.get(value)
            #print(f"  {name}, {type} , {value}")
            if domain.get('type') == 'CodedValue':
                return  domain.get('codedValues')

        return {}


def main(config_file):
    
    now = datetime.datetime.now()
    
 

    with open(config_file, "rt",  encoding='utf8') as f:
        model = yaml.load(f, Loader=yaml.FullLoader)


        # print(json.dumps(model, indent=4))
        print(f"# Datenmodel GeoCover ({now.strftime('%x')})")
        print(f'![geocover](geocover.png "GeoCover")')

        for theme in model['themes']:
            print("")
            print(f"## Thema {theme.get('name','').replace('_', ' ')}")
            for cls in theme.get('classes'):

                print(f"### Klasse {cls.get('name')}")
                desc = cls.get('desc', None)
                if desc is not None:
                    print(f"_{desc}_")
                print("")
                attributes = cls.get('attributes')
                if attributes:
                    for att in attributes:
                        name = att.get('name')
                        type = att.get('type')
                        value = att.get('value')
                        desc = att.get('desc', None)
                        print(f"**Attribute {name.upper()}**")
                        if desc is not None:
                            print(f"_{desc}_")
                        print("")

                        if type == 'CD' and value is not None:
                            pairs = get_coded_values(value)
                            print("")
                            print("|Geolcode|German|French|")
                            print("|----------|--------------------|--------------------|")
                            for k  in sorted(pairs):
                                de=pairs[k]
                                try:
                                    fr = df.loc[int(k)]['FR']
                                except Exception as e:
                                    logger.error(f"{de} is not translated")
                                    fr = ''
                                
                              
                                print(f"|    {k:>10}| {de}|{fr}|")
                            print("")











if __name__ == "__main__":
    main("datamodel.yaml")


