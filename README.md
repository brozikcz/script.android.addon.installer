# script.android.addon.installer
Android native addon installer for Kodi

Usage: 
<ul>
<li>extract the target addon from zip to resources/addon</li>
<li>create zip: zip -FS -q -r script.android.addon.installer.zip script.android.addon.installer -x "*.py[oc] *.sw[onp]" ".*"</li>
<li>install to Kodi, run, restart and manually enable the addon</li>
</ul>

Tested on Nexus 5X and Shield TV.

TODO:
<ul>
<li>check cache directory with the addon</li>
<li>enable the addon from script</li>
</ul>
