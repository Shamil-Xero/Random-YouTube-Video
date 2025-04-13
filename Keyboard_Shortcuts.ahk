#Requires AutoHotkey v2.0
#SingleInstance force

ScrollLock:: {
    Run 'cmd.exe /c python "D:\YouTube\Auto YT Video\Scripts\Random-YT-Video.py" "https://www.youtube.com/playlist?list=PLb-MR2Hfk3tmamG_oQKvYK--4uZ0ULfHn"' , ,"Hide"
}

^Esc:: ExitApp