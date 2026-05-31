// Primary vite config - we extend this for dev mode
import { defineConfig, Plugin } from 'vite'
import { viteExternalsPlugin } from 'vite-plugin-externals'
import viteConfig, { externalLibs } from './vite.config'

{% if cookiecutter.frontend.translation -%}
import react from "@vitejs/plugin-react-swc"
import { lingui } from "@lingui/vite-plugin"
{%- endif %}

function inventreeHmrPlugin(): Plugin {
  const fileRegex = /\.(js|jsx|ts|tsx)(\?|$)/;

  const hmrBlock = [
    '',
    '// __inventree_hmr_injected__',
    'if (import.meta.hot) {',
    '  import.meta.hot.accept((newModule) => {',
    '    window.__plugin_hmr_reload?.(newModule);',
    '  })',
    '}',
  ];

  return {
    name: 'inventree-hmr-plugin',

    transform(code, id) {
      if (!fileRegex.test(id)) return;
      if (id.includes("node_modules")) return;
      if (code.includes("__inventree_hmr_injected__")) return;

      return code + hmrBlock.join('\n');
    }
  }
}

/**
 * Vite config to run the frontend plugin in development mode.
 * 
 * This allows the plugin developer to "live reload" their plugin code,
 * without having to rebuild and reinstall the plugin each time.
 * 
 * This is a very minimal config, and is not meant to be used for production builds.
 * Refer to vite.config.ts for the production build config.
 */
export default defineConfig((cfg) => {

  const config = {
    ...viteConfig,
    resolve: {},
    server: {
      port: 5174,  // Default port for plugins
      strictPort: true,
      cors: {   
        preflightContinue: true,
        origin: '*',  // Allow all origins for development
      }
    },
  };
  
  // Override specific options for development
  delete config.esbuild;
  delete config.optimizeDeps;

  config.plugins = [
    {% if cookiecutter.frontend.translation -%}
    lingui(),
    react({
      plugins: [["@lingui/swc-plugin", {}]],
      reactRefreshHost: 'http://localhost:5173',
    }),
    {%- endif %}
    viteExternalsPlugin(externalLibs),
    inventreeHmrPlugin(),
  ];

  return config;
});
