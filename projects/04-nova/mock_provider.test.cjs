'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { requestWithFallback } = require('./mock_provider_demo.cjs');

test('uses fallback when first provider fails', async () => {
  const providers = [
    { name: 'mock-primary', run: async () => { throw new Error('offline'); } },
    { name: 'mock-backup', run: async () => 'Test-only answer' }
  ];
  assert.deepEqual(await requestWithFallback('Example', providers), {
    provider: 'mock-backup', reply: 'Test-only answer'
  });
});

test('rejects empty prompt and empty provider replies', async () => {
  await assert.rejects(requestWithFallback('', [{ name: 'x', run: async () => 'x' }]));
  await assert.rejects(requestWithFallback('Question', [{ name: 'x', run: async () => '' }]));
});
