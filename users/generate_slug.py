import re

from unidecode import unidecode


def generate_slug(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    slug = unidecode(full_name)
    slug = re.sub(r'[^\w\s-]', '', slug).strip()
    slug = re.sub(r'[-\s]+', '-', slug).lower()
    return slug
