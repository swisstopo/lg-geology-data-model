import yaml
import json
import pprint


def main(config_file):

    with open(config_file, "rt",  encoding='utf8') as f:
        model = yaml.load(f, Loader=yaml.FullLoader)


        # print(json.dumps(model, indent=4))

        for theme in model['themes']:
            try:
                for cls in theme['classes']:
                    print(cls['name'])
            except KeyError as e:
                print(e)




if __name__ == "__main__":
    main("datamodel.yaml")
