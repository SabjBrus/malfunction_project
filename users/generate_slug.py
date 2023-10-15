from unidecode import unidecode
import re


def generate_slug(first_name, last_name):
    # Объедините first_name и last_name с пробелом между ними
    full_name = f"{first_name} {last_name}"

    # Транслитерация текста из кириллицы в латиницу
    slug = unidecode(full_name)

    # Удаление всех символов, кроме букв, цифр и дефисов
    slug = re.sub(r'[^\w\s-]', '', slug).strip()

    # Замена пробелов на дефисы и приведение к нижнему регистру
    slug = re.sub(r'[-\s]+', '-', slug).lower()

    return slug
