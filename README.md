# bonline-wazo-calld-update-callerid

## Installation
Install using wazo-plugind-cli directly from the GitHub repo:

`sudo wazo-plugind-cli -c "install git https://github.com/bonline/bonline-wazo-calld-update-callerid --ref master"`

We can change the ref to point to the branch we want to use, eg testing.

The python code will be installed to the python dist package location, such as `/usr/local/lib/python3.11/dist-packages/bonline_wazo_calld_update_callerid/`, which is used by `wazo-calld` to configure and enable the plugin.

The config will be installed to `/etc/wazo-calld/conf.d/callerid.yml`.


To uninstall the plugin, we should use the plugin name like so:
`sudo wazo-plugind-cli -c "uninstall bonline/bonline-wazo-calld-update-callerid"`


## Troubleshooting

Output will appear in the calld logs, in `/var/log/wazo-calld.log`.
