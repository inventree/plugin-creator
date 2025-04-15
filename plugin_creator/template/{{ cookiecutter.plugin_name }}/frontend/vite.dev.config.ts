import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

/**
 * Vite config to run the frontend plugin in development mode.
 * 
 * This is a very minimal config, and is not meant to be used for production builds.
 * Refer to vite.config.ts for the production build config.
 */
export default defineConfig({
  plugins: [
    react(),
  ],
  build: {
    cssCodeSplit: false,
    manifest: true,
    sourcemap: true,
  },
})
