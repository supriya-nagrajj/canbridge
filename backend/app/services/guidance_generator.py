# backend/app/services/guidance_generator.py

import os
from groq import Groq

# -------------------------------------------------
# SYSTEM PROMPT (FINAL, STRUCTURED, PDF-FRIENDLY)
# -------------------------------------------------
SYSTEM_PROMPT = """
You are a medical support and wellness assistant.

Your task is to generate structured, non-clinical, patient-friendly supportive guidance
based on an AI cancer screening result.

IMPORTANT RULES:
- Do NOT diagnose diseases.
- Do NOT prescribe medications, treatments, or procedures.
- Do NOT give clinical or surgical advice.
- Do NOT estimate prognosis or survival.
- Do NOT claim medical authority.
- Always encourage consultation with qualified healthcare professionals.

OUTPUT REQUIREMENTS:
- Write in clear, professional language suitable for a medical report.
- Use clear section headings (written as normal text, not markdown symbols).
- Do NOT use bullet points, asterisks (*), or markdown formatting.
- Write in short, readable paragraphs.
- Maintain a calm, reassuring, and respectful tone.
- The content must be appropriate for a downloadable PDF.
- Keep the format consistent regardless of input variations.
- Keep each section structured and focused.
- Highlight each section header in bold text.

STRUCTURE YOUR RESPONSE USING THESE SECTIONS (when applicable):
- Introduction (Briefly acknowledge the screening result and its implications in a supportive manner. Do not keep a heavy tone for positive results.)
- Daily Lifestyle & Wellness (Provide general tips for healthy daily habits and routines)
- Nutrition & Dietary Guidance (You can provide general dietary suggestions and tips for balanced nutrition)
- Physical Activity & Body Care (You can suggest general physical activities suitable for most individuals)
- Mental & Emotional Well-being (Suggest stress management techniques and emotional support strategies)
- Ongoing Health Monitoring (Encourage regular health check-ups and monitoring practices)
- Closing Note

End with a gentle reminder to consult healthcare professionals for personalized medical advice.
"""

# -------------------------------------------------
# GROQ CLIENT
# -------------------------------------------------
def _get_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set in environment")
    return Groq(api_key=api_key)


# -------------------------------------------------
# USER PROMPT BUILDER
# -------------------------------------------------
def _build_user_prompt(cancer_type: str, prediction: str) -> str:
    """
    Builds a contextual user prompt depending on
    whether cancer is detected or not.
    """

    if "no tumor" in prediction.lower():
        return f"""
The user has undergone an AI-based cancer screening.

Cancer type screened: {cancer_type}
Screening result: No cancer detected

Generate a structured supportive wellness guide for a person with a negative screening result.

The guidance should:
- Reassure the user in a calm and professional manner
- Encourage long-term healthy lifestyle habits
- Include detailed but general dietary and nutrition guidance
- Promote physical activity and body care for overall wellness
- Address mental well-being and stress management
- Emphasize preventive healthcare and routine medical check-ups

Ensure the tone is supportive, informative, and not celebratory.
"""
    else:
        return f"""
The user has undergone an AI-based cancer screening.

Cancer type screened: {cancer_type}
Screening result: {prediction}

Generate a structured, non-clinical supportive care guide.

The guidance should:
- Acknowledge the emotional impact of a positive screening result
- Provide reassurance without minimizing the situation
- Include general nutrition and hydration guidance to support strength
- Suggest lifestyle adjustments that promote rest and overall well-being
- Encourage emotional support, stress reduction, and mental resilience
- Strongly emphasize consultation with qualified healthcare professionals

Ensure the tone remains calm, respectful, and empowering.
Do not suggest medications, treatments, or medical decisions.
"""


# -------------------------------------------------
# MAIN PUBLIC FUNCTION
# -------------------------------------------------
def generate_guidance(cancer_type: str, prediction: str) -> str:
    """
    Generates structured supportive care guidance using Groq + LLaMA.
    Returns clean plain text suitable for direct PDF inclusion.
    """

    client = _get_client()
    user_prompt = _build_user_prompt(cancer_type, prediction)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )

    return completion.choices[0].message.content.strip()
