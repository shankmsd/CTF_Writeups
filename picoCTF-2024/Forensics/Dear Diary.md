## Challenge 🧩
If you can find the flag on this disk image, we can close the case for good!

Author: SYREAL</br>
Points: 400

Hint: If you're observing binary data raw in the terminal you may be misled about the contents of a block.

## Solution 🕵️‍♂️

```bash
┌──(user㉿shell)-[~]
└─$ sudo autopsy
============================================================================

                       Autopsy Forensic Browser 
                  http://www.sleuthkit.org/autopsy/
                             ver 2.24 

============================================================================
Evidence Locker: /var/lib/autopsy
Remote Host: localhost
Local Port: 9999

Open an HTML browser on the remote host and paste this URL in it:

    http://localhost:9999/autopsy

Keep this process running and use <ctrl-c> to exit
```

![autopsy_welcome](src/autopsy_welcome.PNG)

Lets create a new case </br>

![autopsy_newCase](src/autopsy_newCase.PNG)

Click on add host. Lets continue with the defaults </br>

![autopsy_addHost](src/autopsy_addHost.PNG)

Add the extracted .img file to autopsy </br>

![autopsy_imageAdd](src/autopsy_imageAdd.PNG)
![autopsy_imageAdd_details](src/autopsy_imageAdd_details.PNG)

Lets analyze entire disk which has 3 partitions. Click on `Analyze` to continue </br>

![Volume_Analyze](src/Volume_Analyze.PNG)

Searching for the `pico` keyword yields not-so-helpful results.
![keywordSearch](src/keywordSearch.PNG)
![keywordSearch_pico](src/keywordSearch_pico.PNG)

Lets try with the `.txt` keyword, after analyzing all results we can find the flag. </br>

![keywordSearch_txt](src/keywordSearch_txt.PNG)

`Tool Used: autopsy`

## Flag 🚩

`picoCTF{1_533_n4m35_xxxxxxxx}`
