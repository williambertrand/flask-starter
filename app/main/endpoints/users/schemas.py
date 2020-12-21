from marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "date_created", "_links")

    # Smart hyperlinking
    _links = Hyperlinks(
        {"self": URLFor("user_detail", id="<id>"), "collection": URLFor("users")}
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)