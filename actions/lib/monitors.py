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
        _monitor_tags = kwargs.pop("monitor_tags","")
        _group_states = kwargs.pop("group_states","")
        monitor_tags = [_tag.strip() for _tag in _monitor_tags.split(",")] if _monitor_tags else None
        group_states = [_state.strip() for _state in group_states] if _group_states else None
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
