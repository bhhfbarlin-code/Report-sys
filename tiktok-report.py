import os
import webbrowser
from datetime import datetime

TOOL_NAME = "TIKTOK REPORT SYSTEM"
AUTHOR = "KARLO X MARCO"
REPORT_FILE = "tiktok_reports.txt"

TIKTOK_REPORT_URL = "https://www.tiktok.com/legal/report/feedback"


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def banner():
    clear()

    print("=" * 50)
    print("          TIKTOK REPORT SYSTEM")
    print("=" * 50)
    print(f"          Author: {AUTHOR}")
    print("=" * 50)


def create_report():

    print("\nEnter TikTok Video URL:")
    url = input("> ").strip()

    print("\nSelect Report Reason:")
    print("1. Privacy Violation")
    print("2. Harassment / Bullying")
    print("3. Impersonation")
    print("4. Scam / Fraud")
    print("5. Other")

    choice = input("\nChoice: ").strip()

    reports = {

        "1": (
            "Privacy Violation",
            "I am reporting this content because it appears "
            "to involve personal or private content being "
            "shared without the necessary permission or "
            "authorization. Please review the content under "
            "TikTok's privacy policies and take appropriate "
            "action if a violation is confirmed."
        ),

        "2": (
            "Harassment / Bullying",
            "I am reporting this content because it appears "
            "to contain or contribute to harassment or "
            "bullying. Please review the reported content "
            "under TikTok's Community Guidelines and take "
            "appropriate action if a violation is confirmed."
        ),

        "3": (
            "Impersonation",
            "I am reporting this content because it appears "
            "to involve impersonation or misleading "
            "representation of another person. Please "
            "review the content and take appropriate action "
            "if it violates TikTok's applicable policies."
        ),

        "4": (
            "Scam / Fraud",
            "I am reporting this content because it appears "
            "to be associated with potentially deceptive "
            "or fraudulent activity. Please review the "
            "content and take appropriate action if a "
            "violation is confirmed."
        ),

        "5": (
            "Other",
            "I am reporting this content because I believe "
            "it may violate TikTok's applicable policies "
            "or Community Guidelines. Please review the "
            "reported content and take appropriate action "
            "if a violation is confirmed."
        )
    }

    reason, report_text = reports.get(
        choice,
        reports["5"]
    )

    print("\n" + "=" * 50)
    print("              REPORT DETAILS")
    print("=" * 50)

    print(f"Tool   : {TOOL_NAME}")
    print(f"Author : {AUTHOR}")
    print(f"Reason : {reason}")
    print(f"URL    : {url}")

    print("\nReport Text:")
    print("-" * 50)
    print(report_text)
    print("-" * 50)

    with open(
        REPORT_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Tool: {TOOL_NAME}\n")
        file.write(f"Author: {AUTHOR}\n")
        file.write(
            "Date: "
            + datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            + "\n"
        )
        file.write(f"Video URL: {url}\n")
        file.write(f"Reason: {reason}\n\n")
        file.write(report_text + "\n")
        file.write("=" * 50 + "\n")

    print(f"\nReport saved to: {REPORT_FILE}")

    open_page = input(
        "\nOpen TikTok official reporting page? (y/n): "
    ).lower()

    if open_page == "y":
        webbrowser.open(TIKTOK_REPORT_URL)

    input("\nPress Enter to continue...")


def view_reports():

    banner()

    print("\nSAVED REPORTS")
    print("=" * 50)

    if not os.path.exists(REPORT_FILE):

        print("No saved reports found.")

    else:

        with open(
            REPORT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            print(file.read())

    input("\nPress Enter to continue...")


def open_tiktok():

    webbrowser.open(TIKTOK_REPORT_URL)

    print(
        "\nTikTok official reporting page opened."
    )

    input("\nPress Enter to continue...")


def main():

    while True:

        banner()

        print("\n[1] Create Report")
        print("[2] View Saved Reports")
        print("[3] Open TikTok Report Page")
        print("[4] Exit")

        choice = input(
            "\nSelect option: "
        ).strip()

        if choice == "1":

            create_report()

        elif choice == "2":

            view_reports()

        elif choice == "3":

            open_tiktok()

        elif choice == "4":

            clear()

            print("=" * 50)
            print(f"        {TOOL_NAME}")
            print(f"        Author: {AUTHOR}")
            print("=" * 50)
            print("\nGoodbye!")

            break

        else:

            print("\nInvalid option.")
            input("Press Enter...")


if __name__ == "__main__":
    main()