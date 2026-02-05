from .resources import UpdateCallerIDResource
from .services import UpdateCallerIDService


class Plugin:

    def load(self, dependencies):
        api = dependencies['api']
        ari = dependencies['ari']

        service = UpdateCallerIDService(ari.client)

        api.add_resource(UpdateCallerIDResource, '/applications/<application_uuid>/calls/<call_id>/callerid', resource_class_args=[service])
