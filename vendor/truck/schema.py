from elapi import base_schema, fields, exceptions

from marshmallow import pre_load


class ApplicantSchema(base_schema.Schema):

    name = fields.String(required=True)


class StreetSchema(base_schema.Schema):

    street = fields.String(required=True)


class TruckSchema(base_schema.Schema):

    locationid = fields.Integer(required=False)
    applicant = fields.String(required=True)
    facilitytype = fields.Integer(required=False, default=1)
    status = fields.Integer(required=False)
    cnn = fields.Integer(required=False)
    latitude = fields.Float(required=False)
    longitude = fields.Float(required=False)
    full_address = fields.String(required=False)
    address = fields.String(required=False)
    permit =fields.String(required=False)
    busy = fields.Boolean(required=False, default=False)
    approved = fields.DateTime(required=False, format='%m/%d/%Y')
    expiration = fields.DateTime(required=False, format='%m/%d/%Y')


class ExpirationSchema(base_schema.Schema):
    date = fields.DateTime(required=True, format='%m/%d/%Y')


class PointSchema(base_schema.Schema):
    x = fields.Float(required=True)
    y = fields.Float(required=True)


class AssignTruckSchema(base_schema.Schema):
    points = fields.Nested(PointSchema, many=True)

    @pre_load
    def check_points(self, data):
        if len(data["points"]) == 0:
            raise exceptions.WrongDataException("Pass atleast one point")
