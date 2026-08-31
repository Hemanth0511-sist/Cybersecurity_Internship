import json


QUESTIONS = [
    {
        "q": "An email asks you to verify your password through a link. What should you do?",
        "opts": ["A) Click the link", "B) Contact IT through an official channel", "C) Reply with the password"],
        "ans": "B",
        "exp": "Verify requests through an official channel and never provide passwords through unexpected links."
    },
    {
        "q": "You find an unknown USB drive in a parking lot. What should you do?",
        "opts": ["A) Plug it into your computer", "B) Give it to security/IT", "C) Take it home"],
        "ans": "B",
        "exp": "Unknown USB devices can be used for baiting attacks."
    },
    {
        "q": "A caller claims to be IT support and asks for your password. What should you do?",
        "opts": ["A) Provide it", "B) Verify the caller through an official channel", "C) Write it down for them"],
        "ans": "B",
        "exp": "Legitimate support should not require you to disclose your password."
    },
    {
        "q": "Which is a common social-engineering warning sign?",
        "opts": ["A) Unexpected urgency", "B) Normal documentation", "C) Scheduled meeting"],
        "ans": "A",
        "exp": "Urgency and pressure are commonly used to influence victims."
    },
    {
        "q": "You receive an unexpected attachment from an unknown sender. What is safest?",
        "opts": ["A) Open it immediately", "B) Verify the sender before opening", "C) Forward it to friends"],
        "ans": "B",
        "exp": "Unexpected attachments should be verified before opening."
    },
    {
        "q": "A message says your account will be closed in 10 minutes unless you act. What should you do?",
        "opts": ["A) Act immediately", "B) Verify independently", "C) Send your credentials"],
        "ans": "B",
        "exp": "Artificial urgency is a common social-engineering technique."
    },
    {
        "q": "What is phishing?",
        "opts": ["A) A backup method", "B) A fraudulent attempt to obtain information", "C) A software update"],
        "ans": "B",
        "exp": "Phishing uses deceptive communications to obtain information or influence actions."
    },
    {
        "q": "Which action helps protect against impersonation?",
        "opts": ["A) Trust caller ID alone", "B) Independently verify the person's identity", "C) Share internal information"],
        "ans": "B",
        "exp": "Identity should be verified using an independent trusted method."
    },
    {
        "q": "What should you do with a suspicious security email?",
        "opts": ["A) Report it through the organization's security process", "B) Reply with your password", "C) Forward it externally"],
        "ans": "A",
        "exp": "Reporting suspicious messages helps security teams investigate them."
    },
    {
        "q": "Which is a safe response to an unexpected request for confidential information?",
        "opts": ["A) Provide it quickly", "B) Refuse and verify through an official channel", "C) Send partial information"],
        "ans": "B",
        "exp": "Confidential information should only be shared after proper verification."
    }
]


def run_quiz():
    score = 0
    results = []

    print("=" * 65)
    print("       DAY 11 - SOCIAL ENGINEERING AWARENESS QUIZ")
    print("=" * 65)
    print("Answer each question using A, B, or C.")
    print()

    for i, question in enumerate(QUESTIONS, 1):

        print(f"\nQ{i}: {question['q']}")

        for option in question["opts"]:
            print(option)

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()

            if answer in ["A", "B", "C"]:
                break

            print("Please enter A, B, or C.")

        if answer == question["ans"]:
            print("Correct!")
            score += 1
            correct = True
        else:
            print("Incorrect.")
            print("Explanation:", question["exp"])
            correct = False

        results.append({
            "question": question["q"],
            "answer_given": answer,
            "correct_answer": question["ans"],
            "correct": correct
        })

    percentage = (score / len(QUESTIONS)) * 100

    report = {
        "total_questions": len(QUESTIONS),
        "score": score,
        "percentage": percentage,
        "results": results
    }

    with open("day11_score_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("\n" + "=" * 65)
    print("                  QUIZ COMPLETE")
    print("=" * 65)
    print(f"Score      : {score}/{len(QUESTIONS)}")
    print(f"Percentage : {percentage:.1f}%")
    print("Report     : day11_score_report.json")
    print("=" * 65)


if __name__ == "__main__":
    run_quiz()