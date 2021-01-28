from Components.MenuList import MenuList
from enigma import getDesktop
from Tools.Directories import resolveFilename, SCOPE_ACTIVE_SKIN, defaultPaths, SCOPE_SKIN
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from os import path
from Components.config import config
from enigma import eListboxPythonMultiContent, gFont, BT_SCALE, BT_KEEP_ASPECT_RATIO, BT_HALIGN_CENTER, BT_VALIGN_CENTER
from Tools.LoadPixmap import LoadPixmap
import skin
def PluginEntryComponent(plugin, width=900):
	if plugin.icon is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "icons/plugin.png"))
	else:
		png = plugin.icon
	if getDesktop(0).size().width() == 1920:
		return [
			plugin,
			MultiContentEntryText(pos=(170, 5), size=(width-120, 34), font=0, text=plugin.name),
			MultiContentEntryText(pos=(170, 37), size=(width-120, 28), font=1, text=plugin.description),
			MultiContentEntryPixmapAlphaTest(pos=(0, 5), size=(150, 60), png = png)
	]

	if getDesktop(0).size().width() == 1280:
		return [
			plugin,
			MultiContentEntryText(pos=(120, 5), size=(width-120, 25), font=0, text=plugin.name),
			MultiContentEntryText(pos=(120, 26), size=(width-120, 17), font=1, text=plugin.description),
			MultiContentEntryPixmapAlphaTest(pos=(10, 5), size=(100, 40), png = png)
	]

def PluginEntryComponentSelected(plugin, width=440):
	if plugin.icon is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "icons/plugin.png"))
	else:
		png = plugin.icon
	nx, ny, nh = skin.parameters.get("PluginBrowserName", (170, 5, 34))
	dx, dy, dh = skin.parameters.get("PluginBrowserDescr", (170, 37, 28))
	ix, iy, iw, ih = skin.parameters.get("PluginBrowserIcon", (0, 5, 150, 60))
	return [
		plugin,
		MultiContentEntryText(pos=(nx, ny), size=(width-nx, nh), backcolor_sel = 0xDC143C),
		MultiContentEntryText(pos=(nx, dy), size=(width-dx, dh), backcolor_sel = 0xDC143C),
		MultiContentEntryText(pos=(nx, ny), size=(width-nx, nh), font=0, text=plugin.name),
		MultiContentEntryText(pos=(nx, dy), size=(width-dx, dh), font=1, text=plugin.description),
		MultiContentEntryPixmapAlphaTest(pos=(ix, iy), size=(iw, ih), png = png, flags = BT_SCALE | BT_KEEP_ASPECT_RATIO | BT_HALIGN_CENTER | BT_VALIGN_CENTER)
	]


def PluginCategoryComponent(name, png, width=900):
	if getDesktop(0).size().width() == 1920:
		return [
			name,
			MultiContentEntryText(pos=(80, 15), size=(width-80, 34), font=0, text=name),
			MultiContentEntryPixmapAlphaTest(pos=(10, 10), size=(60, 50), png = png)
	]
	else:
		return [
			name,
			MultiContentEntryText(pos=(80, 5), size=(width-80, 25), font=0, text=name),
			MultiContentEntryPixmapAlphaTest(pos=(10, 0), size=(60, 50), png = png)
	]

def PluginDownloadComponent(plugin, name, version=None, width=440):
	if plugin.icon is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "icons/plugin.png"))
	else:
		png = plugin.icon
	if version:
		if "+git" in version:
			# remove git "hash"
			version = "+".join(version.split("+")[:2])
		elif version.startswith('experimental-'):
			version = version[13:]
		name += "  (" + version + ")"
	if getDesktop(0).size().width() == 1920:
		return [
			plugin,
			MultiContentEntryText(pos=(80, 5), size=(width-80, 34), font=0, text=name),
			MultiContentEntryText(pos=(80, 37), size=(width-80, 28), font=1, text=plugin.description),
			MultiContentEntryPixmapAlphaTest(pos=(10, 10), size=(60, 50), png = png)
	]
	else:
		return [
			plugin,
			MultiContentEntryText(pos=(80, 5), size=(width-80, 25), font=0, text=name),
			MultiContentEntryText(pos=(80, 26), size=(width-80, 17), font=1, text=plugin.description),
			MultiContentEntryPixmapAlphaTest(pos=(10, 0), size=(60, 50), png = png)
	]

class PluginList(MenuList):
	def __init__(self, list, enableWrapAround=True):
		if getDesktop(0).size().width() == 1920:
				MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
				self.l.setFont(0, gFont("Regular", 30))
				self.l.setFont(1, gFont("Regular", 22))
				self.l.setItemHeight(70)
		else:
			MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
			self.l.setFont(0, gFont("Regular", 20))
			self.l.setFont(1, gFont("Regular", 14))
			self.l.setItemHeight(50)
