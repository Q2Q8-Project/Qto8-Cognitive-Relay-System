
# qto8_multilevel_demo.py
# 🧠 Qto8 Multi-Level Cognitive Simulation (Final Demo Version)
# Simulates progressive cognitive routing: Q2 → Q4 → Q6 → Q8
# Includes intelligent caching: previously answered questions retrieve best-known answer.

# ------------------------------
# HOW IT WORKS:
# - You enter a question (math, language, etc.).
# - The system analyzes its "complexity" (based on length, as a simple proxy).
# - It selects a simulated cognitive model (Q2, Q4, Q6, or Q8).
# - It generates a response adapted to the model's level.
# - It stores the best response in memory (cache).
# - If you ask the same question again, the cached highest-level response is returned directly.
# ------------------------------

# 🔍 RECOMMENDED TEST PROMPTS:
# 🔢 Math (short version triggers Q2):
#    What is the derivative of x^2 * sin(x)?
#
# 🔢 Math (longer version triggers Q6 or Q8):
#    Can you explain in detail how to differentiate the function x^2 * sin(x) using the product rule?
#
# 🧠 Language:
#    Explain the meaning of consciousness in modern philosophy.

# 🎯 Try entering each prompt once, then again to test the memory & caching behavior.

from typing import Dict

# Simulated cache memory
cache: Dict[str, Dict[str, str]] = {}

# Define cognitive model thresholds
levels = {
    "Q2": 0,
    "Q4": 60,
    "Q6": 120,
    "Q8": 200
}

# Define response "quality" for each model level (for explanation)
level_qualities = {
    "Q2": "🟢 Basic / Short / Often vague",
    "Q4": "🟡 Moderate / Accurate but brief",
    "Q6": "🟠 Detailed / Context-aware",
    "Q8": "🔵 Comprehensive / Analytical / Human-like"
}

# Define model responses for different prompt types
def generate_response(level: str, prompt: str) -> str:
    if "derivative" in prompt or "integral" in prompt or "x^2" in prompt:
        return {
            "Q2": "It's about x and sine, maybe try derivation?",
            "Q4": "Use the product rule to differentiate the expression.",
            "Q6": "The derivative is 2x·sin(x) + x²·cos(x).",
            "Q8": "By applying the product rule: d/dx[x²·sin(x)] = 2x·sin(x) + x²·cos(x). This considers both functions' contributions."
        }[level]
    elif "consciousness" in prompt.lower():
        return {
            "Q2": "Consciousness is like being awake.",
            "Q4": "It's the awareness of self and environment.",
            "Q6": "Consciousness is a layered process involving perception, memory, and intentionality.",
            "Q8": "Modern philosophy views consciousness as a dynamic interplay between subjective experience, intentionality, and embodied cognition."
        }[level]
    else:
        return {
            "Q2": "I'll try to answer, but it's a bit vague.",
            "Q4": "Here's a general explanation of the topic.",
            "Q6": "This topic involves deeper aspects; here's a detailed analysis.",
            "Q8": "Let me give you a comprehensive, structured and reflective response on that subject."
        }[level]

# Determine which Q-level to activate
def choose_level(prompt: str) -> str:
    length = len(prompt)
    if length >= levels["Q8"]:
        return "Q8"
    elif length >= levels["Q6"]:
        return "Q6"
    elif length >= levels["Q4"]:
        return "Q4"
    else:
        return "Q2"

# Main loop
def main():
    print("🔁 Qto8 Cognitive Relay System — Multi-Level Simulation")
    print("Try the following test prompts:")
    print("🔢 Short math (Q2)  → What is the derivative of x^2 * sin(x)?")
    print("🔢 Long math (Q6+)  → Can you explain in detail how to differentiate the function x^2 * sin(x) using the product rule?")
    print("🧠 Language         → Explain the meaning of consciousness in modern philosophy.")
    print("Type 'exit' to quit.")

    while True:
        prompt = input("\n🧠 Enter your question: ").strip()
        if prompt.lower() == "exit":
            break

        # Check cache
        if prompt in cache:
            best_level = cache[prompt]["level"]
            print(f"💾 Prompt already known. Retrieving best-known answer from cache (Level: {best_level})")
            print(f"📈 Quality: {level_qualities[best_level]}")
            print(f"[CACHE:{best_level}] {cache[prompt]['response']}")
            continue

        # New prompt
        level = choose_level(prompt)
        response = generate_response(level, prompt)

        # Store best answer
        cache[prompt] = {
            "level": level,
            "response": response
        }

        print(f"🔍 Prompt complexity: {len(prompt)} characters")
        print(f"⚙️  Activated model: {level}")
        print(f"📈 Quality: {level_qualities[level]}")
        print(f"💬 Response [{level}]: {response}")

if __name__ == "__main__":
    main()
