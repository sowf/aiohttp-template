import peewee


class BaseModel(peewee.Model):
    char_field = peewee.CharField(max_length=4096)
