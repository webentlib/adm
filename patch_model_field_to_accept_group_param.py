from django.db.models.fields import Field, NOT_PROVIDED


def __init__(
    self,
    verbose_name=None,
    name=None,
    primary_key=False,
    max_length=None,
    unique=False,
    blank=False,
    null=False,
    db_index=False,
    rel=None,
    default=NOT_PROVIDED,
    editable=True,
    serialize=True,
    unique_for_date=None,
    unique_for_month=None,
    unique_for_year=None,
    choices=None,
    help_text="",
    db_column=None,
    db_tablespace=None,
    auto_created=False,
    validators=(),
    error_messages=None,
    db_comment=None,
    db_default=NOT_PROVIDED,
    group=None,  # Added
):
    self.group = group  # Added
    self.name = name
    self.verbose_name = verbose_name  # May be set by set_attributes_from_name
    self._verbose_name = verbose_name  # Store original for deconstruction
    self.primary_key = primary_key
    self.max_length, self._unique = max_length, unique
    self.blank, self.null = blank, null
    self.remote_field = rel
    self.is_relation = self.remote_field is not None
    self.default = default
    self.db_default = db_default
    self.editable = editable
    self.serialize = serialize
    self.unique_for_date = unique_for_date
    self.unique_for_month = unique_for_month
    self.unique_for_year = unique_for_year
    self.choices = choices
    self.help_text = help_text
    self.db_index = db_index
    self.db_column = db_column
    self.db_comment = db_comment
    self._db_tablespace = db_tablespace
    self.auto_created = auto_created

    # Adjust the appropriate creation counter, and save our local copy.
    if auto_created:
        self.creation_counter = Field.auto_creation_counter
        Field.auto_creation_counter -= 1
    else:
        self.creation_counter = Field.creation_counter
        Field.creation_counter += 1

    self._validators = list(validators)  # Store for deconstruction later

    self._error_messages = error_messages  # Store for deconstruction later


Field.__init__ = __init__
Field.non_db_attrs += ('group',)  # Не отражается на базе, соответственно — не требует и не триггерит миграции
