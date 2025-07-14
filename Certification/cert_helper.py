import json
import os

# Certification data (region/crop specific rules)
DATA_PATH = os.path.join("certification","cert_data.json")

def load_certification_data():
  """
  Load certification data from a JSON file.
  """
  try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
      data = json.load(f)
      return data
  except Exception as e:
    print("Errorloading certification data:", str(e))
    return {}

def get_certification_steps(region, crop):
  """
  Get certification steps for a specific region and crop.
  """
  data = load_certification_data()
  region_info = data.get(region.lower())
  if not region_info:
    return f"Certification details for region '{region}' are not available."

  crop_steps = region_info.get("crops", {}).get(crop.lower())
  if crop_steps:
    return f"🌿 Certification Steps for {crop.title()} in {region.title()}:\n\n" + "\n".join(
      [f"{i+1}. {step}" for i, step in enumerate(crop_steps)]
    )
  else:
    generic = region_info.get("generic_steps", [])
    return f"No specific info for '{crop}'. Here's a generic certification process for {region.title()}:\n\n" + "\n".join(
      [f"{i+1}. {step}" for i, step in enumerate(generic)]
    )