class UpdateCallerIDService:
    def __init__(self, ari):
        self._ari = ari

    def update_caller_id(self, call_id, request_data):
        # We target the CONNECTEDLINE function with the 'i' flag
        # to trigger an immediate SIP update frame

        try:
            self._ari.channels.setChannelVar(
                channelId=call_id,
                variable='CONNECTEDLINE(name,i)',
                value=request_data["caller_id"]
            )
            return {}, 204
        except Exception as e:
            return {'error': str(e)}, 500
