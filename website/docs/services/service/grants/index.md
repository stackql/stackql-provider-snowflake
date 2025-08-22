--- 
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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

Creates, updates, deletes, gets or lists a <code>grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.service.grants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_service_role_grants_to"
    values={[
        { label: 'list_service_role_grants_to', value: 'list_service_role_grants_to' }
    ]}
>
<TabItem value="list_service_role_grants_to">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the securable</td>
</tr>
<tr>
    <td><CopyableCode code="grantee_name" /></td>
    <td><code>string</code></td>
    <td>The name of the grantee</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the grant was created</td>
</tr>
<tr>
    <td><CopyableCode code="granted_on" /></td>
    <td><code>string</code></td>
    <td>The type of of the securable</td>
</tr>
<tr>
    <td><CopyableCode code="granted_to" /></td>
    <td><code>string</code></td>
    <td>The type of the grantee</td>
</tr>
<tr>
    <td><CopyableCode code="privilege" /></td>
    <td><code>string</code></td>
    <td>The name of the privilege</td>
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
    <td><a href="#list_service_role_grants_to"><CopyableCode code="list_service_role_grants_to" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-service"><code>service</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all the grants given to the service role</td>
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
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases.</td>
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
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/&#123;database&#125;/schemas` GET request to get a list of available schemas for the specified database.</td>
</tr>
<tr id="parameter-service">
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>Name of the service that contains the service role.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_service_role_grants_to"
    values={[
        { label: 'list_service_role_grants_to', value: 'list_service_role_grants_to' }
    ]}
>
<TabItem value="list_service_role_grants_to">

List all the grants given to the service role

```sql
SELECT
name,
grantee_name,
created_on,
granted_on,
granted_to,
privilege
FROM snowflake.service.grants
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND service = '{{ service }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>
