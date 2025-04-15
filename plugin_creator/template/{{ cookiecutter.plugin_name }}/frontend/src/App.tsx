import { Anchor, Code, Divider, Highlight, Paper, SimpleGrid, Stack, Text } from '@mantine/core';


const DOCS_URL : string = "https://docs.inventree.org/en/latest/extend/plugins/ui/";


// This is a test page for the {{ cookiecutter.plugin_name }} plugin.
// This page is *not* part of the plugin itself, but is used to test the plugin.
export default function App() {

  return (
    <>
    <Paper p='md' m='lg' shadow='md' withBorder>
      <SimpleGrid cols={3}>
        <Paper p='md' m='md' withBorder>
        <Stack>
      <Text size="lg" c='blue' >
        {{ cookiecutter.plugin_name }}
      </Text>
      <Divider />
      <Highlight highlight={['{{ cookiecutter.plugin_slug }}']}>
        This is a test page for the {{ cookiecutter.plugin_slug }} plugin. 
      </Highlight>
        </Stack>
        </Paper>
        <Paper p='md' m='md' withBorder>
        <Stack>
          <Text size='lg' c='blue'>Building</Text>
          <Divider />
          <Text>To build the plugin code, run:</Text>
          <Code>npm run build</Code>
        </Stack>
        </Paper>
        <Paper p='md' m='md' withBorder>
        <Stack>
          <Text size='lg' c='blue'>Developer Documentation</Text>
          <Divider />
          <Text>Read the plugin developer documentation:</Text>
          <Anchor href={DOCS_URL} target="_blank" rel="noopener noreferrer">
            {DOCS_URL}
          </Anchor>
        </Stack>
        </Paper>
      </SimpleGrid>
    </Paper>
    </>
  );
}
