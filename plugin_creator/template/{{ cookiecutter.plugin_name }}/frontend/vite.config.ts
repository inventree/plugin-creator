import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

/**
 * Vite config to build the frontend plugin as an exported module.
 * This will be distributed in the 'static' directory of the plugin.
 */

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    cssCodeSplit: false,
    manifest: false,
    rollupOptions: {
      preserveEntrySignatures: "exports-only",
      input: [
        {% if cookiecutter.frontend.features.panel -%}
        './src/Panel.tsx',
        {%- endif %}
        {% if cookiecutter.frontend.features.dashboard -%}
        './src/Dashboard.tsx',
        {%- endif %}
      ],
      output: {
        dir: '../{{ cookiecutter.package_name }}/static',
        entryFileNames: '[name].js',
        assetFileNames: 'assets/[name].[ext]',
      },
    }
  }
})
