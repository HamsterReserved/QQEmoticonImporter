QQ Emoticon Importer
===
��������������ǰ��Android���ֻ�QQ����ܵı��顣�����Ϊˢ������������ݵ��±��鶪ʧ�����ʹ�ô˳���ָ���

####�÷���

1. ǿ��ֹͣQQ��

2. ��`/data/data/com.tencent.mobileqq/databases/���QQ��.db`���Ƶ������ϡ�

3. adb shell

    `$ md5sum /storage/emulated/0/Tencent/QQ_Favorite/*.jpg > /sdcard/md5.txt`
   
   ע����һ����·������ʡ�ԡ�***�����Ǿ���·����***

4. ��`/sdcard/md5.txt`���Ƶ������ϡ�

5. �ѳ������`HASH_KEY`��`MD5SUM_OUTPUT`��`DATABASE_PATH`����ʵ��������ġ�`HASH_KEY`���ֻ���IMEI�������߾���֮ǰ���Ƶ��ļ���

6. ���޸ĺ�����ݿ��ļ����ǵ�`/data/data/com.tencent.mobileqq/databases/���QQ��.db`

7. ���´��ֻ�QQ��


######������ˢ�����κ��ֱ���ȫ����ʧ�Ĳ����ڶ�ͼ��Ҳ��ϲ��ûͼ���Ըо��ܲ��õ�${REPO_OWNER}�ڵ�Ƭ����������ǰϦ���