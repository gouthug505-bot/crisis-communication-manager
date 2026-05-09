# Post-Demo Notes & Retrospective

**Date:** 2026-05-09
**Presenter(s):** [Your Name(s)]
**Mentor Feedback:** [To be filled out during/after Demo]

## Lessons Learned
1. **Prompt Engineering is Fragile:** We realized that slight changes in the prompt could break the JSON format. Enforcing strict JSON schema expectations and using Groq's `response_format={"type": "json_object"}` was a game-changer.
2. **Security vs Usability:** Implementing JWT auth and rate limiting early saved us from rewriting endpoints later.
3. **Middleware is Powerful:** Using Flask's `before_request` to centrally handle HTML stripping and basic injection detection kept our route logic clean.

## Questions from the Panel
*   *Question 1:* 
    *   *Our Answer:* 
*   *Question 2:* 
    *   *Our Answer:* 

## Features for Future Sprints
1. **Secondary AI Validator:** Instead of relying just on a keyword blocklist for prompt injections, use a smaller, faster model (e.g., Llama-3-8b) specifically to classify incoming prompts as safe/unsafe before sending them to the main generator.
2. **User Context Memory:** Store previous user recommendations in a database to provide "follow-up" context to the AI for iterative conversations.
3. **Admin Dashboard:** A UI to visualize rate limits hit, token usage, and flagged injection attempts.
4. **Streaming Responses:** Implement Server-Sent Events (SSE) to stream the AI response word-by-word back to the frontend for an even faster perceived load time.
