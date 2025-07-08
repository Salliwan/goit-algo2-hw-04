from pathlib import Path

path = Path('cats.txt')


def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats.append({"id": cat_id, "name": name, "age": age})
    except Exception as e:
        print(f'{e} with file')
    return cats


print(get_cats_info(path))
