# [NS API](https://www.ns.nl/en/travel-information/ns-api)

[![PyPI](https://img.shields.io/pypi/v/ns-api.svg)](https://pypi.org/project/ns-api/)

Unofficial wrapper for the Dutch railway [API](https://www.ns.nl/en/travel-information/ns-api) (Nederlandse Spoorwegen). The NS API currently features the following services:

- Prices
- Current departure times
- Disruptions and engineering work
- The station list, with all stations in the Netherlands including Geodata
- Travel recommendations from station to station

```python
from nsapi import NSAPI

ns = NSAPI('yourkey')
ns.get_all_stations()
```

```python
from nsapi import AsyncNSAPI

async def example():
    async with AsyncNSAPI('yourkey') as ns:
        await ns.get_all_stations()
```

## License

Licensed under the [MIT License](LICENSE).
