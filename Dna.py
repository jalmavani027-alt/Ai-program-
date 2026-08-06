import hashlib
import random

traits = {
    "Intelligence": ["Average", "Smart", "Genius", "Mastermind"],
    "Creativity": ["Normal", "Creative", "Inventive", "Visionary"],
    "Luck": ["Low", "Medium", "High", "Legendary"],
    "Energy": ["Calm", "Active", "Hyper", "Unstoppable"],
    "Focus": ["Distracted", "Focused", "Laser Focused", "Monk Mode"]
}

bases = ["A", "T", "G", "C"]

name = input("Enter your name: ").strip()

seed = int(hashlib.sha256(name.encode()).hexdigest(), 16)
random.seed(seed)

dna = "".join(random.choice(bases) for _ in range(120))

print("\n" + "=" * 50)
print("      VIRTUAL DNA ANALYZER")
print("=" * 50)

for i in range(0, len(dna), 30):
    print(dna[i:i+30])

print("\nGENETIC TRAITS")
print("-" * 50)

for trait, values in traits.items():
    print(f"{trait:<15}: {random.choice(values)}")

gc = dna.count("G") + dna.count("C")
gc_percent = gc / len(dna) * 100

print("\nDNA Statistics")
print("-" * 50)
print(f"Length      : {len(dna)}")
print(f"GC Content  : {gc_percent:.2f}%")
print(f"Unique ID   : {hashlib.md5(dna.encode()).hexdigest()[:16].upper()}")

print("\nThis DNA is generated mathematically from your name.")
