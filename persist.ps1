$e = (Out-String -InputObject (net user 'YOUR_USER' 2>&1))

if ($e -like '*could not be found*')
{
    new-localuser -Name "YOUR_USER" -Password (convertto-securestring -string 'P4SSW3RD' -force -asplaintext) -Description "Xampp FSDL account."
    Add-LocalGroupMember -Group "Administrators" -Member "XAMPP"
    Add-LocalGroupMember -Group "Remote Desktop" -Member "XAMPP"
    Add-LocalGroupMember -Group "Remote Desktop Users" -Member "XAMPP"
    Add-LocalGroupMember -Group "Remote Management Use" -Member "XAMPP"
}
