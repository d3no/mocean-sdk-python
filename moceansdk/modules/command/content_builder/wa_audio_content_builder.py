from moceansdk.modules.command.content_builder.wa_rich_media_content_builder_basic import WaRichMediaContentBuilderBasic


class WaAudioContentBuilder(WaRichMediaContentBuilderBasic):

    def type(self):
        return 'audio'