
// Import for type checking
import { type InvenTreePluginContext } from '@inventreedb/ui';

/**
 * Custom spotlight action with the provided context
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
export function {{ cookiecutter.plugin_name }}SpotlightAction({
    context
}: {
    context: InvenTreePluginContext;
}) {

    // Simply display an alert when the action is executed
    // Replace this with any custom action
    alert(`Hello, ${context.user?.username?.()}`);
}
