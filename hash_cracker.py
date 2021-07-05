import argparse, hashlib, time, random, string
from colorama import Fore, Style
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--hash", help="Hash To Crack", required=True)
parser.add_argument("-w", "--wordlist", help="Path To Wordlist", required=False)
parser.add_argument("-b", "--bruteforce", help="Length To Bruteforce", required=False)
args = parser.parse_args()
print(Fore.YELLOW + "  ___ ___     _____     _________  ___ ___      _________ __________    _____   _________   ____  __._____________________ \n /   |   \   /  _  \   /   _____/ /   |   \     \_   ___ \\______   \   /  _  \  \_   ___ \ |    |/ _|\_   _____/\______   \ \n/    ~    \ /  /_\  \  \_____  \ /    ~    \    /    \  \/ |       _/ /  /_\  \ /    \  \/ |      <   |    __)_  |       _/ \n\    Y    //    |    \ /        \\     Y    /    \     \____|    |   \/    |    \\      \____|    |  \  |        \ |    |   \ \n \___|_  / \____|__  //_______  / \___|_  /      \______  /|____|_  /\____|__  / \______  /|____|__ \/_______  / |____|_  / \n       \/          \/         \/        \/              \/        \/         \/         \/         \/        \/         \/" + Style.RESET_ALL)
print(Fore.YELLOW + f"Hash: {args.hash}\nWordlist: \"{args.wordlist}\"" + Style.RESET_ALL)
guesses = 1
start = time.time()
print(Fore.YELLOW + "Starts Cracking..." + Style.RESET_ALL)
if args.wordlist and not args.bruteforce:
    with open(args.wordlist, "r") as wordlist:
        wordlist = wordlist.read().split("\n")
    hash = args.hash
    for i in wordlist:
        if hashlib.md5(i.encode()).hexdigest() == hash:
            print(Fore.GREEN + f"Cracking Done\nHash Was \"{i}\"\nAmount Of Guesses: {guesses}\nTime: {time.time() - start} sec")
            exit()
        guesses += 1
    print(Fore.RED + "Hash Not Found In Wordlist" + Style.RESET_ALL)

elif args.wordlist and args.bruteforce:
    print(Fore.RED + "Please Only Use -w/--wordlist Without Other Arguments")

elif args.bruteforce and not args.wordlist:
    guess = ""
    while hashlib.md5(str(guess).encode()).hexdigest() != args.hash:
        guess = ""
        guess = ''.join(random.choice(string.printable) for _ in range(int(args.bruteforce)))
        guesses += 1
    print(Fore.GREEN + f"Cracking Done\nHash Was \"{guess}\"\nAmount Of Guesses: {guesses}\nTime: {time.time() - start} sec")
elif args.bruteforce and args.wordlist:
    print(Fore.RED + "Please Use -b/--bruteforce Without Other Arguments")
