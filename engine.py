from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return True if all antecedents are true and consequent not yet known."""
        if rule.consequent in self.facts:
            return False

        for antecedent in rule.antecedents:
            if antecedent not in self.facts:
                return False

        return True

    def run(self) -> None:
        """The forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        fire_order = 0
        fireable_rules = []

        for rule in self.rules:
            if self.can_fire(rule):
                fireable_rules.append(rule)

        while (len(fireable_rules) != 0):
            fireable_rules.sort(key=lambda x: x.priority, reverse=True)
            current_rule = fireable_rules[0] # selects highest priority, ties favor first in list

            self.facts.add(current_rule.consequent)
            fire_order += 1
            self.trace.append({current_rule.name: (fire_order, current_rule.antecedents, current_rule.consequent)})

            fireable_rules.clear()
            for rule in self.rules:
                if self.can_fire(rule):
                    fireable_rules.append(rule)

        pass

    def conclusions(self) -> Dict[str, List[str]]:
        """Return separated results (recommendations, specs, other facts)."""
        recs = []
        specs = []
        other = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recs.append(fact)
            elif fact.startswith("spec:"):
                specs.append(fact)
            else:
                other.append(fact)

        return {"recommendations": recs, "specs": specs, "other": other}