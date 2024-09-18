Static IP address -> change Virtual machine manager

nmcli connection modify <interface_name> ipv4.method manual ipv4.addresses <ipv4_cidr> ipv4.gateway <gateway> ipv4.dns <gateway>
nmcli con up <interface_name>

nmcli con up <interface_name>

in case forgot password
https://www.jenkins.io/doc/book/system-administration/admin-password-reset-instructions/
