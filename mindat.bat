@echo off
"C:\Program Files\Python312\python.exe" C:\Users\tartempion\Pictures\mindat_scrap.py
FOR /L %%y IN (0, 1, 5) DO RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters
