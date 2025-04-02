
import { SimpleGrid, Text } from '@mantine/core';

/**
 * Render a custom dashboard item with the provided context
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function {{ cookiecutter.plugin_name }}DashboardItem({
    context
}: {
    context: any;
}) {

    // Render a simple grid of data
    return (
        <SimpleGrid cols={2} spacing="md">
            <Text>Hello world</Text>
            <Text>
                Username: {context.user?.username?.()}
            </Text>
        </SimpleGrid>
    );
}


/**
 * Render the {{ cookiecutter.plugin_name }}DashboardItem component.
 * 
 * @param context - The context object to pass to the panel
 */
export function render{{ cookiecutter.plugin_name }}DashboardItem(context: any) {
    return <{{ cookiecutter.plugin_name }}DashboardItem context={context} />;
}
