--- 
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
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

Creates, updates, deletes, gets or lists a <code>logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.service.logs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="fetch_service_logs"
    values={[
        { label: 'fetch_service_logs', value: 'fetch_service_logs' }
    ]}
>
<TabItem value="fetch_service_logs">

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
    <td><CopyableCode code="system$get_service_logs" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#fetch_service_logs"><CopyableCode code="fetch_service_logs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instanceId"><code>instanceId</code></a>, <a href="#parameter-containerName"><code>containerName</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-numLines"><code>numLines</code></a></td>
    <td>Fetch the logs for a given service.</td>
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
<tr id="parameter-containerName">
    <td><CopyableCode code="containerName" /></td>
    <td><code>string</code></td>
    <td>Container name as specified in the service specification file.</td>
</tr>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-instanceId">
    <td><CopyableCode code="instanceId" /></td>
    <td><code>integer</code></td>
    <td>ID of the service instance, starting with 0.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/&#123;database&#125;/schemas` GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-numLines">
    <td><CopyableCode code="numLines" /></td>
    <td><code>integer</code></td>
    <td>Number of trailing log lines to retrieve.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="fetch_service_logs"
    values={[
        { label: 'fetch_service_logs', value: 'fetch_service_logs' }
    ]}
>
<TabItem value="fetch_service_logs">

Fetch the logs for a given service.

```sql
SELECT
system$get_service_logs
FROM snowflake.service.logs
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND instanceId = '{{ instanceId }}' -- required
AND containerName = '{{ containerName }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND numLines = '{{ numLines }}';
```
</TabItem>
</Tabs>
