import test from '@playwright/test';

test('Plugin - Panels', async ({ page }) => {
    await page.goto('/');

    // TODO: Flesh this out somewhat...

    await page.waitForTimeout(2500);
});