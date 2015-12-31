'''
Quickly re-add all images under /sdcard/Tencent/QQ_Favorite
into your emoticon collection

USAGE:
0. Force-stop Mobile QQ.
1. adb pull /data/data/com.tencent.mobileqq/databases/YOUR_NUMBER.db SOMEWHERE_YOU_KNOW
2. adb shell
    $ md5sum /storage/emulated/0/Tencent/QQ_Favorite/*.jpg > /sdcard/md5.txt
3. adb pull /sdcard/md5.txt SOMEWHERE_YOU_KNOW
4. Change HASH_KEY, MD5SUM_OUTPUT and DATABASE_PATH accordingly.
5. adb push MODIFIED_DB /data/data/com.tencent.mobileqq/databases/YOUR_NUMBER.db
6. Start Mobile QQ.
'''
import sqlite3

HASH_KEY = "YOUR_IMEI_HERE"
MD5SUM_OUTPUT = "G:\md5.txt"
# Double back-slash on Windows
DATABASE_PATH = "G:\\10000.db"

def xor_hash(org_str):
    org_len = len(org_str)
    key_len = len(HASH_KEY)
    chr_index = 0
    result = ""
    while chr_index < org_len:
        result += chr(ord(org_str[chr_index]) ^ ord(HASH_KEY[chr_index % key_len]))
        chr_index += 1
    return result

class EmoticonRecord(object):
    def __init__(self, path, md5):
        self.path = path
        self.md5 = md5
        self.roaming_type = 'init' # Copied from original records
        self.hash_path = xor_hash(path)
        self.hash_md5 = xor_hash(md5)
        self.hash_roaming_type = xor_hash(self.roaming_type)

    def __str__(self):
        return "Path/MD5 is %s %s\nEncrypted path/MD5 is %s %s\n" \
            % (self.path, self.md5, self.hash_path, self.hash_md5)

sql_conn = sqlite3.connect(DATABASE_PATH)
cursor = sql_conn.cursor()
file = open(MD5SUM_OUTPUT)
i = 0
for line in file.readlines():
    parts = line.split()
    rec = EmoticonRecord(parts[1], parts[0])
    i += 1
    ins_values = (rec.hash_roaming_type, i, rec.hash_path,0, rec.hash_md5)
    cursor.execute('INSERT INTO CustomEmotionData (RomaingType, emoId, emoPath, isMarkFace, md5) VALUES (?, ?, ?, ?, ?)', ins_values)
sql_conn.commit()
cursor.close()
sql_conn.close()
file.close()

