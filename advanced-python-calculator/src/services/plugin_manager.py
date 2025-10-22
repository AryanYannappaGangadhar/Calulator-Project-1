class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name, plugin):
        if plugin_name not in self.plugins:
            self.plugins[plugin_name] = plugin
            print(f"Plugin '{plugin_name}' loaded.")
        else:
            print(f"Plugin '{plugin_name}' is already loaded.")

    def unload_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            print(f"Plugin '{plugin_name}' unloaded.")
        else:
            print(f"Plugin '{plugin_name}' not found.")

    def execute_plugin(self, plugin_name, *args, **kwargs):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(*args, **kwargs)
        else:
            print(f"Plugin '{plugin_name}' not found.")
            return None

    def list_plugins(self):
        return list(self.plugins.keys())