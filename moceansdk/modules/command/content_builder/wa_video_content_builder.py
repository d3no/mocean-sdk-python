from moceansdk.modules.command.content_builder.wa_rich_media_content_builder_basic import WaRichMediaContentBuilderBasic


class WaVideoContentBuilder(WaRichMediaContentBuilderBasic):

    def type(self):
        return 'video'