"""
Get the current kubernetes context and namespace
from KUBECONFIG=~/.kube/config
"""

from ..utils import BasicSegment
import os
import yaml


def get_kube_context():
    """Get the current kubernetes context"""
    kubeconfig = os.path.expanduser('~/.kube/config')
    with open(kubeconfig) as file:
        kubeconfig = yaml.load(file, Loader=yaml.FullLoader)
    return kubeconfig['current-context']


def get_kube_namespace():
    """Get the current kubernetes namespace"""
    kubeconfig = os.path.expanduser('~/.kube/config')
    with open(kubeconfig) as file:
        kubeconfig = yaml.load(file, Loader=yaml.FullLoader)
    return kubeconfig['contexts'][0]['context']['namespace']


def add_k8s_segment(powerline):
    context = get_kube_context()
    namespace = get_kube_namespace()
    if powerline.segment_conf("k8s", "mode") == "context":
        powerline.append(' {} '.format(context), powerline.theme.KUBE_CONTEXT_FG,
                         powerline.theme.KUBE_CONTEXT_BG)
    elif powerline.segment_conf("k8s", "mode") == "namespace":
        powerline.append(' {} '.format(namespace), powerline.theme.KUBE_CONTEXT_FG,
                         powerline.theme.KUBE_CONTEXT_BG)
    elif powerline.segment_conf("k8s", "mode") == "both":
        powerline.append(' {}:{} '.format(context, namespace), powerline.theme.KUBE_CONTEXT_FG,
                         powerline.theme.KUBE_CONTEXT_BG)
        return


class Segment(BasicSegment):
    def add_to_powerline(self):
        add_k8s_segment(self.powerline)
