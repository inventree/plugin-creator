
import { i18n } from '@lingui/core';


/**
 * Helper function to dynamically load frontend translations,
 * based on the provided locale.
 */
export default async function loadPluginLocale(locale: string) {
    const { messages } = await import(`./locales/${locale}/messages.ts`);
    
    i18n.load(locale, messages);
    i18n.activate(locale);
}
