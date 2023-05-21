
class ToxWatchMonitor:
    """ base class ToxWatchMonitor accepts a MonitorPlugin parameter in its constructor. \
    The ToxWatchMonitor class has methods start_monitoring and stop_monitoring that are \
    expected to be implemented by its subclasses."""
    def __init__(self, monitor_plugin):
        self.monitor_plugin = monitor_plugin

    def start_monitoring(self):
        pass

    def stop_monitoring(self):
        pass


class InputMonitor(ToxWatchMonitor):
    def __init__(self, monitor_plugin):
        super().__init__(monitor_plugin)

    def start_monitoring(self):
        print("Input monitoring started")

    def stop_monitoring(self):
        print("Input monitoring stopped")


class AdversarialDriftMonitor(ToxWatchMonitor):
    def __init__(self, monitor_plugin):
        super().__init__(monitor_plugin)

    def start_monitoring(self):
        print("Adversarial drift monitoring started")

    def stop_monitoring(self):
        print("Adversarial drift monitoring stopped")


class ModelMonitor(ToxWatchMonitor):
    def __init__(self, monitor_plugin):
        super().__init__(monitor_plugin)

    def start_monitoring(self):
        print("Model monitoring started")

    def stop_monitoring(self):
        print("Model monitoring stopped")
