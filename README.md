QQ Emoticon Importer
===
用来批量导入以前在Android版手机QQ里积攒的表情。如果因为刷机或者清除数据导致表情丢失，则可使用此程序恢复。

####用法：

1. 强行停止QQ。

2. 把`/data/data/com.tencent.mobileqq/databases/你的QQ号.db`复制到电脑上。

3. adb shell

    `$ md5sum /storage/emulated/0/Tencent/QQ_Favorite/*.jpg > /sdcard/md5.txt`
   
   注意这一步的路径不能省略。***必须是绝对路径。***

4. 把`/sdcard/md5.txt`复制到电脑上。

5. 把程序里的`HASH_KEY`、`MD5SUM_OUTPUT`和`DATABASE_PATH`按照实际情况更改。`HASH_KEY`是手机的IMEI。后两者就是之前复制的文件。

6. 用修改后的数据库文件覆盖到`/data/data/com.tencent.mobileqq/databases/你的QQ号.db`

7. 重新打开手机QQ。


######由连续刷机两次后发现表情全部丢失的不善于斗图但也不喜欢没图所以感觉很不好的${REPO_OWNER}于单片机课设验收前夕完成