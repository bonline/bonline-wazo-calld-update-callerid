class UpdateCallerIDService:
    def __init__(self, ari, amid):
        self._ari = ari
        self._amid = amid

    def update_caller_id(self, call_id, request_data):
        """ Updates the CALLERID seen by the callee.
        Supports: overwrite, prepend, append

        The variable is read and written over AMI rather than ARI: ARI channel
        variable operations on a Stasis channel are queued on the channel's
        control queue behind any playback in progress, which blocks this
        request until the audio finishes.
        """
        new_text = request_data["caller_id"]
        mode = request_data["mode"]

        try:
            # Snapshot read from the Stasis cache; does not queue on the channel
            channel_name = self._ari.channels.get(channelId=call_id).json['name']

            if mode == "overwrite":
                final_name = new_text
            else:
                current_name = self._get_caller_id_name(channel_name)

                if mode == "prepend":
                    final_name = f"{new_text}{current_name}"
                elif mode == "append":
                    final_name = f"{current_name}{new_text}"
                else:
                    final_name = new_text

            self._amid.action('Setvar', {
                'Channel': channel_name,
                'Variable': 'CALLERID(name)',
                'Value': final_name,
            })

            return {}, 204

        except Exception as e:
            return {'error': str(e)}, 500

    def _get_caller_id_name(self, channel_name):
        response = self._amid.action('Getvar', {
            'Channel': channel_name,
            'Variable': 'CALLERID(name)',
        })
        for message in response:
            if 'Value' in message:
                return message['Value']
        return ''
