<style>
  .md-content__button {
    display: none;
  }
</style>
# DMA Tuple Fields

**This information is also available in [table format](/tables/dma_tuple/)**


## Available Fields 

The metadata specification for a DIGITbrain DMA Tuple
has these sections:

- [Definition](#definition)
- [Data Assets Mapping](#data-assets-mapping)
- [Deployments](#deployments)


### Definition


`ID`{ #id }
:   **Auto-generated**-*ID / URI*- Unique identifier for the DMA Tuple

    === "Example"
        ``` yaml     
        123e4567-e89b-12d3-a456-426614174000
        ```

`Created at`{ #created-at }
:   **Auto-generated**-*ISO 8601*- Date of creation

    === "Example"
        ``` yaml     
        2021-05-01T00:00:00Z
        ```

`Version`{ #version }
:   **Optional**-*Integer*- Version number of the DMA Tuple
    === "Example"
        ``` yaml     
        21
        ```

`Author`{ #author }
:   **Auto-generated**-*ID / URI*- Identifier of the Author of the MA Pair (NB: Entity for author is referenced)

    === "Example"
        ``` yaml     
        person_123e4567-e89b-12d3 (auto)
        ```

`Licensor`{ #licensor }
:   **Auto-generated**-*ID / URI*- Identifier of the Legal Entity licensing the the MA Pair (NB: Entity for Licensor is referenced)

    === "Example"
        ``` yaml     
        legal_entity_123e4567-e89b-12d3 (auto)
        ```

`Derivation`{ #derivation }
:   **Auto-generated**-*IDs / URIs*- In case of derivation, references to parent / child (optional)

    === "Example"
        ``` yaml     
        dma_tuple_123e4567-e89b-12d3 (auto)
        ```

`Name`{ #name }
:   **Required**-*Text*- Short name to identify the DMA Tuple

    === "Example"
        ``` yaml     
        Pressure drop for the injection in hall 3
        ```

`Scope`{ #scope }
:   **Required**-*Text*- Short description of the scope of the DMA Tuple (human readable)

    === "Example"
        ``` yaml     
        Effectiveness of the mold closing process
        ```

`IP Instance`{ #ip-instance }
:   **Required**-*ID / URI*- Identifier of the IP Instance the DMA Tuple is valid for (NB: Entity for IP Instance is referenced)

    === "Example"
        ``` yaml     
        ip_instance_123e4567-e89b-12d3
        ```

`Namespace`{ #namespace }
:   **Optional**-*ID / URI?*- Context to interpret the associated information (optional?)
    === "Example"
        ``` yaml     
        namespace_123e4567-e89b-12d3
        ```

`MA Pair`{ #ma-pair }
:   **Required**-*ID / URI*- Identifier of the MA Pair associated to the DMA Tuple

    === "Example"
        ``` yaml     
        ma_pair_123e4567-e89b-12d3
        ```

`Schedule`{ #schedule }
:   **Optional**-*Dates*- Days and hours the DMA Tuple will be active (optional)
    === "Example"
        ``` yaml     
        R90/2021-05-01T00:00:00Z/PT48H
        ```

`Payload`{ #payload }
:   **Optional**-*String*- User-defined key-value pairs: JSON string with additional information (optional)
    === "Example"
        ``` yaml     
        {‘injectionMold’: ‘Circuit Case’}
        ```


### Data Assets Mapping


`DataAssetsMapping`{ #dataassetsmapping }
:   **Required**-*[DataAssetsMapping](../dataassetsmapping.md)*- Mapping required Data assets to Microservices specified in the MA Pair. Not every Microservice needs a Data asset.



### Deployments


`Deployments`{ #deployments }
:   **Required**-*[Deployment](../deployment.md)*- Characteristics of the Deployment (i.e. Cloud or Edge infrastructure) for every Microservice associated to the DMA Tuple

