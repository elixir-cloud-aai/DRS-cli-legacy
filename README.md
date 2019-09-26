[![PyPI version](https://badge.fury.io/py/drs-client.svg)](https://badge.fury.io/py/drs-client) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drs_client)
# DRS-cli

This repository contains a [Bravado]-based client for a mockup implementation of
the [Data Repository Service] API schema of the [Global Alliance for Genomics
and Health], as described in the [mock-DRS] repository. The client was developed
for the use within the [TEStribute] task distribution logic application.

## Usage

To use the client import it as follows in your Python code after
[installation](#Installation):

```py
import drs_client

client = drs_client.Client("http://localhost:9101/ga4gh/drs/v1/")
```

It is possible to supply a Bearer token, which will then be added to the
`Authentication` header (prepended by `Bearer`) for every outbound call:

```py
client = tes_client.Client(
   url="https://path.to/swagger.json",
   jwt="SomET0kEn"
)
```

> Note that the indicated URL is valid when [mock-DRS] was installed at the
> default location on your local machine. When a different DRS instance is
> supposed to be used, replace the full URL (including `http://` or `https://`).

Access the [mock-DRS] `GET /objects/{object_id}` endpoint with, e.g.:

```py
response = client.GetObject("a001")
```

Access the [mock-DRS] `POST /update-db` endpoint with, e.g.:

```py
response = client.updateDatabaseObjects(
    clear_db=True,
    objects=[
        {
            "access_methods": [
                {
                    "access_id": "string",
                    "access_url": {"headers": ["Authorization"], "url": "string"},
                    "region": "us-east-1",
                    "type": "s3",
                }
            ],
            "aliases": ["string"],
            "checksums": [{"checksum": "string", "type": "string"}],
            "created": "string",
            "description": "string",
            "id": "string",
            "mime_type": "application/json",
            "name": "string",
            "size": 0,
            "updated": "string",
            "version": "string",
        },
    ],
)
```
the objects list can contain any number of such drs_object dicts and the clear_db
indicates weather or not the db should be emptied before upload of specified 
objects. 

For further details on populating the DRS via the `POST /update-db` endpoint,
please see the documentation in the [mock-DRS] repository.

Note that all other endpoints are currently not implemented.

## Installation

You can install `DRS-cli` in one of two ways:

### Manual installation

```bash
git clone https://github.com/elixir-europe/DRS-cli.git
cd DRS-cli
python setup.py install
```

### Installation via package manager

```bash
pip install -e git+https://github.com/elixir-europe/DRS-cli.git#egg=drs_client
```
or

```bash
pip install drs_client
```

## Contributing

This project is a community effort and lives off your contributions, be it in
the form of bug reports, feature requests, discussions, or fixes and other code
changes. Please read the [contributing guidelines] if you want to contribute.
And please mind the [code of conduct] for all interactions with the community.

## Versioning

Development of the app is currently still in alpha stage, and current versioning
is for internal use only. In the future, we are aiming to adopt [semantic
versioning] that is synchronized to the versioning of [TEStribute] and
[mock-TES] in order to ensure that these apps will be compatible as long as both
their major and minor versions match.

## License

This project is covered by the [Apache License 2.0] also available [shipped
with this repository](LICENSE).

## Contact

Please contact the [project leader](mailto:alexander.kanitz@sib.swiss) for
inquiries, proposals, questions etc. that are not covered by the
[Contributing](#Contributing) section.

## Acknowledgments

The project is a collaborative effort under the umbrella of the [ELIXIR Cloud
and AAI] group. It was started during the [2019 Google Summer of Code] as part
of the [Global Alliance for Genomics and Health] [organization].

![logo banner]

[Apache License 2.0]: <https://www.apache.org/licenses/LICENSE-2.0>
[2019 Google Summer of Code]: <https://summerofcode.withgoogle.com/projects/#6613336345542656>
[Bravado]: <https://github.com/Yelp/bravado>
[contributing guidelines]: CONTRIBUTING.md
[code of conduct]: CODE_OF_CONDUCT.md
[Data Repository Service]: <https://github.com/ga4gh/data-repository-service-schemas>
[ELIXIR Cloud and AAI]: <https://elixir-europe.github.io/cloud/>
[Global Alliance for Genomics and Health]: <https://www.ga4gh.org/>
[logo banner]: logos/logo-banner.svg
[mock-DRS]: <https://github.com/elixir-europe/mock-DRS>
[organization]: <https://summerofcode.withgoogle.com/organizations/6643588285333504/>
[semantic versioning]:https://semver.org/
[TESTribute]:https://github.com/elixir-europe/TEStribute 
