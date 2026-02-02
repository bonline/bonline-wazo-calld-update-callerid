from marshmallow import (
    fields,
    Schema,
)
from marshmallow.validate import Length


class UpdateCallerIDSchema(Schema):
    caller_id = fields.Str(validate=Length(min=1))

    class Meta:
        strict = True


update_caller_id_schema = UpdateCallerIDSchema()
