import random
import time
import sys
from rich import print

print("""[red]
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░░░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░░░██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║░░░░░░░░██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║░░░░░░░░██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░░░╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
[/red]""")
print("[yellow][1]Nitro Generator[/yellow]")
print("[yellow][2]Erase Codes[/yellow]")
print("[yellow][3]Exit[/yellow]")
print("[gray]Credits to Etheriul#2034[/gray]")
choice = int(input("[?]"))


if choice == 1:
    codelen = 16
    letters = "ABCDEFGHJKLMNOPQRSTUWXYZabcdefghjklmnopqrstuwxyz0123456789"
    f = open('nitrocodes.txt', 'w')
    amount = int(input("Enter the amount of code you want to genarate:"))
    def codes():
        return ''.join(random.choice(letters) for i in range(codelen))
    lp = amount
    for i in range(lp):
        f.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
        time.sleep(0.3)
        print(codes())

elif choice == 2:
    sure = input("Are you sure you want to delete all the codes? (yes/no):")
    if sure == "yes":
        f = open('nitrocodes.txt', 'r+')
        f.truncate(0)
    elif sure == "no":
        sys.exit()
elif choice == 3:
    print("[red]Exiting in 3[/red]")
    time.sleep(1)
    print("[red]Exiting in 2[/red]")
    time.sleep(1)
    print("[red]Exiting in 1[/red]")
    time.sleep(1)
    print("[red]Goodbye...[/red]")
    time.sleep(1.75)
    sys.exit()

else:
    print("[red]Please enter a valid choice next time...[/red]")
    time.sleep(1.5)
    sys.exit()