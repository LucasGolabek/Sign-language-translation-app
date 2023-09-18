import configparser
import pathlib


def create_parser():
    config = configparser.ConfigParser()
    config.read(f'{pathlib.Path(__file__).parent.resolve()}/conf.ini')
    return config


def get_model_conf():
    config = create_parser()

    model_attrs = {
        'file_name': config['CLASSIFICATION_MODEL']['file_name'],
        'input_size': int(config['CLASSIFICATION_MODEL']['input_size']),
        'output_size': int(config['CLASSIFICATION_MODEL']['output_size']),
        'classes': eval(config['CLASSIFICATION_MODEL']['classes'])
    }

    return model_attrs


def get_images_conf():
    config = create_parser()

    images_attrs = {
        'image_edge': int(config['IMAGES']['edge']),
        'mean': eval(config['IMAGES']['mean']),
        'std': eval(config['IMAGES']['std']),
    }

    return images_attrs
