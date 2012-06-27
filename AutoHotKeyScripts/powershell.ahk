#IfWinActive Windows PowerShell
^u::Send {Esc}
^a::Send {Home}
^e::Send {End}
^l::Send {Esc}cls{Enter}
^b::Send {Left}
^f::Send {Right}
!b::Send ^{Left}
!f::Send ^{Right}
^p::Send {Up}
^n::Send {Down}
^d::Send {Delete}
^h::Send {Backspace}
#IfWinActive