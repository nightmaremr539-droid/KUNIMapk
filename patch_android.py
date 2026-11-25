import os,shutil
from PIL import Image
A='android/app/src/main'
m=open(f'{A}/AndroidManifest.xml',encoding='utf8').read()
perms=''.join(f'    <uses-permission android:name="android.permission.{p}"/>\n' for p in
 ['POST_NOTIFICATIONS','VIBRATE','WAKE_LOCK','USE_EXACT_ALARM','SCHEDULE_EXACT_ALARM','RECEIVE_BOOT_COMPLETED','USE_FULL_SCREEN_INTENT'])
if 'USE_EXACT_ALARM' not in m:
    m=m.replace('</manifest>',perms+'</manifest>')
open(f'{A}/AndroidManifest.xml','w',encoding='utf8').write(m)
os.makedirs(f'{A}/res/raw',exist_ok=True);shutil.copy('resources/alarm.wav',f'{A}/res/raw/alarm.wav')
os.makedirs(f'{A}/res/drawable',exist_ok=True);shutil.copy('resources/ic_stat_kunim.png',f'{A}/res/drawable/ic_stat_kunim.png')
shutil.rmtree(f'{A}/res/mipmap-anydpi-v26',ignore_errors=True)
src=Image.open('resources/icon-512.png').convert('RGBA')
for d,sz in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}.items():
    os.makedirs(f'{A}/res/mipmap-{d}',exist_ok=True)
    for n in('ic_launcher.png','ic_launcher_round.png'):
        src.resize((sz,sz),Image.LANCZOS).save(f'{A}/res/mipmap-{d}/{n}')
print('patched')
