"""
Payment Studio
Generation Builder
"""

from App.Core.Generation.xml_generator import XMLGenerator

from App.Core.Generation.generation_result import (
    GenerationResult,
)

from App.Core.Generation.json_builder import (
    JsonBuilder,
)


class GenerationBuilder:

    def __init__(
        self,
        xml_builder,
    ):

        self.xml_builder = xml_builder
        self.json_builder = JsonBuilder()

    # --------------------------------------------------

    def build(
        self,
        complex_type_name,
        context,
    ):

        #
        # XML Tree
        #

        root = self.xml_builder.build_component_message(
            complex_type_name,
            context,
        )

        if root is None:

            return None

        #
        # XML Text
        #

        xml = XMLGenerator.generate(
            root,
        )

        #
        # JSON
        #

        json = self.json_builder.build(
            xml,
        )

        #
        # Result
        #

        result = GenerationResult()

        result.root = root
        result.xml = xml
        result.json = json

        return result

    def build_message(
        self,
        message,
        context,
    ):

        root = self.xml_builder.build_message(
            message,
            context,
        )

        if root is None:

            return None

        xml = XMLGenerator.generate(
            root,
        )

        json = self.json_builder.build(
            xml,
        )

        result = GenerationResult()

        result.root = root
        result.xml = xml
        result.json = json

        return result
