import { Alert, Button, Group, Stack, Text, Title } from '@mantine/core';
import { notifications } from '@mantine/notifications';
import { useCallback, useMemo, useState } from 'react';

// Import for type checking
import { checkPluginVersion, type InvenTreePluginContext } from '@inventreedb/ui';
import { ApiEndpoints, apiUrl, ModelType } from '@inventreedb/ui';

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

    const partId = useMemo(() => {
        return context.model == ModelType.part ? context.id || null: null;
    }, [context.model, context.id]);

    // Hello world - counter example
    const [ counter, setCounter ] = useState<number>(0);

    // Extract context information
    const instance: string = useMemo(() => {
        const data = context?.instance ?? {};
        return JSON.stringify(data, null, 2);
    }, [context.instance]);

    // Custom form to edit the selected part
    const editPartForm = context.forms.edit({
        url: apiUrl(ApiEndpoints.part_list, partId),
        title: "Edit Part",
        preFormContent: (
            <Alert title="Custom Plugin Form" color="blue">
                This is a custom form launched from within a plugin!
            </Alert>
        ),
        fields: {
            name: {},
            description: {},
            category: {},
        },
        successMessage: null,
        onFormSuccess: () => {
            notifications.show({
                title: 'Success',
                message: 'Part updated successfully!',
                color: 'green',
            });
        }
    });

    // Custom callback function example
    const openForm = useCallback(() => {
        editPartForm?.open();
    }, [editPartForm]);

    // Navigation functionality example
    const gotoDashboard = useCallback(() => {
        context.navigate('/home');
    }, [context]);

    return (
        <>
        {editPartForm.modal}
        <Stack gap="xs">
        <Title c={context.theme.primaryColor}  order={3}>{{ cookiecutter.plugin_title }}</Title>
        <Text>
            This is a custom panel for the {{ cookiecutter.plugin_name }} plugin.
        </Text>
        <Group justify='apart' wrap='nowrap' gap='sm'>
            <Button color='blue' onClick={gotoDashboard}>
                Go to Dashboard
            </Button>
            {partId && <Button color='green' onClick={openForm}>
                Edit  Part
            </Button>}
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
    checkPluginVersion(context);
    return <{{ cookiecutter.plugin_name }}Panel context={context} />;
}