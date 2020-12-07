import logging
import uuid
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class UuidExtension(Extension):

    def __init__(self):
        logger.info('init UUID extension')
        super(UuidExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        generated_uuids = []
        accepted_versions = ["v1", "v3", "v4", "v5"]
        args = None
        v = "v4"
        name = "python.org"

        args_string = event.get_argument()

        if args_string is not None:
            args = args_string.split(' ')  # [0]v5 [1]name

        try:
            if args is not None and args[0] in accepted_versions:
                v = args[0]
        except IndexError:
            pass

        try:
            if args is not None and args[1] is not None:
                name = args[1]
        except IndexError:
            pass

        if v == "v1":
            generated_uuids.append(["UUID v1", str(uuid.uuid1())])
        elif v == "v4":
            generated_uuids.append(["UUID v4", str(uuid.uuid4())])
        elif v == "v3":
            generated_uuids.append(["UUID v3 DNS", str(uuid.uuid3(uuid.NAMESPACE_DNS, name))])
            generated_uuids.append(["UUID v3 URL", str(uuid.uuid3(uuid.NAMESPACE_URL, name))])
        elif v == "v5":
            generated_uuids.append(["UUID v5 DNS", str(uuid.uuid5(uuid.NAMESPACE_DNS, name))])
            generated_uuids.append(["UUID v5 URL", str(uuid.uuid5(uuid.NAMESPACE_URL, name))])

        for desc, uuid_value in generated_uuids:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=uuid_value,
                                             description=desc,
                                             highlightable=False,
                                             on_enter=CopyToClipboardAction(uuid_value)
                                             ))
        return RenderResultListAction(items)


if __name__ == '__main__':
    UuidExtension().run()


