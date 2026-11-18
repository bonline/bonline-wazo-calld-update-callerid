from wazo_amid_client import Client as AmidClient

from .resources import UpdateCallerIDResource
from .services import UpdateCallerIDService


class Plugin:

    def load(self, dependencies):
        api = dependencies['api']
        ari = dependencies['ari']
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']

        amid_client = AmidClient(**config['amid'])
        token_changed_subscribe(amid_client.set_token)

        service = UpdateCallerIDService(ari.client, amid_client)

        api.add_resource(UpdateCallerIDResource, '/applications/<application_uuid>/calls/<call_id>/callerid', resource_class_args=[service])
