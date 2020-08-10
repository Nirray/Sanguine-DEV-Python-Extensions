"""
--------------------------------------------
	Sanguine Project ~ Nirray & BeHolder
	Hi, if you're reading this, feel free to use the solutions used in this file. 
	Some scripts were written a long time ago (around 2010) so they may be somewhat outdated.
	We had plans to create a server already in 2009 r/slowpoke/
	
	- Special thanks to:
	* metin2.dev/board/
	* elitepvpers.com/forum/metin2/
	* metin2zone.net/
	* m2zone.tech/

--------------------------------------------
"""
import grp
import player
import re
import item
import app
import shop
ENABLE_SPLASH_SCREEN = 0
ENABLE_ADMIN_LOGO = 1
ENABLE_BGM_PUSH = 0
ENABLE_NEW_AUTO_LOGIN = 0
ENABLE_ITEM_LONG_TOOLTIP = 1
ENABLE_TRUE_DEBUG_MODE = 1
# BeHolder
GET_CURRENT_SELECTED_VNUM = 0
GET_NEXT_REFINE_VNUM = 0

GAME_RENDER_CLOUDS = 1
GAME_RENDER_BUILDING = 1
GAME_RENDER_TREE = 1
GAME_RENDER_NOTICE = 1
GAME_RENDER_FPS_COUNT = 0
GAME_HIDE_TASKBAR = 0
GAME_SHOW_ONLYOWNNAME_AND_ITEMS = 0

# test
ACROBATIC_DODGE_SET_LEFT = 0
ACROBATIC_DODGE_SET_RIGHT = 0
ACROBATIC_DODGE_SET_DOWN = 0
ACROBATIC_DODGE_SET_UP = 0
ACROBATIC_DODGE_TIME_LEFT = 0.0
ACROBATIC_DODGE_TIME_RIGHT = 0.0
ACROBATIC_DODGE_TIME_DOWN = 0.0
ACROBATIC_DODGE_TIME_UP = 0.0

def CheckTrueDebug():
	if (ENABLE_TRUE_DEBUG_MODE and app.IsPressed(app.DIK_LSHIFT)):
		return True
	else:
		return False
def unsigned32(n):
	return n & 0xFFFFFFFFL

def CheckArmor(form):
	if (form % 10 == 9):
		return form-3
	elif (form % 10 == 8):
		return form-2
	elif (form % 10 == 7):
		return form-1
	else:
		return form

def StripColor(text):
		find = re.search('\|c([a-zA-Z0-9]{0,8})', text)
		happy_02 = "|Ehappy_02|e"
		sad_02 = "|Esad_02|e"
		tongue_04 = "|Etongue_04|e"
		happy_07 = "|Ehappy_07|e"
		angry_04 = "|Eangry_04|e"
		kiss_04 = "|Ekiss_04|e"
		love = "|Elove|e"
		embarrassed_03 = "|Eembarrassed_03|e"
		crying = "|Ecrying|e"
		text = text.replace(happy_02,':)')
		text = text.replace(sad_02,':(')
		text = text.replace(tongue_04,':P')
		text = text.replace(happy_07,':D')
		text = text.replace(angry_04,'>_<')
		text = text.replace(kiss_04,':*')
		text = text.replace(love,'<3')
		if find:
			text = text.replace(find.group(0),'')
			text = text.replace('|r','')
			text = text.replace('|h','')
			text = text.replace('|E','')
			text = text.replace('|e','')
			text = text.replace('|c','')
		return text

def CheckWrongAddon(id):
	blval = 0
	if (player.GetStatus(id) <= 0):
		blval = 1
	return blval

def CheckAddon(id):
	blval = 0
	if (player.GetStatus(id) < 0):
		blval = 1
	elif (player.GetStatus(id) == 0):
		blval = 2
	return blval

def GetNextRefineName(itemVnum):
	next_refine = item.GetNextRefine(itemVnum)
	item_name = ""
	item.SelectItem(next_refine)
	item_name = ("|cff6D8E6F%s" % item.GetItemName())
	item.SelectItem(itemVnum)
	return item_name

def AppendNextRefine():
	GET_NEXT_REFINE_VNUM = item.GetNextRefine(GET_CURRENT_SELECTED_VNUM)
	if (app.IsPressed(app.DIK_LALT) and item.GetNextRefine(GET_CURRENT_SELECTED_VNUM) != 0) and not shop.IsOpen():
		return True
	return False

def CheckStatusColor(value):
	color = 0
	if value == 88 or value == 89:
		if (CheckWrongAddon(value)):
			return grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
		else:
			return grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
	if (CheckAddon(value) == 1):
		color = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
	elif (CheckAddon(value) == 0):
		color = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
	else:
		color = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	return color
