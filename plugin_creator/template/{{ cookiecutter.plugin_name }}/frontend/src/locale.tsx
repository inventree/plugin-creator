
import { i18n } from '@lingui/core';
import { Skeleton } from '@mantine/core';
import { useEffect, useState } from 'react';
import { I18nProvider } from '@lingui/react';


/**
 * Helper function to dynamically load frontend translations,
 * based on the provided locale.
 */
async function loadPluginLocale(locale: string) {
    const { messages } = await import(`./locales/${locale}/messages.ts`);
    
    i18n.load(locale, messages);
    i18n.activate(locale);
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
