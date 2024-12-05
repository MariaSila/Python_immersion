from pathlib import Path
from os import walk, path
from collections import namedtuple
import logging
import argparse

Dir_info = namedtuple('Dir_info', ['name', 'extension', 'type', 'parent'])


logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    format='{levelname}: {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def obj_dir(directory):
    if isinstance(directory, str):
        directory = Path(directory)
    if not path.isdir(directory):
        raise ValueError(f'Директория {directory} не найдена')

    for root, dirs, files in walk(directory):
        for name in dirs + files:
            path_d = path.join(root, name)
            if path.isdir(path_d):
                info_dir = Dir_info(name, None, 'Directory', path.basename(root))
            else:
                new_name = name[:name.find('.')]
                ext = name[name.find('.') + 1:]
                info_dir = Dir_info(new_name, ext, 'File', path.basename(root))

            logger.info(f'Name: {info_dir.name}, extension: {info_dir.extension}, '
                        f'type: {info_dir.type}, parent: {info_dir.parent}')


if __name__ == '__main__':
    try:
        obj_dir(Path.cwd())
    except ValueError as e:
        print(e)
