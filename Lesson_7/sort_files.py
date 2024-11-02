# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import chdir
from pathlib import Path


def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {
            Path('Videos'): ['mp4', 'mov', 'mkv'],
            Path('Images'): ['png', 'jpg', 'jpeg']
        }
    reverse_groups = {}
    for target_dir, ext_lst in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True)
        for ext in ext_lst:
            reverse_groups[f'.{ext}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(
                reverse_groups[file.suffix] / file.name
            )


if __name__ == '__main__':
    sort_files(Path(r'C:\Users\user\Python_immersion\Lesson_7'))
