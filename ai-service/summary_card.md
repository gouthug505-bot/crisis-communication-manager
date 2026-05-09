# AI Integration Summary

**Project:** AI Service Backend  
**Goal:** Provide secure, rapid, and structured AI generation capabilities.

## Tech Stack
*   **Backend Framework:** Python Flask (Lightweight, robust routing)
*   **AI Engine:** Groq API (Ultra-low latency Llama-3 inference)
*   **Security:** PyJWT (Authentication), Flask-Limiter (Rate Limiting), Bleach (XSS Prevention)
*   **Testing:** Pytest (Unit Testing, Mocking)
*   **Deployment:** Docker & Docker Compose (Containerized E2E Environment)

## Core Endpoints
1.  **`/api/recommend`**: Takes a user profile and context to generate 3 actionable, personalized recommendations with confidence scores.
2.  **`/api/report`**: Transforms raw data summaries into structured executive reports with key findings and conclusions.
3.  **`/api/generate`**: A secure, general-purpose prompt endpoint.

## Security Posture
*   **Authentication Required:** All AI endpoints enforce `Bearer` JWT validation.
*   **Rate Limiting:** Capped at 30 requests per minute to prevent API exhaustion.
*   **Injection Defense:** Custom middleware detects and rejects prompt overriding attempts.
*   **Data Safety:** HTML stripping prevents XSS; PII audits ensure no sensitive data leaks.

**GitHub Repository:** [Insert Link Here]
*(Print 2 copies for Demo Day)*
