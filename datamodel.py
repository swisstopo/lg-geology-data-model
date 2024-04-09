import yaml
import json
import pprint


with open('coded_domains.json', 'r') as f:
    domains = json.load(f)


def get_coded_values(value):

        if value in domains.keys():

            domain = domains.get(value)
            #print(f"  {name}, {type} , {value}")
            if domain.get('type') == 'CodedValue':
                return  domain.get('codedValues')

        return {}


def main(config_file):

    with open(config_file, "rt",  encoding='utf8') as f:
        model = yaml.load(f, Loader=yaml.FullLoader)


        # print(json.dumps(model, indent=4))

        for theme in model['themes']:
            print("")
            print(f"# Thema {theme.get('name')}")
            for cls in theme.get('classes'):

                print(f"## Klasse {cls.get('name')}")
                desc = cls.get('desc')
                if desc:
                    print(f"    _{desc}_")
                attributes = cls.get('attributes')
                if attributes:
                    for att in attributes:
                        name = att.get('name')
                        type = att.get('type')
                        value = att.get('value')
                        desc = att.get('desc', '')
                        print(f"** Attribute {name}** _{desc}_")

                        if type == 'CD' and value is not None:
                            pairs = get_coded_values(value)
                            print("|Geolcode|German|French|")
                            print("|----------|--------------------|--------------------|")
                            for k  in sorted(pairs):
                                print(f"|    {k:>10}| {pairs[k]}||")











if __name__ == "__main__":
    main("datamodel.yaml")


