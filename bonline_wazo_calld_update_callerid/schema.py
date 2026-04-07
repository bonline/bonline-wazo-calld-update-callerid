from marshmallow import (
    fields,
    Schema,
    validate,
)
from marshmallow.validate import Length


class UpdateCallerIDSchema(Schema):
    caller_id = fields.Str(validate=Length(min=1), required=True)
    mode = fields.Str(
        validate=validate.OneOf(["prepend", "overwrite", "append"]),
        load_default="prepend"
    )

    class Meta:
        strict = True


update_caller_id_schema = UpdateCallerIDSchema()
