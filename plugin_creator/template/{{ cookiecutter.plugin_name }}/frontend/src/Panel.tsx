import { Alert, Button, Group, Stack, Text, Title } from '@mantine/core';
import { useCallback, useMemo, useState } from 'react';

// Import for type checking
import { type InvenTreePluginContext } from 'inventree';
import { ApiEndpoints, apiUrl } from 'inventree';

/**
 * Render a custom panel with the provided context.
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/stable/extend/plugins/ui/#plugin-context
 */
function {{ cookiecutter.plugin_name }}Panel({
    context
}: {
    context: InvenTreePluginContext;
}) {

    // Hello world - counter example
    const [ counter, setCounter ] = useState<number>(0);

    // Extract context information
    const instance: string = useMemo(() => {
        const data = context?.instance ?? {};
        return JSON.stringify(data, null, 2);
    }, [context.instance]);

    // Custom form to create a new part
    const newPartForm = context.forms.create({
        url: apiUrl(ApiEndpoints.part_list),
        title: "New Part",
        preFormContent: (
            <Alert title="Custom Plugin Form" color="blue">
                This is a custom form launched from within a plugin!
            </Alert>
        ),
        fields: {
            name: {},
            description: {},
            category: {},
        }
    });

    // Custom callback function example
    const openForm = useCallback(() => {
        newPartForm?.open();
    }, [newPartForm]);

    return (
        <>
        {newPartForm.modal}
        <Stack gap="xs">
        <Title order={3}>{{ cookiecutter.plugin_title }}</Title>
        <Text>
            This is a custom panel for the {{ cookiecutter.plugin_name }} plugin.
        </Text>
        <Group justify='apart' wrap='nowrap' gap='sm'>
            <Button color='green' onClick={openForm}>
                Create New Part
            </Button>
            <Button onClick={() => setCounter(counter + 1)}>
                Increment Counter
            </Button>
            <Text size='xl'>Counter: {counter}</Text>
        </Group>
        {instance ? (
            <Alert title="Instance Data" color="blue">
                {instance}
            </Alert>
        ) : (
            <Alert title="No Instance" color="yellow">
                No instance data available
            </Alert>
        )}
        </Stack>
        </>
    );
}

// This is the function which is called by InvenTree to render the actual panel component
export function render{{ cookiecutter.plugin_name }}Panel(context: InvenTreePluginContext) {
    return <{{ cookiecutter.plugin_name }}Panel context={context} />;
}