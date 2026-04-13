import { useCallback, useEffect, useMemo, useState } from 'react';
import { Accordion, Alert, Button, Group, SimpleGrid, Stack, Text, Title } from '@mantine/core';
import { notifications } from '@mantine/notifications';
{% if "UrlsMixin" in cookiecutter.plugin_mixins.mixin_list -%}
import { useQuery } from '@tanstack/react-query';
{%- endif %}

{% if cookiecutter.frontend.translation -%}
import { t } from '@lingui/core/macro';
import { LocalizedComponent } from './locale';
{%- endif %}

// Import for type checking
import { checkPluginVersion, type InvenTreePluginContext } from '@inventreedb/ui';
import { ApiEndpoints, apiUrl, ModelType } from '@inventreedb/ui';

// Import table display function
import { InvenTreeTable, useTable, RowEditAction } from '@inventreedb/ui';

/**
 * Render a custom panel with the provided context.
 * Refer to the InvenTree documentation for the context interface
 * https://docs.inventree.org/en/latest/plugins/mixins/ui/#plugin-context
 */
function {{ cookiecutter.plugin_name }}Panel({
    context
}: {
    context: InvenTreePluginContext;
}) {

    // React hooks can be used within plugin components
    useEffect(() => {
        console.log("useEffect in plugin component:");
        console.log("- Model:", context.model);
        console.log("- ID:", context.id);
    }, [context.model, context.id]);

    // Memoize the part ID as passed via the context object
    const partId = useMemo(() => {
        return context.model == ModelType.part ? context.id || null: null;
    }, [context.model, context.id]);

    // Does this InvenTree version support tables in plugins?
    const supportsTables = useMemo(() => !!context.tables, [context.tables]);

    // State management for the API driven table
    const tableState = useTable('my-custom-table');

    // Custom table properties for the loaded table
    const tableProps = {
        enableSelection: true,
        enablePagination: true,
        enableRefresh: true,
        modelType: ModelType.part,
        params: {
            active: true
        },
        tableFilters: [
            {
                name: 'assembly',
                label: 'Assembly',
                description: 'Show assembly parts',
                type: 'boolean',
            }
        ],
        rowActions: (record: any) => [
            RowEditAction({
                onClick: () => {
                    notifications.show({
                        title: 'Row Action Clicked',
                        message: `You clicked the edit action for ${record.name}`,
                        color: 'blue',
                    });
                }
            })
        ]
    };

    // Hello world - counter example
    const [ counter, setCounter ] = useState<number>(0);

    // Extract context information
    const instance: string = useMemo(() => {
        const data = context?.instance ?? {};
        return JSON.stringify(data, null, 2);
    }, [context.instance]);

    {% if "UrlsMixin" in cookiecutter.plugin_mixins.mixin_list -%}
    // Fetch API data from the example API endpoint
    // It will re-fetch when the partId changes
    const apiQuery = useQuery(
        {
            queryKey: ['apiData', partId],
            queryFn: async() => {
                const url = `/plugin/{{ cookiecutter.plugin_slug }}/example/`;

                return context.api.get(url).then((response) => response.data).catch(() => {});
            }
        },
        context.queryClient,
    );
    {%- endif %}

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
        <Accordion defaultValue='main'>
        <Accordion.Item value='main'>
            <Accordion.Control>
                <Title c={context.theme.primaryColor}  order={4}>{{ cookiecutter.plugin_title }}</Title>
            </Accordion.Control>
        <Accordion.Panel>
            <SimpleGrid cols={2}>
                {% if cookiecutter.frontend.translation -%}
                <Alert title='Translated Text' color='grape'>
                    <Stack gap='xs'>
                        <Text>{t`Translated text, provided by custom code!`}</Text>
                        <Text>{t`Translations are loaded automatically.`}</Text>
                        <Text>{t`Fallback locale is used if no translation is available`}</Text>
                    </Stack>
                </Alert>
                {%- endif %}
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
                {% if "UrlsMixin" in cookiecutter.plugin_mixins.mixin_list -%}
                {apiQuery.isFetched && apiQuery.data && (
                <Alert color="green" title="API Query Data">
                        {apiQuery.isFetching || apiQuery.isLoading ? (
                        <Text>Loading...</Text>
                        ) : (
                        <Stack gap='xs'>
                            <Text>Part Count: {apiQuery.data.part_count}</Text>
                            <Text>Today: {apiQuery.data.today}</Text>
                            <Text>Random Text: {apiQuery.data.random_text}</Text>
                            <Button
                                disabled={apiQuery.isFetching || apiQuery.isLoading}
                                onClick={() => apiQuery.refetch()}>
                                Reload Data
                            </Button>
                        </Stack>
                    )}
                </Alert>
                )}{%- endif %}
            </SimpleGrid>
        </Accordion.Panel>
        </Accordion.Item>
        <Accordion.Item value='table'>
            <Accordion.Control>
                <Title c={context.theme.primaryColor}  order={4}>Custom Table Example</Title>
            </Accordion.Control>
        <Accordion.Panel>
        {
            supportsTables ? (
                <InvenTreeTable
                    url={apiUrl(ApiEndpoints.part_list)}
                    tableState={tableState}
                    context={context}
                    props={tableProps}
                    columns={[
                        {
                            accessor: 'name',
                            switchable: false,
                        },
                        {
                            accessor: 'IPN',
                        },
                        {
                            accessor: 'description',
                        }
                    ]}
                />
            ) : (
                <Alert title="Table Not Supported" color="red">
                    {
                        'This version of InvenTree does not support tables within plugins.'
                    }
                    <br />
                    {
                        'Please upgrade to a more recent version of InvenTree to use this feature.'
                    }
                </Alert>
            )
        }
        </Accordion.Panel>
        </Accordion.Item>
        </Accordion>
        </>
    );
}


// This is the function which is called by InvenTree to render the actual panel component
export function render{{ cookiecutter.plugin_name }}Panel(context: InvenTreePluginContext) {
    checkPluginVersion(context);

    {% if cookiecutter.frontend.translation -%}
    return (
        <LocalizedComponent locale={context.locale}>
            <{{ cookiecutter.plugin_name }}Panel context={context} />
        </LocalizedComponent>
    );
    {%- else -%}
    return (
        <{{ cookiecutter.plugin_name }}Panel context={context} />
    );
    {%- endif %}
}
