--- 
title: search_services
hide_title: false
hide_table_of_contents: false
keywords:
  - search_services
  - cortex_search_service
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>search_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>search_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_search_service.search_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_cortex_search_services"
    values={[
        { label: 'list_cortex_search_services', value: 'list_cortex_search_services' },
        { label: 'fetch_cortex_search_service', value: 'fetch_cortex_search_service' },
        { label: 'query_cortex_search_service', value: 'query_cortex_search_service' }
    ]}
>
<TabItem value="list_cortex_search_services">

A Snowflake cortex search service object.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name for the cortex search service, must be unique for the schema in which the cortex search service is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the cortex search service is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the cortex search service is stored</td>
</tr>
<tr>
    <td><CopyableCode code="attribute_columns" /></td>
    <td><code>array</code></td>
    <td>Specifies the attribute columns, which can be referenced in filters in search queries to the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>Specifies all columns included in the cortex search service and that can be returned in search queries.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the cortex search service</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the cortex search service was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time as of which data existent in base tables is now serving.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>string</code></td>
    <td>Specifies the definition (source query) used to create the cortex search service (example: SELECT col1, col2 FROM foo)</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_error" /></td>
    <td><code>string</code></td>
    <td>Error encountered during the latest indexing pipeline of the cortex search service, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="search_column" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the search column for the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="serving_data_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Size of the serving index, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="serving_state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source_data_num_rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the materialized source data feeding into the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="target_lag" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically refreshing the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the warehouse that provides the compute resources for refreshing the cortex search service (example: test_wh)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_cortex_search_service">

A Snowflake cortex search service object.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the name for the cortex search service, must be unique for the schema in which the cortex search service is created</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the cortex search service is stored</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the cortex search service is stored</td>
</tr>
<tr>
    <td><CopyableCode code="attribute_columns" /></td>
    <td><code>array</code></td>
    <td>Specifies the attribute columns, which can be referenced in filters in search queries to the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>Specifies all columns included in the cortex search service and that can be returned in search queries.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the cortex search service</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the cortex search service was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time as of which data existent in base tables is now serving.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>string</code></td>
    <td>Specifies the definition (source query) used to create the cortex search service (example: SELECT col1, col2 FROM foo)</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_error" /></td>
    <td><code>string</code></td>
    <td>Error encountered during the latest indexing pipeline of the cortex search service, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="search_column" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the search column for the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="serving_data_bytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>Size of the serving index, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="serving_state" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source_data_num_rows" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of rows in the materialized source data feeding into the cortex search service.</td>
</tr>
<tr>
    <td><CopyableCode code="target_lag" /></td>
    <td><code>object</code></td>
    <td>Specifies the schedule for periodically refreshing the dynamic table.</td>
</tr>
<tr>
    <td><CopyableCode code="warehouse" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the warehouse that provides the compute resources for refreshing the cortex search service (example: test_wh)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="query_cortex_search_service">

Search results.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td>ID of the request.</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>array</code></td>
    <td>List of result rows.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list_cortex_search_services"><CopyableCode code="list_cortex_search_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-fromName"><code>fromName</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a></td>
    <td>Lists the cortex search services under the database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_cortex_search_service"><CopyableCode code="fetch_cortex_search_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a Cortex Search Service.</td>
</tr>
<tr>
    <td><a href="#query_cortex_search_service"><CopyableCode code="query_cortex_search_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Query a Cortex Search Service to get search results.</td>
</tr>
<tr>
    <td><a href="#create_cortex_search_service"><CopyableCode code="create_cortex_search_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a cortex search service, with standard create modifiers as query parameters. See the Cortex Search Service component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#delete_cortex_search_service"><CopyableCode code="delete_cortex_search_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a cortex search service with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#suspend_cortex_search_service"><CopyableCode code="suspend_cortex_search_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td>Suspends one or both of the indexing or serving targets of a cortex search service.</td>
</tr>
<tr>
    <td><a href="#resume_cortex_search_service"><CopyableCode code="resume_cortex_search_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a>, <a href="#parameter-target"><code>target</code></a></td>
    <td>Resume the cortex search service</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the <code>/api/v2/databases</code> GET request to get a list of available databases.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the <code>/api/v2/databases/&#123;database&#125;/schemas</code> GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Cortex Search Service.</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
<tr id="parameter-target">
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>Query parameter that identifies the target to which suspension or resumption of the cortex search service should be applied.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_cortex_search_services"
    values={[
        { label: 'list_cortex_search_services', value: 'list_cortex_search_services' },
        { label: 'fetch_cortex_search_service', value: 'fetch_cortex_search_service' },
        { label: 'query_cortex_search_service', value: 'query_cortex_search_service' }
    ]}
