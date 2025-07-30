from openai import OpenAI
import json

from config import openai_settings
from services.logger import logger

client = OpenAI(api_key=openai_settings.OPENAI_TOKEN)  # or replace with your key

def extract_jd_data(jd_text: str) -> dict:
    logger.info("interacting with openai to parse the JD!!")
    prompt = f"""
    Extract the following structured information from the JD below:
    - Job Title
    - Location
    - Salary Range (Integer or null)
    - Skills (as list)
    - Responsibilities (as list)
    - Requirements
    - Benefits

    JD:
    {jd_text}

    Respond in JSON format like:
    {{
      "job_title": "",
      "location": "",
      "salary_range": "",
      "experience_level": "",
      "job_type": "",
      "skills": [],
      "responsibilities": [],
      "requirements": [],
      "benefits": []
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",#"gpt-4.1",
        messages=[
            {"role": "system", "content": "You are an expert at parsing job descriptions into structured data."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_input = response.choices[0].message.content

    try:
        json_string = raw_input.strip().removeprefix("```json").removesuffix("```").strip()
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        logger.error("Warning: Could not parse JSON. Raw output: %s", e)
        return {}