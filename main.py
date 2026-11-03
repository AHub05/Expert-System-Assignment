from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # Ask questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Do you primarily game? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is this for the office? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("Do you prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you prefer linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    if input("Do you prefer windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")
    if input("Do you attend to work with AI? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you want a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference

    ie = ForwardChainingEngine(load_rules(KB_PATH))

    ie.assert_facts(collect_initial_facts())

    ie.run

    Conclusions = ie.conclusions()

    print(ie.trace)

    pass

if __name__ == "__main__":
    main()
