import yaml


def load_yaml(path) -> dict:
    """
    读取一个yaml文件
    :param path: 文件路径
    :return:
    """
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def write_yaml(data, path):
    """
    将对象写yaml
    :param data:
    :param path:
    :return:
    """
    with open(path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True)
