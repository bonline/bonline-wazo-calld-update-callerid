class UpdateCallerIDService:
    def __init__(self, ari):
        self._ari = ari

    def update_caller_id(self, call_id, request_data):
        """ Updates the CALLERID seen by the callee.
        Supports: overwrite, prepend, append
        """
        new_text = request_data["caller_id"]
        mode = request_data["mode"]

        try:
            if mode == "overwrite":
                final_name = new_text
            else:
                res = self._ari.channels.getChannelVar(
                    channelId=call_id,
                    variable='CALLERID(name)'
                )
                current_name = res.get('value', '')

                if mode == "prepend":
                    final_name = f"{new_text}{current_name}"
                elif mode == "append":
                    final_name = f"{current_name}{new_text}"
                else:
                    final_name = new_text

            self._ari.channels.setChannelVar(
                channelId=call_id,
                variable='CALLERID(name)',
                value=final_name
            )

            return {}, 204

        except Exception as e:
            return {'error': str(e)}, 500
