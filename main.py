import sys

def print_line():
    print("-" * 50)

def show_menu():
    print("\n" + "="*50)
    print("       DIGITAL LITERACY PORTFOLIO (CLI)        ")
    print("="*50)
    print("1. [Module 1]  Presentation Software")
    print("2. [Module 2/3] Digital Portfolio & Programming")
    print("3. [Module 4]  Email & Social Media Etiquette")
    print("4. [Module 5]  Cyber Crime & Fraud Awareness")
    print("5. Exit Application")
    print("="*50)

def module_1():
    print_line()
    print("MODULE 1: PRESENTATION SOFTWARE")
    print_line()
    print("Requirement: Hands-on Training on Presentation Software.")
    print("\nSummary: I have developed a structured, 5-slide deck")
    print("covering academic background and technical skills.")
    print("\nVIEW SLIDE DECK HERE:")
    print(">> [INSERT_YOUR_GOOGLE_SLIDES_LINK_HERE] <<")
    print_line()

def module_2_3():
    print_line()
    print("MODULES 2 & 3: PORTFOLIO & PROGRAMMING")
    print_line()
    print("Project: This CLI application itself serves as my portfolio.")
    print("Platform: Hosted on GitHub (Collaborative Learning).")
    print("Language: Python (Programming Platforms).")
    print("\nOTHER PROJECTS:")
    print("- Unbeatable Tic-Tac-Toe AI (Minimax Algorithm)")
    print("  Link: https://github.com/nipurn25bai10239-hash/unbeatable-tictactoe-python")
    print_line()

def module_4():
    print_line()
    print("MODULE 4: DIGITAL ETIQUETTE")
    print_line()
    print("EMAIL ETIQUETTE:")
    print("- Use professional salutations and clear subject lines.")
    print("- Keep messages concise and proofread for clarity.")
    print("\nSOCIAL MEDIA ETIQUETTE:")
    print("- Maintain a professional digital footprint.")
    print("- Verify information before sharing (Fact-checking).")
    print_line()

def module_5():
    print_line()
    print("MODULE 5: CYBER SECURITY & FRAUD AWARENESS")
    print_line()
    print("CYBER HYGIENE:")
    print("- Use complex passphrases and Enable MFA/2FA.")
    print("- Keep software and antivirus definitions updated.")
    print("\nFRAUD PREVENTION:")
    print("- Never share OTPs or sensitive bank details.")
    print("- Be cautious of 'Phishing' via urgent emails/SMS.")
    print_line()

def main():
    while True:
        show_menu()
        choice = input("Select a module to evaluate (1-5): ")

        if choice == '1':
            module_1()
        elif choice == '2':
            module_2_3()
        elif choice == '3':
            module_4()
        elif choice == '4':
            module_5()
        elif choice == '5':
            print("\nExiting. Thank you for the evaluation!")
            sys.exit()
        else:
            print("\n[!] Invalid input. Please enter a number between 1 and 5.")
        
        input("\nPress ENTER to return to the Main Menu...")

if __name__ == "__main__":
    main()
