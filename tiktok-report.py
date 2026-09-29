import os
import textwrap
import webbrowser
from datetime import datetime

TOOL_NAME = "TIKTOK REPORT SYSTEM"
AUTHOR = "KARLO X MARCO"
REPORT_FILE = "tiktok_reports.txt"
TIKTOK_URL = "https://www.tiktok.com/legal/report/feedback"

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def width():
    try:
        return max(42, min(os.get_terminal_size().columns, 72))
    except OSError:
        return 60


def line():
    print(GRAY + "─" * width() + RESET)


def title(text):
    w = width()
    print(CYAN + "╔" + "═" * (w - 2) + "╗" + RESET)
    print(
        CYAN + "║" +
        BOLD + WHITE + text.center(w - 2) +
        RESET + CYAN + "║" + RESET
    )
    print(CYAN + "╚" + "═" * (w - 2) + "╝" + RESET)


def wrap(text):
    return textwrap.fill(
        text,
        width=max(35, width() - 4),
        break_long_words=False,
        break_on_hyphens=False
    )


def pause():
    input(
        "\n" + GRAY +
        "Press ENTER to continue..." +
        RESET
    )


def banner():
    clear()
    print()
    title(TOOL_NAME)
    print(CYAN + "  Professional Report Assistant" + RESET)
    print(GRAY + f"  Author : {AUTHOR}" + RESET)
    print()
    line()


CATEGORIES = {

    "Privacy Violation": {
        "keywords": [
            "private",
            "privacy",
            "personal",
            "without permission",
            "without consent",
            "uploaded without",
            "personal video",
            "private video"
        ],
        "reason": (
            "The information provided may indicate that "
            "personal or private material was shared "
            "without the necessary permission."
        )
    },

    "Harassment / Bullying": {
        "keywords": [
            "harass",
            "harassment",
            "bully",
            "bullying",
            "abuse",
            "abusive",
            "insult",
            "threat",
            "target",
            "humiliate"
        ],
        "reason": (
            "The description may indicate targeted "
            "harassment, bullying, abusive behavior, "
            "or threatening content."
        )
    },

    "Impersonation": {
        "keywords": [
            "impersonate",
            "impersonation",
            "fake account",
            "pretending to be",
            "pretend",
            "posing as"
        ],
        "reason": (
            "The information may indicate that someone "
            "is pretending to be or representing another "
            "person."
        )
    },

    "Scam / Fraud": {
        "keywords": [
            "scam",
            "fraud",
            "fraudulent",
            "money scam",
            "fake offer",
            "fake payment",
            "cheat",
            "cheating",
            "deception"
        ],
        "reason": (
            "The description may indicate deceptive, "
            "fraudulent, or scam-related activity."
        )
    },

    "Copyright": {
        "keywords": [
            "copyright",
            "copied my video",
            "stolen video",
            "reuploaded",
            "re-uploaded",
            "my original video",
            "without authorization"
        ],
        "reason": (
            "The information may indicate unauthorized "
            "use or distribution of copyrighted material."
        )
    }
}


def analyze_category(description):

    text = description.lower()
    scores = {}

    for category, data in CATEGORIES.items():

        score = 0

        for keyword in data["keywords"]:

            if keyword in text:
                score += 1

        scores[category] = score

    matched = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    best_category, best_score = matched[0]

    if best_score == 0:
        return "Other", 0, []

    alternatives = [
        item for item in matched
        if item[1] > 0
    ]

    return best_category, best_score, alternatives


def show_analysis(description):

    category, score, alternatives = analyze_category(
        description
    )

    print()
    title("REPORT CATEGORY ANALYZER")
    print()

    if score == 0:

        print(
            YELLOW +
            "  Suggested Category : OTHER" +
            RESET
        )

        print(
            GRAY +
            "  No specific category was detected." +
            RESET
        )

        return category

    print(
        GREEN +
        f"  Suggested Category : {category}" +
        RESET
    )

    print(
        WHITE +
        f"  Match Indicators    : {score}" +
        RESET
    )

    print()
    print(
        CYAN +
        "  Why this category?" +
        RESET
    )

    print(
        "  " +
        wrap(CATEGORIES[category]["reason"])
    )

    if len(alternatives) > 1:

        print()
        print(
            CYAN +
            "  Other possible categories:" +
            RESET
        )

        for name, points in alternatives[1:4]:

            print(
                f"  • {name} ({points} indicator)"
            )

    print()
    print(
        YELLOW +
        "  This is only a category suggestion." +
        RESET
    )

    return category


