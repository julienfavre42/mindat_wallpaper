# mindat_wallpaper
Mindat daily picture wallpaper

This script allows you to scrap and save the background image of Mindat website (https://www.mindat.org/), and to use it as a wallpaper. The "Picture of the day" of this site changes every day, and it shows nice minerals, that can make a beautiful wallpaper different everyday for your PC.

The script works this way:

On Windows:
- You should edit the bat file to update the Python setup path, and your working folder (supposed to be the "Pictures" folder here) on line 2
- Then in the Python script, you should edit the lines 18-19 to change the setup path of Chrome browser, and line 24 for your working directory.
- Finally add the bat file to the startup programs (a shortcut in C:\Users\...\AppData\Roaming\Microsoft\Windows\Start Menu\Programs should work).
Then manually select the scrapped picture "photo.png" as a wallpaper in the Windows configuration. It should change daily. There may be some delay sometimes to refresh the background.

On Linux:
Just use the Python script, auto-start it by adding it to crontab or some autostart file, and select the scrapped picture as a wallpaper.
