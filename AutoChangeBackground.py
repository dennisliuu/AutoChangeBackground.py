import os

import xml.etree.cElementTree as ET

a = os.listdir('/usr/share/backgrounds')

background = ET.Element("background")

starttime = ET.SubElement(background, "starttime")
ET.SubElement(starttime, "year").text = "2009"
ET.SubElement(starttime, "month").text = "08"
ET.SubElement(starttime, "day").text = "04"
ET.SubElement(starttime, "hour").text = "00"
ET.SubElement(starttime, "minute").text = "00"
ET.SubElement(starttime, "second").text = "00"

for i in a:
	static = ET.SubElement(background, "static")
	ET.SubElement(static, "duration").text = "1795.0"
	ET.SubElement(static, "file").text = '/usr/share/backgrounds/' + i

	transition = ET.SubElement(background, "transition")
	ET.SubElement(transition, "duration").text = "5.0"
	ET.SubElement(transition, "from").text = '/usr/share/backgrounds/' + i
	try:
		ET.SubElement(transition, "to").text = '/usr/share/backgrounds/' + a[a.index(i) + 1]	
	except Exception as e:
		ET.SubElement(transition, "to").text = '/usr/share/backgrounds/' + a[0]
	

tree = ET.ElementTree(background)
tree.write("bionic.xml")