def generate_report(category, description):

    templates = {

        "Privacy Violation":
            "I am reporting this content because it appears "
            "to involve personal or private material being "
            "shared without the necessary permission or "
            "authorization. Please review the reported "
            "content under TikTok's applicable privacy "
            "policies and Community Guidelines and take "
            "appropriate action if a violation is confirmed.",

        "Harassment / Bullying":
            "I am reporting this content because it appears "
            "to involve harassment, bullying, abusive "
            "behavior, or targeted conduct. Please review "
            "the video, captions, audio, and surrounding "
            "context under TikTok's applicable Community "
            "Guidelines and take appropriate action if a "
            "violation is confirmed.",

        "Impersonation":
            "I am reporting this content because it appears "
            "to involve impersonation or misleading "
            "representation of another person. Please "
            "review the reported content and account "
            "context to determine whether it violates "
            "TikTok's applicable policies.",

        "Scam / Fraud":
            "I am reporting this content because it appears "
            "to involve potentially deceptive or fraudulent "
            "activity. Please review the reported content "
            "and the information provided below to determine "
            "whether it violates TikTok's applicable policies.",

        "Copyright":
            "I am reporting this content because I believe "
            "it may contain or distribute copyrighted "
            "material without the necessary authorization. "
            "Please review the reported content under "
            "TikTok's applicable intellectual property "
            "policies.",

        "Other":
            "I am reporting this content because I believe "
            "it may violate TikTok's applicable policies "
            "or Community Guidelines. Please review the "
            "reported content and the additional information."
    }

    base = templates.get(
        category,
        templates["Other"]
    )

    return (
        base +
        "\n\nAdditional context provided by the reporter:\n" +
        description
    )


def create_report():

    banner()

    print(CYAN + "VIDEO INFORMATION" + RESET)
    line()

    url = input(
        "TikTok Video URL\n> "
    ).strip()

    if not url:

        print(
            RED +
            "\nURL cannot be empty." +
            RESET
        )

        pause()
        return

    print()

    print(
        CYAN +
        "Describe what actually happens in the video." +
        RESET
    )

    print(
        GRAY +
        "Use factual information only." +
        RESET
    )

    description = input("\n> ").strip()

    if not description:

        print(
            RED +
            "\nDescription cannot be empty." +
            RESET
        )

        pause()
        return

    category = show_analysis(description)

    print()

    report = generate_report(
        category,
        description
    )

    title("PROFESSIONAL ADDITIONAL INFORMATION")

    print()
    print(wrap(report))
    print()

    line()

    print(
        GREEN +
        "Report generated successfully." +
        RESET
    )

    with open(
        REPORT_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write(f"Tool: {TOOL_NAME}\n")
        file.write(f"Author: {AUTHOR}\n")
        file.write(
            "Date: " +
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ) +
            "\n"
        )
        file.write(
            f"Category: {category}\n"
        )
        file.write(
            f"Video URL: {url}\n\n"
        )
        file.write(report)
        file.write("\n")
        file.write("=" * 60 + "\n")

    print()
    print(
        GREEN +
        f"Saved to: {REPORT_FILE}" +
        RESET
    )

    print()

    open_page = input(
        "Open TikTok official report page? [y/n]: "
    ).lower()

    if open_page == "y":
        webbrowser.open(TIKTOK_URL)

    pause()


def view_reports():

    banner()
    title("SAVED REPORTS")
    print()

    if not os.path.exists(REPORT_FILE):

        print(
            YELLOW +
            "No saved reports found." +
            RESET
        )

    else:

        with open(
            REPORT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            print(file.read())

    pause()


def open_tiktok():

    banner()

    print(
        GREEN +
        "Opening TikTok official reporting page..." +
        RESET
    )

    webbrowser.open(TIKTOK_URL)

    pause()


def about():

    banner()
    title("ABOUT")
    print()

    print(f"Tool   : {TOOL_NAME}")
    print(f"Author : {AUTHOR}")
    print("Mode   : Report Assistant")
    print("Engine : Python")

    print()

    print(
        wrap(
            "This tool organizes factual information, "
            "suggests a potentially relevant report category, "
            "and prepares professional additional information "
            "for manual submission."
        )
    )

    print()

    print(
        YELLOW +
        "It does not guarantee content removal or faster review." +
        RESET
    )

    pause()


def main():

    while True:

        banner()

        print()
        print(
            f"{CYAN}[1]{RESET} "
            "Create Professional Report"
        )

        print(
            f"{CYAN}[2]{RESET} "
            "Report Category Analyzer"
        )

        print(
            f"{CYAN}[3]{RESET} "
            "View Saved Reports"
        )

        print(
            f"{CYAN}[4]{RESET} "
            "Open TikTok Report Page"
        )

        print(
            f"{CYAN}[5]{RESET} "
            "About Tool"
        )

        print(
            f"{RED}[6]{RESET} "
            "Exit"
        )

        line()

        choice = input(
            "\nSelect option > "
        ).strip()

        if choice == "1":
            create_report()

        elif choice == "2":

            banner()

            print(
                "Enter a description of the content:"
            )

            description = input(
                "\n> "
            ).strip()

            if description:
                show_analysis(description)
            else:
                print(
                    RED +
                    "\nNo description provided." +
                    RESET
                )

            pause()

        elif choice == "3":
            view_reports()

        elif choice == "4":
            open_tiktok()

        elif choice == "5":
            about()

        elif choice == "6":

            clear()

            print(
                CYAN +
                TOOL_NAME +
                RESET
            )

            print(
                f"Author: {AUTHOR}"
            )

            print("\nGoodbye.")
            break

        else:

            print(
                RED +
                "\nInvalid option." +
                RESET
            )

            pause()


if __name__ == "__main__":
    main()