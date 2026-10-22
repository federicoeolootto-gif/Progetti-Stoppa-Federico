"""Synthetic stateful auction event ingestion demo; NOT private platform source."""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class AuctionState:
    budgets: dict[str, int]
    last_bid: dict[str, int] = field(default_factory=dict)
    leading_bidder: dict[str, str] = field(default_factory=dict)
    purchases: list[tuple[str, str, int]] = field(default_factory=list)
    processed_events: dict[str, tuple[str, str, str, int]] = field(default_factory=dict)

    def consume(self, event: dict) -> bool:
        """Return False for duplicate events, True for newly applied events."""
        needed = {"event_id", "kind", "player", "team", "price"}
        if not needed.issubset(event):
            raise ValueError("Missing fields")
        event_id, kind, player, team, price = (
            event["event_id"], event["kind"], event["player"], event["team"], event["price"]
        )
        if not all(isinstance(v, str) and v.strip() for v in (event_id, kind, player, team)):
            raise ValueError("IDs and labels must be non-empty strings")
        if type(price) is not int or price <= 0:
            raise ValueError("Price must be a positive integer")
        fingerprint = (kind, player, team, price)
        if event_id in self.processed_events:
            if self.processed_events[event_id] != fingerprint:
                raise ValueError("Conflicting payload for an already processed event ID")
            return False  # Identical retries cannot decrement budgets twice.
        if team not in self.budgets:
            raise ValueError("Unknown synthetic participant")
        if kind == "BID":
            if any(p == player for p, _, _ in self.purchases):
                raise ValueError("Player already sold")
            if price <= self.last_bid.get(player, 0):
                raise ValueError("Bid must increase")
            if price > self.budgets[team]:
                raise ValueError("Bid exceeds available budget")
            self.last_bid[player] = price
            self.leading_bidder[player] = team
        elif kind == "PURCHASE":
            if any(p == player for p, _, _ in self.purchases):
                raise ValueError("Player already sold")
            if price < self.last_bid.get(player, 0):
                raise ValueError("Purchase below highest bid")
            if player in self.leading_bidder and team != self.leading_bidder[player]:
                raise ValueError("Buyer does not match highest bidder")
            if price > self.budgets[team]:
                raise ValueError("Purchase exceeds budget")
            self.budgets[team] -= price
            self.purchases.append((player, team, price))
            self.last_bid.pop(player, None)
            self.leading_bidder.pop(player, None)
        else:
            raise ValueError("Unsupported event kind")
        self.processed_events[event_id] = fingerprint
        return True


def sample_events() -> list[dict]:
    return [
        {"event_id": "event-1", "kind": "BID", "player": "Player-A", "team": "Team-1", "price": 12},
        {"event_id": "event-2", "kind": "BID", "player": "Player-A", "team": "Team-2", "price": 15},
        {"event_id": "event-3", "kind": "PURCHASE", "player": "Player-A", "team": "Team-2", "price": 15},
    ]


if __name__ == "__main__":
    state = AuctionState(budgets={"Team-1": 100, "Team-2": 100})
    for event in sample_events():
        state.consume(event)
    assert not state.consume(sample_events()[-1])
    assert state.budgets["Team-2"] == 85
    print("Synthetic state:", state.purchases, state.budgets)
