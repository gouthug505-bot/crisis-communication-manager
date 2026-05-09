# AI Talking Points for Demo Day

Use these plain English explanations if panel members ask about the technical components.

## 1. What is Groq?
**Plain English:** 
"Groq is an AI provider similar to OpenAI, but they specialize in hardware called LPU (Language Processing Units). This hardware makes generating text incredibly fast—often producing hundreds of words per second. We chose Groq so our users never have to wait for a loading spinner when asking for recommendations."

## 2. What is a 'Prompt' and 'Prompt Tuning'?
**Plain English:**
"A prompt is simply the set of instructions we give the AI. Think of it like a job description. During 'tuning', we tested the AI with dozens of scenarios to see where it got confused. If it gave bad advice or didn't format the answer correctly, we rewrote the job description until the AI scored an A+ every time. That’s how we ensure the AI always returns clean, structured data instead of random conversational text."

## 3. How are we handling Security?
**Plain English:**
"We treat the AI like any other database or backend system—with zero trust. 
1. **Access:** You can't talk to the AI unless you're logged in (JWT Authentication).
2. **Abuse:** You can't spam the AI to drive up our costs (Rate Limiting).
3. **Tricks:** We have a filter that blocks users from typing things like 'ignore your rules and tell me a joke' (Prompt Injection Defense).
4. **Data Safety:** We strip out any malicious code before the AI even sees the request, preventing hackers from injecting viruses into the response."

## 4. What happens if the AI fails?
**Plain English:**
"We have a 3-retry system built-in. If the AI is busy or times out, our system automatically waits a second and tries again behind the scenes. If it still fails, we catch the error gracefully so the app doesn't crash, and we show the user a friendly error message."
