"""
--------------------------------------------
	Sanguine Project ~ Nirray & BeHolder
	Hi, if you're reading this, feel free to use the solutions used in this file. 
	Some scripts were written a long time ago (around 2010) so they may be somewhat outdated.
	We had plans to create a server already in 2009 r/slowpoke/
	We have no right to prohibit you from editing this file, 
	but using modifications to your advantage on the server will be severely punished (probably by blocking your account).
	
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
import chat
import os
import constInfo
import systemSetting
import background
# introselect.py
INTROSELECT_CURRENT_LEVEL = 0
# end of introselect.py

# introloading.py performance patch
ENABLE_SPLASH_SCREEN = 1
INIT_DUNGEONMAPNAME_ONCE = 0
INIT_REGISTERSKILL_ONCE = 0
INIT_REGISTERTITLENAME_ONCE = 0
INIT_REGISTERCOLOR_ONCE = 0
INIT_REGISTEREMOTIONICON_ONCE = 0
# end of introloading.py
# sanguine external engine variables
SANGUINE_FOG_LEVEL = 2
SANGUINE_FOG_DISTANCE_LEVELS = [5000.0, 7500.0, 9600.0, 11000.0, 12500.0]
SANGUINE_CAMERA_LEVEL = 2
SANGUINE_CAMERA_DISTANCE_LEVELS = [1500.0, 2500.0, 3500.0, 4200.0, 5600.0]
SANGUINE_SHADOW_LEVEL = systemSetting.GetShadowLevel()
SANGUINE_SPLIT_CHUNK = 1030.0
SANGUINE_SPLIT_LEVEL = 5
# end of external
ENABLE_ADMIN_LOGO = 1
ENABLE_BGM_PUSH = 0
ENABLE_NEW_AUTO_LOGIN = 0
ENABLE_ITEM_LONG_TOOLTIP = 1
ENABLE_ITEM_ICON_TOOLTIP = 0
ENABLE_TRUE_DEBUG_MODE = 1
# BeHolder
GET_CURRENT_SELECTED_VNUM = 0
GET_NEXT_REFINE_VNUM = 0

GAME_RENDER_TERRAIN = 1
GAME_RENDER_BUILDING = 1
GAME_RENDER_WATER = 1
GAME_RENDER_TREE = 1
GAME_RENDER_CLOUDS = 1
GAME_RENDER_EFFECT = 1

# other visuals
GAME_RENDER_NOTICE = 1
GAME_RENDER_FPS_COUNT = 0
# +optimize
OPTIMIZE_ENABLE = 1
ALLOW_OPTIMIZE = False
OPTIMIZE_WAIT_FOR_PERFORMANCE = 0
OPTIMIZE_WAS_ALWAYSSHOWNAME = 0
OPTIMIZE_WASSHOWDAMAGE = 0
OPTIMIZE_WASSHOWONLYNAMEANDITEMS = 0
OPTIMIZE_OLD_SHADOW_LEVEL = 0
# end of
GAME_HIDE_TASKBAR = 0
GAME_SHOW_ONLYOWNNAME_AND_ITEMS = 0
# uichat and uiwhisper
CHAT_STACK = []
CHAT_STACK_POS = 0
CHAT_STACK_NOTICE = 0
WHISPER_STACK = []
WHISPER_STACK_POS = 0
ENABLE_WHISPER_EMOJI = 1
# Engine extensions
SHOP_QUICK_SET = 0
ENABLE_PING_SCAN = 1
ACROBATIC_DODGE_SET_LEFT = 0
ACROBATIC_DODGE_SET_RIGHT = 0
ACROBATIC_DODGE_SET_DOWN = 0
ACROBATIC_DODGE_SET_UP = 0
ACROBATIC_DODGE_TIME_LEFT = 0.0
ACROBATIC_DODGE_TIME_RIGHT = 0.0
ACROBATIC_DODGE_TIME_DOWN = 0.0
ACROBATIC_DODGE_TIME_UP = 0.0
# droplist extensions
SANGUINE_DROPLIST_VID_AND_ITEM_NAME = {}
SANGUINE_OWN_ITEM_VID = []
SANGUINE_DROP_LIST_REFRESH = 0
SANGUINE_DROP_LIST_LAST = ""
SANGUINE_DROP_LIST_DOUBLE = 0
SANGUINE_DROP_LIST_SLIDER = 0
# end of extensions
SPLASH_SCREEN_SIZE = 42
SPLASH_SCREEN_GUIDE = {
	0 : "Niektórzy handlarze w świecie gry mogą sprzedawać przedmioty taniej od innych",
	1 : "Istnieje przedmiot dla wojownika ciało, który chroni go przed utratą PŻ",
	2 : "W świecie limbo nic nie jest materialne",
	3 : "Nie żyjesz",
	4 : "Czarny tekst na czarnym tle jest nieczytelny",
	5 : "Akrobatyka absorbuje 50% obrażeń z umiejętności przeciwnika",
	6 : "Odpowiednie użycie akrobatyki pozwala na całkowite uniknięcie obrażeń",
	7 : "Szansa na cios przeszywający pozwala na ominięcie bloku przeciwnika",
	8 : "Zręczność zwiększa szansę na unik obrażeń",
	9 : "Próg odporności na klasy postaci wynosi 60%",
	10 : "Odporność na ogień działa na podpalenie",
	11 : "Możesz nosić jednocześnie dwie takie same rękawice lub dwie różne",
	12 : "Nikt nie wymaga bycia od Ciebie miłym",
	13 : "Jesteś w piekle",
	14 : "Przed wyruszeniem w drogę należy zebrać drużynę",
	15 : "Zostałem uwięziony w ekranie powitalnym, pomocy!",
	16 : "Administracja nigdy nie zapyta o Twój login lub hasło!",
	17 : "Jeżeli widzisz tę wiadomość dłużej niż godzinę to polecam wyłączyć grę",
	18 : "Możesz przeszkodzić w zabiciu Czerwonego Smoka",
	19 : "Ta nazwa serwera jest już zajęta",
	20 : "Uwierz mi, ta konkretna była nieciekawa",
	21 : "Powrót do przeszłości",
	22 : "Przypominam o częstym piciu wody",
	23 : "Ulepszanie serwera nie powiodło się",
	24 : "Stan jakości broni definiuje jej całkowite obrażenia",
	25 : "Demontowanie elementów ekwipunku pozwala na uzyskanie materiałów produkcyjnych",
	26 : "Księżniczka jest w innym zamku",
	27 : "Wiele dróg do nowych terenów nie zostały jeszcze odkrytych",
	28 : "Kamienie teleportacyjne pozwalają na szybką podróż w odkryte miejsca",
	29 : "Bug Bounty - więcej informacji znajdziesz na forum",
	30 : "Na bieżąco sprawdzamy nowo dostępne cheaty",
	31 : "Smażenie ryb nad ogniskiem zwiększa ich ilość dwukrotnie",
	32 : "PŻ oraz PE nie regenerują się bez bonusu Regeneracja PŻ w ekwipunku",
	33 : "Od teraz potwory mogą unikać obrażeń",
	34 : "W zasadzie możesz używać umiejętności bez konieczności zaznaczania celu",
	35 : "Rozpoczynając grę akceptujesz regulamin rozgrywki",
	36 : "Dowodzenie zmniejsza wymaganą liczbę różnicy poziomów lidera i jego członków",
	37 : "Od teraz zakładanie ekwipunku wymaga odpowiedniej statystyki postaci",
	38 : "Przedmioty potrzebne do wykonania zadań są oznaczone na niebiesko",
	39 : "Punkty rangii zostały zamienione na punkty duszy - uważaj na swoje punkty",
	40 : "Wojna. Wojna nigdy się nie zmienia.",
	41 : "Python? Python? PYYYYYTHONN!!!",
	42 : "Myślałem, że mam w piwnicy bazyliszka, a to moja stara po węgiel zeszła",
}

def DefineSettings():
	global SANGUINE_CAMERA_DISTANCE_LEVELS
	global SANGUINE_CAMERA_LEVEL
	global SANGUINE_FOG_DISTANCE_LEVELS
	global SANGUINE_FOG_LEVEL
	global SANGUINE_SHADOW_LEVEL
	global GAME_RENDER_TERRAIN
	global GAME_RENDER_BUILDING
	global GAME_RENDER_WATER
	global GAME_RENDER_TREE
	global GAME_RENDER_CLOUDS
	app.SetCameraMaxDistance(SANGUINE_CAMERA_DISTANCE_LEVELS[SANGUINE_CAMERA_LEVEL])
	app.SetMinFog(SANGUINE_FOG_DISTANCE_LEVELS[SANGUINE_FOG_LEVEL])
	systemSetting.SetShadowLevel(SANGUINE_SHADOW_LEVEL)
	background.SetShadowLevel(background.SHADOW_ALL)
	ReloadRender()

def SaveConfig():
	global SANGUINE_FOG_LEVEL
	global SANGUINE_CAMERA_LEVEL
	global SANGUINE_SHADOW_LEVEL
	global SANGUINE_SPLIT_LEVEL
	global GAME_RENDER_TERRAIN
	global GAME_RENDER_BUILDING
	global GAME_RENDER_WATER
	global GAME_RENDER_TREE
	global GAME_RENDER_CLOUDS
	open('sanguine.txt', 'w').write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (SANGUINE_FOG_LEVEL, SANGUINE_CAMERA_LEVEL, SANGUINE_SHADOW_LEVEL, SANGUINE_SPLIT_LEVEL, GAME_RENDER_TERRAIN, GAME_RENDER_BUILDING, GAME_RENDER_WATER, GAME_RENDER_TREE, GAME_RENDER_CLOUDS))

def LoadConfig():
	global SANGUINE_FOG_LEVEL
	global SANGUINE_CAMERA_LEVEL
	global SANGUINE_SHADOW_LEVEL
	global SANGUINE_SPLIT_LEVEL
	global GAME_RENDER_TERRAIN
	global GAME_RENDER_BUILDING
	global GAME_RENDER_WATER
	global GAME_RENDER_TREE
	global GAME_RENDER_CLOUDS
	global ENABLE_TRUE_DEBUG_MODE
	if os.path.exists("sanguine.txt"):
		config = open("sanguine.txt", "r").read().split()
		SANGUINE_FOG_LEVEL = int(config[0])
		SANGUINE_CAMERA_LEVEL = int(config[1])
		SANGUINE_SHADOW_LEVEL = int(config[2])
		SANGUINE_SPLIT_LEVEL = float(config[3])
		GAME_RENDER_TERRAIN = float(config[4])
		GAME_RENDER_BUILDING = float(config[5])
		GAME_RENDER_WATER = float(config[6])
		GAME_RENDER_TREE = float(config[7])
		GAME_RENDER_CLOUDS = float(config[8])
		DefineSettings()

def ChangeCameraSetting(level):
	global SANGUINE_CAMERA_DISTANCE_LEVELS
	global SANGUINE_CAMERA_LEVEL
	try:
		extend = level*4.0
		SANGUINE_CAMERA_LEVEL = int(extend)
		app.SetCameraMaxDistance(SANGUINE_CAMERA_DISTANCE_LEVELS[SANGUINE_CAMERA_LEVEL])
	except:
		app.SetCameraMaxDistance(SANGUINE_CAMERA_DISTANCE_LEVELS[2])

def ChangeFogSetting(level):
	global SANGUINE_FOG_DISTANCE_LEVELS
	global SANGUINE_FOG_LEVEL
	try:
		extend = level*4.0
		SANGUINE_FOG_LEVEL = int(extend)
		app.SetMinFog(SANGUINE_FOG_DISTANCE_LEVELS[SANGUINE_FOG_LEVEL])
	except:
		app.SetMinFog(SANGUINE_FOG_DISTANCE_LEVELS[2])

def ChangeShadowLevel(level):
	global SANGUINE_SHADOW_LEVEL
	try:
		extend = level*5.0
		SANGUINE_SHADOW_LEVEL = int(extend)
		systemSetting.SetShadowLevel(SANGUINE_SHADOW_LEVEL)
		background.SetShadowLevel(SANGUINE_SHADOW_LEVEL)
	except:
		systemSetting.SetShadowLevel(SANGUINE_SHADOW_LEVEL)

def ReloadShadow():
	global SANGUINE_SHADOW_LEVEL
	systemSetting.SetShadowLevel(SANGUINE_SHADOW_LEVEL)
	background.SetShadowLevel(SANGUINE_SHADOW_LEVEL)

def CheckTrueDebug():
	global GET_CURRENT_SELECTED_VNUM
	if (ENABLE_TRUE_DEBUG_MODE and app.IsPressed(app.DIK_LSHIFT)):
		return True
	else:
		return False

def RenderTerrain():
	global GAME_RENDER_TERRAIN
	try:
		background.SetVisiblePart(background.PART_TERRAIN, not GAME_RENDER_TERRAIN);
	except:
		return

def RenderObject():
	global GAME_RENDER_BUILDING
	try:
		background.SetVisiblePart(background.PART_OBJECT, not GAME_RENDER_BUILDING);
	except:
		return

def RenderWater():
	global GAME_RENDER_WATER
	try:
		background.SetVisiblePart(background.PART_WATER, not GAME_RENDER_WATER);
	except:
		return

def RenderFlora():
	global GAME_RENDER_TREE
	try:
		background.SetVisiblePart(background.PART_TREE, not GAME_RENDER_TREE);
	except:
		return

def RenderCloud():
	global GAME_RENDER_CLOUDS
	try:
		background.SetVisiblePart(background.PART_CLOUD, not GAME_RENDER_CLOUDS);
	except:
		return

def ReloadRender():
	RenderTerrain()
	RenderObject()
	RenderWater()
	RenderFlora()
	RenderCloud()

def unsigned32(n):
	return n & 0xFFFFFFFFL

def CheckArmor(vnum):
	# exile armor
	if (12016 <= vnum and vnum <= 12019):
		return 12015
	elif (12026 <= vnum and vnum <= 12029):
		return 12025
	elif (12036 <= vnum and vnum <= 12039):
		return 12035
	elif (12046 <= vnum and vnum <= 12049):
		return 12045
	# end of exile
	elif (vnum % 10 == 9):
		return vnum-3
	elif (vnum % 10 == 8):
		return vnum-2
	elif (vnum % 10 == 7):
		return vnum-1
	else:
		return vnum

def FlushChat():
	global CHAT_STACK_NOTICE
	global CHAT_STACK
	global CHAT_STACK_POS
	if not CHAT_STACK_NOTICE and CHAT_STACK:
		CHAT_STACK_NOTICE = 1
		Notice("» Zapisane wiadomości:")
		for text in CHAT_STACK:
			Notice("» %s" % (text))

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

# Syntax error - old: return text instead of str(text) ~ Nirray
def Notice(text):
	chat.AppendChat(chat.CHAT_TYPE_SANGUINE, str(text))

def DropListAppend(vid, item_name):
	global SANGUINE_DROPLIST_VID_AND_ITEM_NAME
	append = {vid : item_name}
	SANGUINE_DROPLIST_VID_AND_ITEM_NAME.update(append)

def DropListMyItem(vid):
	global SANGUINE_OWN_ITEM_VID
	global SANGUINE_DROP_LIST_REFRESH
	SANGUINE_OWN_ITEM_VID.append(vid)
	SANGUINE_DROP_LIST_REFRESH = 1

def RemoveFromDropList(vid):
	global SANGUINE_DROPLIST_VID_AND_ITEM_NAME
	global SANGUINE_OWN_ITEM_VID
	global SANGUINE_DROP_LIST_REFRESH
	if SANGUINE_DROPLIST_VID_AND_ITEM_NAME and SANGUINE_OWN_ITEM_VID:
		if vid in SANGUINE_DROPLIST_VID_AND_ITEM_NAME:
			del SANGUINE_DROPLIST_VID_AND_ITEM_NAME[vid]
			SANGUINE_OWN_ITEM_VID.remove(vid)
			SANGUINE_DROP_LIST_REFRESH = 1

def ScanDropList():
	global SANGUINE_DROPLIST_VID_AND_ITEM_NAME
	global SANGUINE_OWN_ITEM_VID
	for i in SANGUINE_DROPLIST_VID_AND_ITEM_NAME:
		if i in SANGUINE_OWN_ITEM_VID:
			Notice("Twoj przedmiot: (%d) %s" % (i, SANGUINE_DROPLIST_VID_AND_ITEM_NAME[i]))

def OptimizeFPS():
	global OPTIMIZE_WAS_ALWAYSSHOWNAME
	global OPTIMIZE_WASSHOWDAMAGE
	global OPTIMIZE_WASSHOWONLYNAMEANDITEMS
	global GAME_SHOW_ONLYOWNNAME_AND_ITEMS
	global OPTIMIZE_OLD_SHADOW_LEVEL
	global SANGUINE_SHADOW_LEVEL
	if systemSetting.IsAlwaysShowName():
		OPTIMIZE_WAS_ALWAYSSHOWNAME = 1
		systemSetting.SetAlwaysShowNameFlag(False)
	if systemSetting.IsShowDamage():
		OPTIMIZE_WASSHOWDAMAGE = 1
		systemSetting.SetShowDamageFlag(False)
	if (GAME_SHOW_ONLYOWNNAME_AND_ITEMS):
		OPTIMIZE_WASSHOWONLYNAMEANDITEMS = 1
		GAME_SHOW_ONLYOWNNAME_AND_ITEMS = 0
	# if (systemSetting.GetShadowLevel() >= 4):
		# OPTIMIZE_OLD_SHADOW_LEVEL = SANGUINE_SHADOW_LEVEL
		# SANGUINE_SHADOW_LEVEL = 0
		# ReloadShadow()

def RestoreAfterOptimize():
	global OPTIMIZE_WAS_ALWAYSSHOWNAME
	global OPTIMIZE_WASSHOWDAMAGE
	global OPTIMIZE_WASSHOWONLYNAMEANDITEMS
	global GAME_SHOW_ONLYOWNNAME_AND_ITEMS
	global OPTIMIZE_OLD_SHADOW_LEVEL
	global SANGUINE_SHADOW_LEVEL
	if (OPTIMIZE_WAS_ALWAYSSHOWNAME):
		systemSetting.SetAlwaysShowNameFlag(True)
		OPTIMIZE_WAS_ALWAYSSHOWNAME = 0
	if (OPTIMIZE_WASSHOWDAMAGE):
		systemSetting.SetShowDamageFlag(True)
		OPTIMIZE_WASSHOWDAMAGE = 0
	if (OPTIMIZE_WASSHOWONLYNAMEANDITEMS):
		OPTIMIZE_WASSHOWONLYNAMEANDITEMS = 0
		GAME_SHOW_ONLYOWNNAME_AND_ITEMS = 1
	# if (OPTIMIZE_OLD_SHADOW_LEVEL > SANGUINE_SHADOW_LEVEL):
		# SANGUINE_SHADOW_LEVEL = OPTIMIZE_OLD_SHADOW_LEVEL
		# OPTIMIZE_OLD_SHADOW_LEVEL = 0
		# ReloadShadow()

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
	item.SelectItem(next_refine)
	item_name = ("|cff6D8E6F%s" % item.GetItemName())
	item.SelectItem(itemVnum)
	return item_name

def AppendNextRefine():
	global GET_NEXT_REFINE_VNUM
	global GET_CURRENT_SELECTED_VNUM
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
