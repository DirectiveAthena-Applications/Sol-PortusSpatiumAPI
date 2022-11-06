# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
from json_framework.json_encoder.custom_json_encoder import CustomJsonEncoder
from json_framework.json_encoder.encoder_mapping import EncoderMapping


def include_in_encoder(_cls=None, **kwargs):
    # this allows the decorator to be used with or without `()`
    if _cls is not None:
        return EncoderMapping.match_model_fields(_cls)
    else:
        return EncoderMapping.match_model_fields