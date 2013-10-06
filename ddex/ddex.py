import xml.etree.cElementTree as ET

class DDEX:

	def __init__(self, product_release):
		self.product_release = product_release

	def write(self):
		root =  ET.Element("ernm:NewReleaseMessage", {'MessageSchemaVersionId': 'ern/341', 'LanguageAndScriptCode': 'en', 'xs:schemaLocation': 'http://ddex.net/xml/ern/341 http://ddex.net/xml/ern/341/release-notification.xsd', 'xmlns:ernm': 'http://ddex.net/xml/ern/341', 'xmlns:xs':'http://www.w3.org/2001/XMLSchema-instance'})
		releaseList = ET.SubElement(root,"ReleaseList")
		releaseList.append(self.__write_product_release())
		tree = ET.ElementTree(root)
		tree.write("file.xml")
	
	def __write_product_release(self):
		return self.product_release.write()
