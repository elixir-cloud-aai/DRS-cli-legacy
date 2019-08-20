# DRS-cli
This repository contains a [Bravado]-based client for a [modified] version of
the [Data Repository Service] API schema of the [Global Alliance for Genomics and
Health], as described in the [mock-DRS] repository. The client was developed for
the use within the [TEStribute] task distribution logic application.

# Usage

To use the client import it as follows in your Python code after
[installation](#Installation):

```py
from drs_client import Client
client = Client.Client("http://localhost:9101/ga4gh/drs/v1/")
```
> Note that the indicated URL is valid when [mock-DRS] was installed at the
> default location on your local machine. When a different DRS instance is
> supposed to be used, replace the full URL (including `http://` or `https://`.

Access the [mock-DRS] `GET /objects/{object_id}` endpoint with, e.g.:

```py
response = client.GetObject("object_id")
```

Access the [mock-DRS] `/update-db` endpoint with, e.g.:

```py
response = client.UpdateTaskInfoConfig(
    clear="True",
    objects=["objet_id1","object_id2"],
)
```
for details on the population of the mock-DRS please view the [mock-DRS] repository.
all other endpoints still remain unimplemented.

# Installation

You can install the ```DRS-cli``` in one of two ways

## Manual Installation

Clone repository
```bash
git clone https://github.com/elixir-europe/DRS-cli.git
```

Traverse project repository & setup
```bash
cd DRS-cli
python DRS-cli/setup.py install
```

Installation using a package manager

```bash
pip install -e git+https://github.com/elixir-europe/DRS-cli.git
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

This project is covered by the [Apache License 2.0] also available [shippied
with this repository](LICENSE).

## Contact

Please contact the [project leader](mailto:alexander.kanitz@sib.swiss) for
inquiries, proposals, questions etc. that are not covered by the
[Contributing](CONTRIBUTING.md) section.

## Acknowledgments

The project is a collaborative effort under the umbrella of the [ELIXIR Cloud
and AAI] group. It was started during the [2019 Google Summer of Code] as part
of the [Global Alliance for Genomics and Health][organization].

![logo banner]

[Apache License 2.0]:https://www.apache.org/licenses/LICENSE-2.0
[bravado]:https://github.com/Yelp/bravado
[contributing guidelines]: CONTRIBUTING.md
[code of conduct]: CODE_OF_CONDUCT.md
[Data Repository Service]:https://github.com/ga4gh/data-repository-service-schemas
[ELIXIR Cloud and AAI]: <https://elixir-europe.github.io/cloud/>
[Global Alliance for Genomics and Health]: <https://www.ga4gh.org/>
[2019 Google Summer of Code]: <https://summerofcode.withgoogle.com/projects/#6613336345542656>
[logo banner]: logos/logo-banner.svg
[mock-DRS]:https://github.com/elixir-europe/mock-DRS
[Open API specification]:https://github.com/elixir-europe/mock-DRS/blob/master/mock_drs/specs/schema.data_repository_service.cd0186f.openapi.modified.yaml
[organization]: <https://summerofcode.withgoogle.com/organizations/6643588285333504/>
[semantic versioning]:https://semver.org/
[TESTribute]:https://github.com/elixir-europe/TEStribute 
