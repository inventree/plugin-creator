"""API serializers for the {{ cookiecutter.plugin_name }} plugin.

In practice, you would define your custom serializers here.

Ref: https://www.django-rest-framework.org/api-guide/serializers/
"""

from rest_framework import serializers


class ExampleSerializer(serializers.Serializer):
    """Example serializer for the {{ cookiecutter.plugin_name }} plugin.
    
    This simply demonstrates how to create a serializer,
    with a few example fields of different types.
    """

    class Meta:
        """Meta options for this serializer."""
        fields = [
            'random_text',
            'part_count',
            'today',
        ]
    
    random_text = serializers.CharField(
        max_length=100,
        required=True,
        label="Random Text",
        help_text="A text field containing randomly generated data."
    )

    part_count = serializers.IntegerField(
        label="Number of Parts",
        help_text="Total number of parts in the InvenTree database.",
    )

    today = serializers.DateField(
        required=False,
        label="Today",
        help_text="The current date.",
    )
