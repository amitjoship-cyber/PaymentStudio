"""
Project Prism
Generation Statistics
"""


class GenerationStatistics:

    def __init__(self):

        self.nodes_created = 0

        self.populated_elements = 0

        self.empty_elements = 0

        self.optional_generated = 0

        self.optional_skipped = 0

        self.choice_selected = 0

        self.choice_skipped = 0

        self.generation_time = 0

    # --------------------------------------------------

    def finish(
        self,
        elapsed_ms,
    ):

        self.generation_time = elapsed_ms
