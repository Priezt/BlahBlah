#1::
IfWinExist Case-Dev5
	WinActivate
return

#2::
IfWinExist JP Case-Dev5
	WinActivate
return

#3::
IfWinExist ahk_class MozillaWindowClass
	WinActivate
return

#4::
IfWinExist ahk_class Chrome_WidgetWin_0
	WinActivate
return