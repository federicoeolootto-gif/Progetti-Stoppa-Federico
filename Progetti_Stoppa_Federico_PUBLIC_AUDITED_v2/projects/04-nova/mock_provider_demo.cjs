'use strict';
// Offline illustration of fallbacks. This file does not make API calls.
// Never embed API credentials in source. Production apps should use secure OS key storage.

async function requestWithFallback(prompt, providers) {
  if (typeof prompt !== 'string' || !prompt.trim()) throw new Error('Prompt is required');
  if (!Array.isArray(providers) || providers.length === 0) throw new Error('Providers required');
  const errors = [];
  for (const provider of providers) {
    try {
      if (typeof provider.run !== 'function') throw new Error('Missing provider function');
      const reply = await provider.run(prompt);
      if (typeof reply !== 'string' || !reply.trim()) throw new Error('Empty response');
      return { provider: provider.name, reply };
    } catch (error) {
      errors.push(`${provider.name || 'unknown'}: unavailable`);
    }
  }
  throw new Error(`No provider returned a valid response (${errors.length} attempts)`);
}

module.exports = { requestWithFallback };
