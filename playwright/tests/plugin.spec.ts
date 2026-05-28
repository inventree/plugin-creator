import test, { Page } from '@playwright/test';

const BASE_URL = 'http://localhost:8000';


interface LoginOptions {
    username?: string;
    password?: string;
};


// Perform login for the given page
const doLogin = async (page: Page, options: LoginOptions = {}) => {

    await page.goto(BASE_URL);

    // Assume that we are on the login page, and perform login
    await page.getByRole('textbox', { name: 'login-username' }).fill(options?.username || 'steven');
    await page.getByRole('textbox', { name: 'login-password' }).fill(options?.password || 'wizardstaff');
    await page.getByRole('button', { name: 'Log In' }).click();
    await page.waitForLoadState('networkidle');

    await page.getByText('InvenTree Demo Server').first().waitFor();
}


/**
 * First test - activate the plugin, and ensure it is loaded correctly (no errors in console)
 * Note: This requires a superuser account
 */
test('Plugin - Activate', async ({ page }) => {
    await doLogin(page, { username: 'admin', password: 'inventree' });

    await page.goto(`${BASE_URL}/web/settings/admin/plugin`);
    await page.getByRole('textbox', { name: 'table-search-input' }).fill('custom');

    await page.waitForTimeout(500);
    await page.waitForLoadState('networkidle');
    
    // Right click on the plugin row, and activate the plugin
    await page.getByRole('cell', { name: 'MyCustomPlugin' }).click({ button: 'right' });
    
    const deactivateButton = page.getByRole('button', { name: 'Deactivate', exact: true });
    
    if (await deactivateButton.isVisible({ timeout: 2000 })) {
        // Plugin is already active - deactivate it first
        await deactivateButton.click();
        await page.getByText('The selected plugin will be deactivated').waitFor();
        await page.getByRole('button', { name: 'Submit', exact: true }).click();
        await page.waitForTimeout(500);
        await page.waitForLoadState('networkidle');

        // Right-click again to re-activate the menu
        await page.getByRole('cell', { name: 'MyCustomPlugin' }).click({ button: 'right' });
    }
    
    await page.waitForTimeout(500);
    await page.waitForLoadState('networkidle');

    await page.getByRole('button', { name: 'Activate', exact: true }).click();
    await page.getByText('The selected plugin will be activated').waitFor();
    await page.getByRole('button', { name: 'Submit', exact: true }).click();
    await page.waitForLoadState('networkidle');

    await page.waitForTimeout(2500);
});


/**
 * Test for expected data in plugin panels
 */
test('Plugin - Panels', async ({ page }) => {
    await doLogin(page);

    // Navigate to the "Part" page - check for custom panel
    await page.goto(`${BASE_URL}/web/part/50/`);

    // Load the plugin tab
    await page.getByRole('tab', { name: /My Custom Plugin/ }).click();

    // Click the "Increment Counter" button a few times
    for (let i = 0; i < 5; i++) {
        await page.getByText(`Counter: ${i}`).waitFor();
        await page.getByRole('button', { name: 'Increment Counter' }).click();
    }

    // Open a dialog
    await page.getByRole('button', { name: 'Edit Part' }).click();
    await page.getByText('Custom Plugin Form').waitFor();
    await page.getByRole('textbox', { name: 'text-field-name' }).waitFor();
    await page.getByRole('textbox', { name: 'text-field-description' }).waitFor();
    await page.getByRole('button', { name: 'Cancel' }).click();

    // Check for expected text values (translated text should be visible)
    await page.getByText('Translated text, provided by custom code!').waitFor();
    await page.getByText('Translations are loaded automatically').waitFor();

    // Check for custom API query data
    // This is fetched from a custom API endpoint, which should be provided by the plugin code
    await page.getByText('API Query Data').waitFor();
    await page.getByText(/Part Count: \d+/).waitFor();
    await page.getByText(/Today: \d{4}-\d{2}-\d{2}/).waitFor();

    await page.waitForTimeout(2500);
});