import json
import os

# Load tips based on diagnosis results
TIPS_PATH = os.path.join("yield_boost", "tips.json")

def load_tips():
    try:
        with open(TIPS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading tips data:", str(e))
        return {}

def diagnose_yield(factors):
    """
    Takes a dictionary of farmer responses and returns a diagnosis report.
    factors = {
        "soil_fertility": "low",
        "water_access": "moderate",
        "pest_control": "none",
        "crop_rotation": "no",
        "seed_quality": "unknown"
    }
    """
    tips_data = load_tips()
    findings = []
    suggestions = []

    for factor, value in factors.items():
        result = tips_data.get(factor, {}).get(value)
        if result:
            findings.append(f"🔎 {factor.replace('_', ' ').title()}: {value.title()} — {result['issue']}")
            suggestions.append(f"✅ Recommendation: {result['tip']}")

    return findings, suggestions
