Running the binary will give us this a messagebox showing hex encoded value

![picture1](https://user-images.githubusercontent.com/46635361/51079417-70526480-16cf-11e9-879a-396c57c04aca.png)

using PEstudio you can find that the binary was packed using UPX 

![picture2](https://user-images.githubusercontent.com/46635361/51079452-07b7b780-16d0-11e9-8dfc-ae13b9ec93ad.png)

Disable ASLR & Unpack it

![picture3](https://user-images.githubusercontent.com/46635361/51079512-fc18c080-16d0-11e9-9c2b-3e1dba69c7a1.png)

using x64dbg you can find that it uses [IsDebuggerPresent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680345(v=vs.85).aspx) function to dentermine whenever there is a debugger or not and if there is a debugger a messagebox saying 'This is a third-party compiled AutoIt script.' will show instead.

![untitled](https://user-images.githubusercontent.com/46635361/51079617-b4933400-16d2-11e9-8203-0c3641e5a6a6.png)

Here you can find how to detect AutoIt compailed scripts [AutoIt Malware: From Compiled Binary to Plain-Text Script](https://r3mrum.wordpress.com/2017/07/10/autoit-malware-from-compiled-binary-to-plain-text-script/)


Now let's reverse it !


using EXE2aut you can extract the actual script

![untitled](https://user-images.githubusercontent.com/46635361/51079703-45b6da80-16d4-11e9-88c6-36f893e67ae0.png)

Here, near the buttom you can find this function 

```C
Func cmmkxdi()
	Global $povvyzid_qgidn_wyfvjlrasdasd = 202
	Local $texjyuus_kxmczmsui_waowsej = "0xAFAF301D3DF20EE93EB8B8A9842FB0781FEFAAB30F4628D4"
	Global $qw_vouefw_jxcp_ucasdasd = 46689
	Local $var_1044 = asdasfcyzncmmkxdiasd(False, $texjyuus_kxmczmsui_waowsej, "i4m_th3_fl@g")
	Global $aycqkqgdnvzzuelotalsibomsdsd = 116
	MsgBox($mb_systemmodal, "BSides Cairo", $texjyuus_kxmczmsui_waowsej)
EndFunc
```

so all we need here is to print var_1044 value instead of the hex encoded values in texjyuus_kxmczmsui_waowsej, Change the code to

```C
Func cmmkxdi()
	Global $povvyzid_qgidn_wyfvjlrasdasd = 202
	Local $texjyuus_kxmczmsui_waowsej = "0xAFAF301D3DF20EE93EB8B8A9842FB0781FEFAAB30F4628D4"
	Global $qw_vouefw_jxcp_ucasdasd = 46689
	Local $var_1044 = asdasfcyzncmmkxdiasd(False, $texjyuus_kxmczmsui_waowsej, "i4m_th3_fl@g")
	Global $aycqkqgdnvzzuelotalsibomsdsd = 116
	MsgBox($mb_systemmodal, "BSides Cairo", $var_1044)
EndFunc
```

and run it using the AutoIT interpreter

![untitled](https://user-images.githubusercontent.com/46635361/51079752-c88c6500-16d5-11e9-8baa-800c582f9dc8.png)
