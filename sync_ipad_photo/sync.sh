#!/usr/bin/bash

ssh root@192.168.1.4 ls /User/Media/DCIM/100APPLE | sort > /tmp/ipad.lst 
ls /cygdrive/c/’’∆¨/IPAD | sort > /tmp/local.lst
diff /tmp/local.lst /tmp/ipad.lst  | grep '^>' | awk '{print $2}' > /tmp/diff.lst
echo Total `wc -l /tmp/diff.lst` new files
cat /tmp/diff.lst | xargs -I , scp root@192.168.1.4:/User/Media/DCIM/100APPLE/, /cygdrive/c/’’∆¨/IPAD 
echo Done

