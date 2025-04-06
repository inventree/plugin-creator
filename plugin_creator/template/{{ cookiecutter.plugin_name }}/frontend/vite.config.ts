import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { viteExternalsPlugin } from 'vite-plugin-externals'

/**
 * Vite config to build the frontend plugin as an exported module.
 * This will be distributed in the 'static' directory of the plugin.
 */
export default defineConfig({
  plugins: [
    react({
      jsxRuntime: 'classic'
    }),
    viteExternalsPlugin({
      react: 'React',
      'react-dom': 'ReactDOM',
      '@mantine/core': 'MantineCore',
      "@mantine/notifications": 'MantineNotifications',
    }),
  ],
  esbuild: {
    jsx: 'preserve',
  },
  build: {
    // minify: false,
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
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
          '@mantine/core': 'MantineCore',
          "@mantine/notifications": 'MantineNotifications',
        },
      },
      external: ['react', 'react-dom', '@mantine/core', '@mantine/notifications'],
    }
  },
  optimizeDeps: {
    exclude: ['react', 'react-dom', '@mantine/core', '@mantine/notifications'],
  },
})
