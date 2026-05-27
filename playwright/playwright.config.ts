import { defineConfig, devices } from '@playwright/test';

/**
 * Run a playwright integration test suite for the plugin creator.
 * 
 * Workflow:
 * 
 * 1. Install InvenTree into the local environment
 * 2. Run data migrations, ensure InvenTree install is up to date
 * 3. Install demo dataset, so we have some data to work with
 * 4. Use the plugin-creator tool to create a new default plugin
 * 5. Build and install the plugin into the local python environment
 * 6. Run the playwright tests to ensure the plugin is working correctly
 * 
 * By the time we launch playwright, we assume that the InvenTree server is up!
 */

export default defineConfig({
    testDir: './tests',
    fullyParallel: false,
    timeout: 10000,
    retries: 0,
    workers: 1,
    reporter: [['html', { open: 'never' }], ['github']],
    projects: [
        {
            'name': 'chromium',
            'use': {
                ...devices['Desktop Chrome']
            }
        }
    ],
    use: {
        baseUrl: 'http://localhost:8000',
        trace: 'on',
    }
});