from SocialInfoga.URLInfo import urlinfo
from SocialInfoga.ImageInfoga import recon
from SocialInfoga.IPFinder import iplocate
from SocialInfoga.Hitmapper import read_multiple_ip
from SocialInfoga.WebRats import Links
from SocialInfoga.NameInfo import Nameinfo
from SocialInfoga.PhoneInfoga import number

R = '\033[1;31;40m'
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m'


def reconinput():
    inp = input("Information you want to gather: ")
    if inp == '1':
        recon()
    elif inp == '2':
        iplocate()
    elif inp == '3':
        read_multiple_ip()
    elif inp == '4':
        urlinfo()
    elif inp == '5':
        Links()
    elif inp == '6':
        Nameinfo()
    elif inp == '7':
        number()
    elif inp == 'exit':
        exit()
    elif inp == 'tools':
        print(G + """Tools available:
        1. Social Media Accounts finder using an Image
        2. Trace Single IP
        3. Trace Multiple IPs
        4. URL Redirection Finder
        5. Links lookup in Web pages
        6. Information Gathering using Name
        7. Phone number verifier

        Usage: Type exit to stop
        """)
    else:
        print(R + "Enter an Valid option")
    while True:
        reconinput()


if __name__ == "__main__":
    reconinput()