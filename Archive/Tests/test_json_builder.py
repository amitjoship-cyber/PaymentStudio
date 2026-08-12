"""
Payment Studio
JSON Builder Test
"""

from App.Core.Generation.json_builder import (
    JsonBuilder,
)


def test_json_builder():

    xml = """
<Document>
    <GrpHdr>
        <MsgId>MSG000001</MsgId>
        <CreDtTm>2026-08-05T10:00:00</CreDtTm>
    </GrpHdr>
</Document>
"""

    builder = JsonBuilder()

    result = builder.build(
        xml,
    )

    print(result)

    assert '"Document"' in result
    assert '"GrpHdr"' in result
    assert '"MsgId"' in result
    assert '"MSG000001"' in result
