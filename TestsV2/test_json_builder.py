"""
Payment Studio
JSON Builder Unit Test

Isolated from PaymentStudio/RepositoryService on purpose: it needs
no real XSD bundle, so it runs anywhere and actually exercises the
namespace-stripping and attribute-preservation behaviour, unlike
test_json_generation.py's loose substring check.
"""

import json

from App.Core.Generation.json_builder import JsonBuilder


SAMPLE_XML = """<?xml version="1.0"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08">
  <FIToFICstmrCdtTrf>
    <GrpHdr>
      <MsgId>MSG12345</MsgId>
      <NbOfTxs>1</NbOfTxs>
    </GrpHdr>
    <CdtTrfTxInf>
      <IntrBkSttlmAmt Ccy="INR">1000.50</IntrBkSttlmAmt>
      <ChrgsInf>
        <Amt Ccy="INR">10.00</Amt>
      </ChrgsInf>
      <ChrgsInf>
        <Amt Ccy="INR">5.00</Amt>
      </ChrgsInf>
    </CdtTrfTxInf>
  </FIToFICstmrCdtTrf>
</Document>"""


def test_json_builder_strips_namespace_from_keys():

    data = json.loads(JsonBuilder().build(SAMPLE_XML))

    #
    # Bug found in audit: raw ElementTree tags leak the full
    # namespace URI, e.g. "{urn:iso:...}MsgId" instead of "MsgId".
    #

    assert "Document" in data
    assert "urn:iso" not in json.dumps(data)

    grp_hdr = data["Document"]["FIToFICstmrCdtTrf"]["GrpHdr"]

    assert grp_hdr["MsgId"] == "MSG12345"


def test_json_builder_preserves_attributes():

    data = json.loads(JsonBuilder().build(SAMPLE_XML))

    #
    # Bug found in audit: element.attrib was never read, so the
    # Ccy currency code on amount elements silently disappeared.
    #

    tx = data["Document"]["FIToFICstmrCdtTrf"]["CdtTrfTxInf"]

    amount = tx["IntrBkSttlmAmt"]

    assert amount["@Ccy"] == "INR"
    assert amount["#text"] == "1000.50"


def test_json_builder_handles_repeated_elements_with_attributes():

    data = json.loads(JsonBuilder().build(SAMPLE_XML))

    charges = data["Document"]["FIToFICstmrCdtTrf"]["CdtTrfTxInf"]["ChrgsInf"]

    assert isinstance(charges, list)
    assert len(charges) == 2
    assert charges[0]["Amt"]["@Ccy"] == "INR"
    assert charges[0]["Amt"]["#text"] == "10.00"
    assert charges[1]["Amt"]["#text"] == "5.00"
