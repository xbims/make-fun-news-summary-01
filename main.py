"""make.fun bounty news-summary-01.

Writes one English summary of the world's news of Wednesday
11 November 2026 to /output/entry.txt.

Standard library only. Deterministic: no network, no time,
no randomness. Running it twice produces identical bytes.
"""

from pathlib import Path

SUMMARY = (
    "On 11 November 2026, Nvidia's board prepared to oust chief executive "
    "Jensen Huang after reports of two affairs, one with a Megaspeed "
    "executive US officials suspect of spying for China, the Wall Street "
    "Journal reported; shares fell about 8% after hours. "
    "Russia and Ukraine agreed in principle in Abu Dhabi to their largest "
    "prisoner exchange, possibly 1,000 to 1,500 each, but reached no "
    "ceasefire, the Associated Press reported. "
    "Russia's ambassador to the United States, Alexander Darchiev, died "
    "suddenly in Moscow aged 66, Reuters reported. "
    "At COP31 in Antalya, UN chief Antonio Guterres warned the climate "
    "crisis was \"outrunning us\", Reuters reported. "
    "Iran's army said a tanker caught fire after hitting a mine in the "
    "Strait of Hormuz, while British maritime authorities confirmed only "
    "an incident, Tasnim reported. "
    "Spain held its first general strike in 14 years over housing costs, "
    "with about 4 million workers taking part and at least 49 arrests, "
    "the Associated Press reported. "
    "US Soccer withdrew its men's under-17 team from the World Cup in "
    "Qatar over safety concerns, Reuters reported. "
    "In Gaza, Israeli strikes killed five people as floods submerged "
    "70,000 tents, Al Jazeera reported. "
    "Sudan's army said it shot down two drones, bringing its claimed "
    "total to 29, Sudan Now reported. "
    "The 990-foot SS United States was sunk off Florida to become the "
    "world's largest artificial reef, the Pensacola News Journal reported."
)


def main() -> None:
    # The bounty requires 1 to 2,000 characters; fail loudly instead of
    # writing an entry the gate would reject.
    if not 1 <= len(SUMMARY) <= 2000:
        raise ValueError(f"summary is {len(SUMMARY)} characters, expected 1-2000")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
