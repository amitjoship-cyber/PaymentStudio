from App.Core.Generation.generation_context import GenerationContext
from App.Core.Generation.generation_options import GenerationOptions

context = GenerationContext(
    country="IN",
    message_name="pacs.008.001.14",
    options=GenerationOptions(),
)

print("Country :", context.country)

print("Message :", context.message_name)

print("Output  :", context.options.output_format)

print("Sample  :", context.options.sample_mode)
