# -*- coding: UTF-8 -*-
# /*
# *      Copyright (C) 2017 BrozikCZ
# *
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */
import os
import xbmcaddon
import xbmcgui
import shutil
import json 

__script_id__ = xbmcaddon.Addon().getAddonInfo('id')
__addon__ = xbmcaddon.Addon(id=__script_id__)
__addon_name__ = __addon__.getAddonInfo('name')
__extract_path__ = os.path.join(__addon__.getAddonInfo('path'), 'resources', 'addon')
__addon_to_extract__ = os.walk(__extract_path__).next()[1][0]
__addon_to_extract_path__ = os.path.join(__extract_path__, __addon_to_extract__)

def copy_dir(src, dst):
    try:
        shutil.copytree(src, dst)
    except Exception as e:
        print str(e)
        return False
    return True

def refresh_addon_library():
    xbmc.executebuiltin('UpdateLocalAddons', True)

def enable_addon():
    refresh_addon_library()

    cmd = '{{"jsonrpc": "2.0", "id":1, "method": "Addons.SetAddonEnabled", "params": {{ "addonid": "{}", "enabled": true }}}}'.format(__addon_to_extract__)
    response = xbmc.executeJSONRPC(cmd)
    json_response = json.loads(response.decode('utf-8','replace'))
    return json_response.has_key('result') and json_response['result'] == 'OK'

def exit():
    xbmc.executebuiltin('XBMC.Container.Update(path,replace)')
    xbmc.executebuiltin('XBMC.ActivateWindow(Home)')

result_copy = copy_dir(__addon_to_extract_path__, '/data/user/0/org.xbmc.kodi/cache/apk/assets/addons/{}'.format(__addon_to_extract__));

if result_copy and enable_addon():
    xbmcgui.Dialog().ok(__addon_to_extract__, __addon__.getLocalizedString(1))
else:
    xbmcgui.Dialog().ok(__addon_to_extract__, __addon__.getLocalizedString(2))

exit()
