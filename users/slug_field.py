from transliterate import translit
from autoslug import AutoSlugField


class CyrillicAutoSlugField(AutoSlugField):
    def slugify(self, value):
        return translit(value, 'ru', reversed=True)
