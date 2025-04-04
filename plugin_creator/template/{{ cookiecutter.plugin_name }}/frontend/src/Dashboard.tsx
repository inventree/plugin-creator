
import { Button, SimpleGrid, Text } from '@mantine/core';
import { useState } from 'react';

// Import for type checking
import { checkPluginVersion, type InvenTreePluginContext } from '@inventreedb/ui';

/**
 * Render a custom dashboard item with the provided context
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function {{ cookiecutter.plugin_name }}DashboardItem({
    context
}: {
    context: InvenTreePluginContext;
}) {

    const [ counter, setCounter ] = useState<number>(0);

    const pluginName : string = "{{ cookiecutter.plugin_name }}";

    // Render a simple grid of data
    return (
        <SimpleGrid cols={2} spacing="md">
            <Text>Plugin: {pluginName}</Text>
            <Text>
                Username: {context.user?.username?.()}
            </Text>
            <Text>
                Counter: {counter}
            </Text>
            <Button onClick={() => setCounter(counter + 1)}>+</Button>
        </SimpleGrid>
    );
}


// This is the function which is called by InvenTree to render the actual dashboard
//  component
export function render{{ cookiecutter.plugin_name }}DashboardItem(context: InvenTreePluginContext) {
    checkPluginVersion(context);
    return <{{ cookiecutter.plugin_name }}DashboardItem context={context} />;
}
