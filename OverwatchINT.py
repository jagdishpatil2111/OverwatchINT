from SocialInfoga.SocialInfoga import reconinput
import WebVulture.WebVulture as wv
from PenTest import PenTest as pt

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = "\033[1;33;40m"


def main():
    if a == 1:
        reconinput()
    elif a == 2:
        wv.main()
    elif a == 3:
        pt.main()



if __name__ == "__main__":
    print(cyan + """
             $$$$$$                                                    $$              $$        $$$$$$  $$$    $$  $$$$$$$$
           $$      $$                                                  $$              $$          $$    $$$$   $$     $$
           $$      $$  $$  $$    $$$$$    $$   $$  $$     $$  $$$$$$$  $$      $$$$$$  $$          $$    $$ $$  $$     $$
           $$      $$  $$  $$  $$     $$  $$ $$    $$     $$       $$  $$$$   $$       $$ $$$      $$    $$ $$  $$     $$
           $$      $$  $$  $$  $$$$$$$$   $$$      $$ $$  $$   $$$$$$  $$     $$       $$$   $$    $$    $$  $$ $$     $$
           $$      $$   $  $   $$         $$$      $$$$ $$$$  $$   $$  $$     $$       $$    $$    $$    $$   $$$$     $$
             $$$$$$      $$      $$$$$$$  $$$      $$$    $$   $$$$$$   $$$$   $$$$$$  $$    $$  $$$$$$  $$    $$$     $$
    """)
    print(Y + "                                          Created by : Jagdish Patil")
    print(Y + "                                          Github: https://www.https://github.com/JagdishPatil2111")
    print(green + """ 
              Available Modules
        1. Information Gathering
        2. Web Vulnerability Scanning
        3. Penetration Testing
        4. Steganography
        5. Digital Forensics
    """)
    print(Y + "Note: In Information Gathering, type 'tools' to find tools.")
    a = int(input("What would you like to do: "))
    main()
