#!bin/bash

create_usr() {
    username=$(whiptail --inputbox "Ievadi lietotājvārdu" 8 39 --title "Jauns lietotājs" 3>&1 1>&2 2>&3)
    sudo useradd $username
    newpass+$(whiptail --passwordbox "Ievadi paroli" 8 78 --title "Jaunā parole" 3>&1 1>&2 2>&3)
    sudo chpasswd <<<"$username: $newpass"
}
delete_usr() {
    username=$(whiptail --inputbox "Ievadi lietotājvārdu, kuru izdzēst" 8 39 --title "Lietotājvārdu" 3>&1 1>&2 2>&3)
    subchotce=$(whiptail --title "Izvēlne" --radiolist \
    "Izvēlies vienu" 20 78 4 \
    "1" "Dzēst visus lietotaja datus" ON \
    "2" "Dzēst lietotāju, bet saglabāt datus" OFF \
    3>&2 2>&1 1>&3)
case $subchoice in
    "1")
        sudo userdel -r $username
        whiptail-title "Darīts" --msgbox "Pabeigts" 8 78
    ;;
    "2")
        sudo userdel $username
        whiptail-title "Darīts" --msgbox "Pabeigts" 8 78
    ;;
esac
        }
change_usr() {
    user=$(whiptail --inputbox "Ievadi lietotāju, kuram mainit paroli" 8 39 --title "" 3>&1 1>&2 2>&3)
    newpass=$(whiptail --passwordbox "Ievadi paroli" 8 78 --title "Paroles dialogs" 3>&1 1>&2 2>&3)
}
while command
do
CHOICE=$(
whiptail --title "Lietotāja apstrāde" --menu "Izvēlne" 16 100 9 \
    "1)" "Izveidot jaunu lietotāju" \
    "2)" "Dzēst lietotāju" \
    "3)" "Mainit paroli" \
    "4)" "Beigt programmu" \
    3>&2 2>&1 1>&3
    )
case $CHOICE in
    "1)")
        create_usr
    ;;
    "2)")
        delete_usr
    ;;
    "3)")
        change_usr
    ;;
    "4)")
        exit
    ;;
esac
done
exit
