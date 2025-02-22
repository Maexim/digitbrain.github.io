<style>
  .md-content__button {
    display: none;
  }
</style>
# Data Fields

**This information is also available in [table format](/tables/data/)**


## Available Fields 

The metadata specification for a DIGITbrain Data
has these sections:

- [Administrative data](#administrative-data)
- [Description](#description)
- [Search support](#search-support)
- [Datakind specification](#datakind-specification)
- [Data access specification](#data-access-specification)
- [Open parameters](#open-parameters)
- [Further access clauses (extensible)](#further-access-clauses-extensible)
- [Data content semantics](#data-content-semantics)


### Administrative data


`ID`{ #id }
:   **Auto-generated**-*id*- Unique identifier of the data resource.

    === "Example"
        ``` yaml     
        UUID
        ```

`AUTHOR`{ #author }
:   **Auto-generated**-*id*- Unique identifier of the user who created this record

    === "Example"
        ``` yaml     
        UUID
        ```

`PROVIDER`{ #provider }
:   **Auto-generated**-*id*- Legal entity who provides the data resource (owner). It is the affiliation of the author by default.

    === "Example"
        ``` yaml     
        UUID
        ```

`DATE`{ #date }
:   **Auto-generated**-*timestamp*- Date of data resource registration.

    === "Example"
        ``` yaml     
        10:45:13 CET 21/03/2021
        ```


### Description


`DATA_NAME`{ #data_name }
:   **Required**-*string*- Name of the data resource. (The directory hierarchy in Nexus provides a fully qualified (FQ) name, which is unique.)

    === "Example"
        ``` yaml     
        CNSPiezoBolt#1 (in directory: factory 1 , machine1 , piezobolts)
        ```

`DATA_VERSION`{ #data_version }
:   **Optional**-*string*- Version of this data resource entry (major.minor.patch). Defaults to 1.0.0
    === "Example"
        ``` yaml     
        2.3.4
        ```

`DATA_DESC`{ #data_desc }
:   **Optional**-*string*- Human readable description of the data resource.
    === "Example"
        ``` yaml     
        This sensor measures temperature in Celsius, sends data via ConSenses edge device via an MQTT broker
        ```

`DATA_DESC_URL`{ #data_desc_url }
:   **Optional**-*URL*- More detailed specification of data source characteristics (doc, pdf, …)
    === "Example"
        ``` yaml     
        data-source-specification-sheet.pdf
        ```

`DATA_SIZE`{ #data_size }
:   **Optional**-*integer*- Estimated/exact size of data (e.g. file size, volume size, or message size); might be used to assess HW requirements (RAM, CPU) . In bytes (k - kilo, m - mega, t - tera, p - peta)
    === "Example"
        ``` yaml     
        112m
        ```


### Search support


`DATA_TAGS`{ #data_tags }
:   **Optional**-*list of strings*- A list of tags freely added to help in searching/indexing (not limited to a basic set of tags, keywords)
    === "Example"
        ``` yaml     
        [camera, rgb, w640, h480, jpg]
        ```


### Datakind specification


`DATA_KIND`{ #data_kind }
:   **Required**-*enum*- Type of the data resource (e.g. file/object storage, database management system, streaming broker). FILE can mean a single file or a folder.

    === "Example"
        ``` yaml     
        FILE , DATABASE , STREAM
        ```

`DATA_DIRECTION`{ #data_direction }
:   **Required**-*enum*- Direction of data flow (source: data provider, sink: data consumer/storage)

    === "Example"
        ``` yaml     
        SOURCE , SINK , BIDIRECTIONAL
        ```

`DATA_FORMAT`{ #data_format }
:   **Optional**-*list of strings*- Format/encoding of the data produced or consumed by the data resource as a MIME type (IETF RFC 6838 https://www.sitepoint.com/mime-types-complete-list/). More than one can appear here (remote directory with several files).
    === "Example"
        ``` yaml     
        [ { application/json , text/plain , application/octet-stream , application/zip } ] 
        ```

`DATA_STORE_TYPE`{ #data_store_type }
:   **Optional**-*string*- The exact type of the data resource. Typically (but not always) corresponds to the scheme part (scheme://) of DATA_URI.
    === "Example"
        ``` yaml     
        S3 , MYSQL , MQTT , ... (WP6: DATA_SOURCE_TYPE=LOCAL, PATH=...")
        ```


### Data access specification


`DATA_URI`{ #data_uri }
:   **Optional**-*URI*- Accessibility of the data resource, including host, port information, protocol, and other fields (path is protocol dependent, can be a topic name). GUI may show host, port, path separately. Hidden at search. Format: scheme://host:port/path.  Pseudo vars: DATA_PROTOCOL, DATA_HOST, DATA_PORT, DATA_PATH, DATA_QUERY, DATA_FRAGMENT.
    === "Example"
        ``` yaml     
        https://amazonaws/bucket/object , kafka://host/topic#1 , ...
        ```

`DATA_AUTH`{ #data_auth }
:   **Optional**-*list of enums*- One or more authentication types that can be accepted by the storage resource.
    === "Example"
        ``` yaml     
        [ { none , userpass , accesskey_secretkey , ssl_certificate , tls_mutual, access_token , rclone_config }+ ]
        ```


### Open parameters


`DATA_CREDENTIALS`{ #data_credentials }
:   **Optional**-*OPEN*- Credentials (e.g. string/json, zip, config file)


### Further access clauses (extensible)


`DATA_AUX_INFO`{ #data_aux_info }
:   **Optional**-*string*- List of key-value pais (JSON object/YAML dictionary) for additional specification of the data resource. New keys can be added on demand, a list of known keys is available.
    === "Example"
        ``` yaml     
        { PROTOCOL: http, MYSQL_DIALECT: mariadbdialect, MQTT_PROTOCOL_VERSION: 3.1.1, KAFKA_BROKER_VERSION: 2.7.0, S3_REGION: eu-central-1 }
        ```


### Data content semantics


`DATA_SCHEMA`{ #data_schema }
:   **Optional**-*string*- Describes message internal structure, semantics, ontology. It can be any file (doc, rdf, owl, etc.). Asset Administration Shell, IEC 61360 - Common Data Dictionary, ...
    === "Example"
        ``` yaml     
        database schema description/contents 
        ```

`DATA_SCHEMA_URL`{ #data_schema_url }
:   **Optional**-*URL*- No description available.
    === "Example"
        ``` yaml     
        database schema URL
        ```
