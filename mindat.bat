@echo off
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\python.exe" C:\Users\tartempion\Pictures\mindat_scrap.py
FOR /L %%y IN (0, 1, 10) DO RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters 1, True