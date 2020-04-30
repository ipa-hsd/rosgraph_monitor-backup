from rosgraph_monitor.observer import TopicObserver
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from diagnostic_msgs.msg import DiagnosticStatus, KeyValue


class QualityObserver(TopicObserver):
    def __init__(self, name):
        topics = [("/power_load", Float32)]     # list of pairs

        super(QualityObserver, self).__init__(
            name, 10, topics)

    def calculate_attr(self, msgs):
        status_msg = DiagnosticStatus()

        attr = msgs[0].data
        print("{0}".format(msgs[0].data))

        status_msg = DiagnosticStatus()
        status_msg.level = DiagnosticStatus.OK
        status_msg.name = self._id
        status_msg.values.append(
            KeyValue("energy", str(attr)))
        status_msg.message = "QA status"

        return status_msg
