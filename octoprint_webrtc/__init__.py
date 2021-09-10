# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class WebrtcPlugin(octoprint.plugin.SettingsPlugin,
                   octoprint.plugin.AssetPlugin,
                   octoprint.plugin.TemplatePlugin
                   ):

    # ~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            # put your plugin's default settings here
        }

    # ~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "css": ["css/webrtc.css"],
            "js": ["js/webrtc.js"]
        }

    # ~~ Template Plugin mixin

    def get_template_configs(self):
        return [{"type": "tab", "template": "webrtc_tab.jinja2", "replaces": "control", "name": "Control"}]

    # ~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "webrtc": {
                "displayName": "Webrtc Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "jneilliii",
                "repo": "OctoPrint-Webrtc",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/jneilliii/OctoPrint-Webrtc/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "Webrtc Plugin"
__plugin_pythoncompat__ = ">=3,<4"  # only python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = WebrtcPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
