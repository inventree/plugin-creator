import { Stack, Text, Title } from '@mantine/core';
import { useMemo } from 'react';

/**
 * Render a custom panel with the provided context.
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function {{ cookiecutter.plugin_name }}Panel({
    context
}: {
    context: any;
}) {

    // Extract context information
    const instance: string = useMemo(() => {
        let data = context?.instance ?? {};
        return JSON.stringify(data, null, 2);
    }, [context.instance]);

    return (
        <>
        <Stack gap="xs">
        <Title order={3}>{{ cookiecutter.plugin_title }}</Title>
        <Text>
            This is a custom panel for the {{ cookiecutter.plugin_name }} plugin.
        </Text>
        <Title order={5}>Instance Data</Title>
        <div>
            {instance}
        </div>
        </Stack>
        </>
    );
}


/**
 * Render the {{ cookiecutter.plugin_name }}Panel component.
 * 
 * @param context - The context object to pass to the panel
 */
export function render{{ cookiecutter.plugin_name }}Panel(context: any) {
    return <{{ cookiecutter.plugin_name }}Panel context={context} />;
}
