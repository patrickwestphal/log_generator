from special.vocab import has_data, has_purpose, has_recipient, has_storage, \
    has_processing


class Policy(object):
    def __init__(
            self, data_classes, purpose_classes, recipient_classes,
            storage_classes, processing_classes):

        self.data_classes = data_classes
        self.purpose_classes = purpose_classes
        self.recipient_clsses = recipient_classes
        self.storage_classes = storage_classes
        self.processing_classes = processing_classes

    def get(self, prop_uri):
        if prop_uri == has_data:
            return self.data_classes
        elif prop_uri == has_purpose:
            return self.purpose_classes
        elif prop_uri == has_recipient:
            return self.recipient_clsses
        elif prop_uri == has_storage:
            return self.storage_classes
        elif prop_uri == has_processing:
            return self.processing_classes
        else:
            raise RuntimeError(
                'Property URI not part of the SPECIAL vocabulary: %s' %
                str(prop_uri))
