"""
Payment Studio
Generation Builder Test
"""

from App.Core.Generation.json_builder import JsonBuilder


def test_generation_builder():

    xml = """
<Document>
    <GrpHdr>
        <MsgId>MSG000001</MsgId>
        <CreDtTm>2026-08-05T10:00:00</CreDtTm>
    </GrpHdr>
</Document>
"""

    json = JsonBuilder().build(
        xml,
    )

    assert json is not None
    assert '"Document"' in json
