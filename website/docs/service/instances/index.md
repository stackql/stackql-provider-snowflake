--- 
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - service
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

Creates, updates, deletes, gets or lists an <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.service.instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_service_instances"
    values={[
        { label: 'list_service_instances', value: 'list_service_instances' }
    ]}
>
<TabItem value="list_service_instances">

successful

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
    <td><CopyableCode code="instance_id" /></td>
    <td><code>string</code></td>
    <td>ID of the service instance (this is the index of the service instance starting from 0).</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="creation_time" /></td>
    <td><code>string</code></td>
    <td>The time when Snowflake started creating the service instance.</td>
</tr>
<tr>
    <td><CopyableCode code="service_status" /></td>
    <td><code>string</code></td>
    <td>The current status of the service.</td>
</tr>
<tr>
    <td><CopyableCode code="spec_digest" /></td>
    <td><code>string</code></td>
    <td>The unique and immutable identifier that represents the service specification content.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string</code></td>
    <td>The time when Snowflake acknowledged the service instance is running on a node.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the service instance.</td>
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
    <td><a href="#list_service_instances"><CopyableCode code="list_service_instances" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all the instances of the service</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_service_instances"
    values={[
        { label: 'list_service_instances', value: 'list_service_instances' }
    ]}
>
<TabItem value="list_service_instances">

List all the instances of the service

```sql
SELECT
instance_id,
database_name,
schema_name,
service_name,
creation_time,
service_status,
spec_digest,
start_time,
status
FROM snowflake.service.instances
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>
