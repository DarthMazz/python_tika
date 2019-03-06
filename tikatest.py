from tikapp import TikaApp

tika_client = TikaApp(file_jar="/Users/yma2/Documents/_garage/python/cxm/tika/tika-app-1.20.jar")

analyzeFile = "/Users/yma2/Downloads/Azure_Developer_Guide_eBook_ja-JP.pdf"
print(tika_client.detect_content_type(analyzeFile))
print(tika_client.detect_language(analyzeFile))
print(tika_client.extract_only_content(analyzeFile))
print(tika_client.extract_only_metadata(analyzeFile))