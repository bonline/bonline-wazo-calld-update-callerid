class UpdateCallerIDService:
    def __init__(self, ari):
        self._ari = ari

    def update_caller_id(self, call_id, request_data):
        """ Use CALLERID to update the caller id shown to the callee
        https://www.voip-info.org/asterisk-func-callerid/
        """
        try:
            self._ari.channels.setChannelVar(
                channelId=call_id,
                variable='CALLERID(all)',
                value=request_data["caller_id"]
            )
            return {}, 204
        except Exception as e:
            return {'error': str(e)}, 500
