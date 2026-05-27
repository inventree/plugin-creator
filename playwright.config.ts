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
 */

export default defineConfig({
    testDir: './tests',
    fullyParallel: false,
    timeout: 90000,
    retries: 3,
    workers: 1,
    reporter: 'list',
    projects: [
        {
            'name': 'chromium',
            'use': {
                ...devices['Desktop Chrome']
            }
        }
    ],
    webServer: [
        {
            command: 'invoke dev.server -a 0.0.0.0:8000',
            env: {
                INVENTREE_DEBUG: 'True',
                INVENTREE_LOG_LEVEL: 'WARNING',
                INVENTREE_PLUGINS_ENABLED: 'True',
                INVENTREE_SITE_URL: 'http://localhost:8000',
                INVENTREE_FRONTEND_API_HOST: 'http://localhost:8000',
                INVENTREE_CORS_ORIGIN_ALLOW_ALL: 'True',
                INVENTREE_COOKIE_SAMESITE: 'False',
                INVENTREE_LOGIN_ATTEMPTS: '100',
                INVENTREE_PLUGINS_MANDATORY: 'my-custom-plugin'
            },
            url: 'http://localhost:8000/api/',
            stdout: 'pipe',
            stderr: 'pipe',
            timeout: 120 * 1000
        }
    ],
    use: {
        baseUrl: 'http://localhost:8000',
        trace: 'on',
    }
});