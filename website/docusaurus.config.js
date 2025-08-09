// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// Provider configuration - change these for different providers
const providerName = "snowflake";
const providerTitle = "Snowflake";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: `StackQL ${providerTitle} Provider`,
  tagline: `Query and Provision ${providerTitle} Resources using StackQL`,
  favicon: 'img/favicon.ico',
  staticDirectories: ['static'],
  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: `https://${providerName}-provider.stackql.io`,
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'stackql', // Usually your GitHub org/user name.
  projectName: `stackql-provider-${providerName}`, // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl: 'https://github.com/stackql/stackql-deploy/tree/main/website/',
          routeBasePath: '/', // Set the docs to be the root of the site
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/stackql-cover.png',
      navbar: {
        logo: {
          alt: 'StackQL Registry',
          href: '/',
          src: 'img/stackql-registry-logo.svg',
          srcDark: 'img/stackql-registry-logo-white.svg',
        },
        items: [
          {
            to: '/stackqldocs',
            position: 'left',
            label: 'StackQL Docs',
          },
          {
            to: '/deploy',
            position: 'left',
            label: 'stackql-deploy',
          },
          {
            to: '/registry',
            type: 'dropdown',
            label: 'StackQL Providers',
            position: 'left',
            items: [
              {
                label: 'AWS',
                to: '/registry/aws',
              },
              {
                label: 'Azure',
                to: '/registry/azure',
              },
              {
                label: 'Google',
                to: '/registry/google',
              },
              {
                label: 'GitHub',
                to: '/registry/github',
              },
              {
                label: 'Kubernetes',
                to: '/registry/k8s',
              },
              {
                label: 'Okta',
                to: '/registry/okta',
              },
              {
                label: 'DigitalOcean',
                to: '/registry/digitalocean',
              },
              {
                label: 'Linode',
                to: '/registry/linode',
              },
              {
                label: '... More',
                to: '/registry',
              },                                                                                                
            ]                      
          },
          {
            to: '/downloads',
            position: 'left',
            label: 'Downloads',
          },
          {
            href: 'https://github.com/stackql/stackql',
            position: 'right',
            className: 'header-github-link',
            'aria-label': 'GitHub repository',
          },          
        ],
      },
      footer: {
        style: 'dark',
        logo: {
          alt: 'StackQL',
          href: 'https://stackql.io/',
          src: 'img/stackql-registry-logo.svg',
          srcDark: 'img/stackql-registry-logo-white.svg',
        },
        links: [
          {
            title: 'StackQL',
            items: [
              {
                label: 'Home',
                to: '/home',
              },
              {
                label: 'Features',
                to: '/features',
              },
              {
                label: 'Downloads',
                to: '/downloads',
              },
              {
                label: 'Contact us',
                href: '/contact-us',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'StackQL Docs',
                to: '/stackqldocs',
              },
              {
                label: 'Providers',
                to: '/registry',
              },
              {
                label: 'Blog',
                to: '/blog',
              },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} StackQL Studios`,
      },
      colorMode: {
        // using user system preferences, instead of the hardcoded defaultMode
        respectPrefersColorScheme: true,
      },
      prism: {
        theme: prismThemes.nightOwl,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
