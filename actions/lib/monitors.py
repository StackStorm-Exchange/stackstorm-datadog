from base import DatadogBaseAction
from datadog import api


class DatadogCreateMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.create(**kwargs)


class DatadogDeleteMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.delete(kwargs.pop("monitor_id"))


class DatadogEditMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.update(kwargs.pop("monitor_id"), **kwargs)


class DatadogGetAllMonitors(DatadogBaseAction):
    def _run(self, **kwargs):
        monitor_tags_raw = kwargs.pop("tags","")
        group_states_raw = kwargs.pop("group_states","")
        monitor_tags = [tag.strip() for tag in monitor_tags_raw.split(",")] if monitor_tags_raw else None
        group_states = [state.strip() for state in group_states_raw] if group_states_raw else None
        return api.Monitor.get_all(monitor_tags=monitor_tags, group_states=group_states, **kwargs)


class DatadogGetMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.get(kwargs.pop("monitor_id"), **kwargs)


class DatadogMuteAllMonitors(DatadogBaseAction):
    def _run(self):
        return api.Monitor.mute_all()


class DatadogMuteMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.mute(kwargs.pop("monitor_id"), **kwargs)


class DatadogUnmuteAllMonitors(DatadogBaseAction):
    def _run(self):
        return api.Monitor.unmute_all()


class DatadogUnmuteMonitor(DatadogBaseAction):
    def _run(self, **kwargs):
        return api.Monitor.unmute(kwargs.pop("monitor_id"), **kwargs)
