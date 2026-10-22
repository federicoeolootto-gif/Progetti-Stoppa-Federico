# Nova — AI Desktop Assistant (Individual Project)

The privately developed Electron/Node.js application integrates external model APIs (including Gemini and Groq), local document retrieval, speech transcription, streaming responses, fallback logic, and mathematical rendering. **API integration is an important part of the project's technical scope.** No proprietary model training is claimed.

**Public code:** [`mock_provider_demo.cjs`](mock_provider_demo.cjs) is a small **independent offline reimplementation** of provider orchestration with safe mocked responses. Its [tests](mock_provider.test.cjs) illustrate failure/fallback behavior without any network traffic or real API keys. This code is not the private Electron application's original source or a performance benchmark.

```bash
node --test mock_provider.test.cjs
```

The original application is not redistributed: it contains unreviewed functionality/configuration and material inappropriate for a recruiter-facing open-source demo. This portfolio focuses on transparent, consent-based document-assisted workflows. Screenshots, conversations and real voice recordings are excluded.
