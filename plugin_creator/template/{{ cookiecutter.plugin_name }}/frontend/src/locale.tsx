
import { i18n } from '@lingui/core';
import { Skeleton } from '@mantine/core';
import { useEffect, useState } from 'react';
import { I18nProvider } from '@lingui/react';


/**
 * Attempt to load the locale file for the given locale, returning null if it fails
 */
async function tryLoadLocale(locale: string): Promise<any> {
  try {
    const messages = await import(`./locales/${locale}/messages.ts`);
    return messages;
  } catch (error) {
    console.warn(`Failed to load locale ${locale}`);
    return null;
  }
}


/**
 * Helper function to dynamically load frontend translations,
 * based on the provided locale.
 */
async function loadPluginLocale(locale: string) {

  let messages = null;

  // Find the most specific locale file possible, with fallbacks to less specific locales if necessary
  messages = await tryLoadLocale(locale);

  if (!messages && locale.includes('-')) {
    const fallbackLocale = locale.split('-')[0];
    console.debug(`Locale ${locale} not found, trying fallback locale ${fallbackLocale}`);
    messages = await tryLoadLocale(fallbackLocale);
  }

  if (!messages && locale.includes('_')) {
    const fallbackLocale = locale.split('_')[0];
    console.debug(`Locale ${locale} not found, trying fallback locale ${fallbackLocale}`);
    messages = await tryLoadLocale(fallbackLocale);
  }

  if (!messages && locale !== 'en') {
    console.debug(`Locale ${locale} not found, trying fallback locale en`);
    messages = await tryLoadLocale('en');
  }

  if (messages) {
    i18n.load(locale, messages);
    i18n.activate(locale);
  } else {
    console.error(`Failed to load any locale for ${locale}`);
  }
}


// Wrapper component for loading dynamic translations
export function LocalizedComponent({
    locale,
    children
}: {
    locale: string,
    children: React.ReactNode
}) {

    const [loaded, setLoaded] = useState(false);

    // Reload componentwhen the locale changes
    useEffect(() => {
        setLoaded(false);
        loadPluginLocale(locale).then(() => {
            setLoaded(true);
        });
    }, [locale]);

    if (!loaded) {
        return (
            <Skeleton w='100%' animate />
        );
    }

    return (
        <I18nProvider i18n={i18n}>
            {children}
        </I18nProvider>
    );
}
