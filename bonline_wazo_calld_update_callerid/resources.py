from flask import request

from wazo_calld.http import AuthResource
from wazo_calld.auth import required_acl
from .schema import update_caller_id_schema


class UpdateCallerIDResource(AuthResource):
    def __init__(self, service):
        self._service = service

    @required_acl('calld.applications.{application_uuid}.calls.{call_id}.update')
    def patch(self, call_id):
        request_body = update_caller_id_schema.load(request.get_json(force=True))
        result, status = self._service.update_caller_id(call_id, request_body)
        return result, status
