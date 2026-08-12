from App.Core.Repository.repository_service import RepositoryService
from App.Core.XSD.xsd_loader import XSDLoader


def test_xsd_element_context():

    repository = RepositoryService()

    xsd_file = repository.latest_xsd("pain.001")

    assert xsd_file is not None

    loader = XSDLoader()

    schema = loader.load(xsd_file.path)

    assert schema.root_element != ""

    print("\nRoot Element:", schema.root_element)

    count = 0

    for complex_type in schema.complex_types:

        for element in complex_type.elements:

            print(
                element.name,
                "->",
                element.type_name,
            )

            count += 1

            if count > 10:
                return
