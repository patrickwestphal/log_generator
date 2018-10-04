from special.vocab import has_data, has_purpose, has_recipient, has_storage, \
    has_processing


class Policy(object):
    def __init__(self, data, purpose, recipient, storage, processing):
        self.data = data
        self.purpose = purpose
        self.recipient = recipient
        self.storage = storage
        self.processing = processing

    def get(self, prop_uri):
        if prop_uri == has_data:
            return self.data
        elif prop_uri == has_purpose:
            return self.purpose
        elif prop_uri == has_recipient:
            return self.recipient
        elif prop_uri == has_storage:
            return self.storage
        elif prop_uri == has_processing:
            return self.processing
        else:
            raise RuntimeError(
                'Property URI not part of the SPECIAL vocabulary: %s' %
                str(prop_uri))