>
<TabItem value="list_cortex_search_services">

Lists the cortex search services under the database and schema.

```sql
SELECT
name,
database_name,
schema_name,
attribute_columns,
columns,
comment,
created_on,
data_timestamp,
definition,
indexing_error,
indexing_state,
search_column,
serving_data_bytes,
serving_state,
source_data_num_rows,
target_lag,
warehouse
FROM snowflake.cortex_search_service.search_services
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND fromName = '{{ fromName }}'
AND showLimit = '{{ showLimit }}';
```
</TabItem>
<TabItem value="fetch_cortex_search_service">

Fetch a Cortex Search Service.

```sql
SELECT
name,
database_name,
schema_name,
attribute_columns,
columns,
comment,
created_on,
data_timestamp,
definition,
indexing_error,
indexing_state,
search_column,
serving_data_bytes,
serving_state,
source_data_num_rows,
target_lag,
warehouse
FROM snowflake.cortex_search_service.search_services
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
<TabItem value="query_cortex_search_service">

Query a Cortex Search Service to get search results.

```sql
SELECT
request_id,
results
FROM snowflake.cortex_search_service.search_services
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_cortex_search_service"
    values={[
        { label: 'create_cortex_search_service', value: 'create_cortex_search_service' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_cortex_search_service">

Create a cortex search service, with standard create modifiers as query parameters. See the Cortex Search Service component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.cortex_search_service.search_services (
data__name,
data__search_column,
data__columns,
data__attribute_columns,
data__target_lag,
data__warehouse,
data__definition,
data__comment,
data__indexing_state,
data__serving_state,
database_name,
schema_name,
endpoint,
createMode
)
SELECT 
'{{ name }}' --required,
'{{ search_column }}' --required,
'{{ columns }}',
'{{ attribute_columns }}',
'{{ target_lag }}' --required,
'{{ warehouse }}' --required,
'{{ definition }}' --required,
'{{ comment }}',
'{{ indexing_state }}',
'{{ serving_state }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: search_services
  props:
    - name: database_name
      value: string
      description: Required parameter for the search_services resource.
    - name: schema_name
      value: string
      description: Required parameter for the search_services resource.
    - name: endpoint
      value: string
      description: Required parameter for the search_services resource.
    - name: name
      value: string
      description: >
        Specifies the name for the cortex search service, must be unique for the schema in which the cortex search service is created
        
    - name: search_column
      value: string
      description: >
        Specifies the name of the search column for the cortex search service.
        
    - name: columns
      value: array
      description: >
        Specifies all columns included in the cortex search service and that can be returned in search queries.
        
    - name: attribute_columns
      value: array
      description: >
        Specifies the attribute columns, which can be referenced in filters in search queries to the cortex search service.
        
    - name: target_lag
      value: object
      description: >
        Specifies the schedule for periodically refreshing the dynamic table.
        
    - name: warehouse
      value: string
      description: >
        Specifies the name of the warehouse that provides the compute resources for refreshing the cortex search service
        
    - name: definition
      value: string
      description: >
        Specifies the definition (source query) used to create the cortex search service
        
    - name: comment
      value: string
      description: >
        Specifies a comment for the cortex search service
        
    - name: indexing_state
      value: string
      valid_values: ['ACTIVE', 'SUSPENDED', 'INITIALIZING']
    - name: serving_state
      value: string
      valid_values: ['ACTIVE', 'SUSPENDED', 'INITIALIZING']
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_cortex_search_service"
    values={[
        { label: 'delete_cortex_search_service', value: 'delete_cortex_search_service' }
    ]}
>
<TabItem value="delete_cortex_search_service">

Delete a cortex search service with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

```sql
DELETE FROM snowflake.cortex_search_service.search_services
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="suspend_cortex_search_service"
    values={[
        { label: 'suspend_cortex_search_service', value: 'suspend_cortex_search_service' },
        { label: 'resume_cortex_search_service', value: 'resume_cortex_search_service' }
    ]}
>
<TabItem value="suspend_cortex_search_service">

Suspends one or both of the indexing or serving targets of a cortex search service.

```sql
EXEC snowflake.cortex_search_service.search_services.suspend_cortex_search_service 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@target='{{ target }}';
```
</TabItem>
<TabItem value="resume_cortex_search_service">

Resume the cortex search service

```sql
EXEC snowflake.cortex_search_service.search_services.resume_cortex_search_service 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@target='{{ target }}';
```
</TabItem>
</Tabs>
