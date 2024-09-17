// next.config.mjs
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const nextConfig = {
  experimental: {
    appDir: true, // Add this line to enable the experimental app directory
  },
  webpack: (config) => {
    config.resolve.alias = {
      ...config.resolve.alias,
      '@codemirror/state': path.resolve(__dirname, 'node_modules/@codemirror/state')
    };
    return config;
  }
};

export default nextConfig;
