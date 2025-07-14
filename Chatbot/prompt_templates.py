from langchain.prompts import PromptTemplate

# 🌿 Prompt: Organic Certification Help
certification_prompt = PromptTemplate.from_template(
    "You are an expert in organic farming. Explain the steps for organic certification in {region} for a farmer growing {crop}. Provide a friendly and concise summary."
)

# 🦠 Prompt: Crop Disease Explanation
disease_explanation_prompt = PromptTemplate.from_template(
    "As an agricultural expert, describe the symptoms and recommended treatment for {disease_name} in organic farming, keeping advice safe, natural, and eco-friendly."
)

# 📉 Prompt: Low Yield Diagnosis Follow-Up
yield_followup_prompt = PromptTemplate.from_template(
    "A farmer is experiencing low yields with {crop}. They reported issues with {factor}. Suggest practical organic solutions tailored to small-scale farms."
)

# 🧠 Prompt: Personalized Chat Response
organic_chat_prompt = PromptTemplate.from_template(
    "Act as an organic farming assistant. A farmer asked: '{query}'. Reply in a helpful, conversational tone and include eco-friendly recommendations."
)

# 🌱 Prompt: Crop Rotation Advice
crop_rotation_prompt = PromptTemplate.from_template(
    "As an organic farming expert, provide advice on crop rotation practices for {crop}. Include benefits and practical tips."
)