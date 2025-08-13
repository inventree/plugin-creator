import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { viteExternalsPlugin } from 'vite-plugin-externals'
{% if cookiecutter.frontend.translation -%}
import { lingui } from "@lingui/vite-plugin";
{%- endif %}


/**
 * The following libraries are externalized to avoid bundling them with the plugin.
 * These libraries are expected to be provided by the InvenTree core application.
 */
export const externalLibs : Record<string, string> = {
  react: 'React',
  'react-dom': 'ReactDOM',
  'ReactDom': 'ReactDOM',
  '@lingui/core': 'LinguiCore',
  '@lingui/react': 'LinguiReact',
  '@mantine/core': 'MantineCore',
  "@mantine/notifications": 'MantineNotifications',
};

// Just the keys of the externalLibs object
const externalKeys = Object.keys(externalLibs);

/**
 * Vite config to build the frontend plugin as an exported module.
 * This will be distributed in the 'static' directory of the plugin.
 */
export default defineConfig({
  plugins: [
    {% if cookiecutter.frontend.translation -%}
    lingui(),
    {%- endif %}
    react({
      jsxRuntime: 'classic',
      {% if cookiecutter.frontend.translation -%}
      babel: {
        plugins: ['macros'], // Required for @lingui macros
      },
      {%- endif %}
    }),
    viteExternalsPlugin(externalLibs),
  ],
  esbuild: {
    jsx: 'preserve',
  },
  build: {
    // minify: false,
    target: 'esnext',
    cssCodeSplit: false,
    manifest: true,
    sourcemap: true,
    rollupOptions: {
      preserveEntrySignatures: "exports-only",
      input: [
        {% if cookiecutter.frontend.features.panel -%}
        './src/Panel.tsx',
        {%- endif %}
        {% if cookiecutter.frontend.features.dashboard -%}
        './src/Dashboard.tsx',
        {%- endif %}
        {% if cookiecutter.frontend.features.settings -%}
        './src/Settings.tsx',
        {%- endif %}
      ],
      output: {
        dir: '../{{ cookiecutter.package_name }}/static',
        entryFileNames: '[name].js',
        assetFileNames: 'assets/[name].[ext]',
        globals: externalLibs,
      },
      external: externalKeys,
    }
  },
  optimizeDeps: {
    exclude: externalKeys,
  }
})
