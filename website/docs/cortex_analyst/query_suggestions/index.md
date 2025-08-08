--- 
title: query_suggestions
hide_title: false
hide_table_of_contents: false
keywords:
  - query_suggestions
  - cortex_analyst
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

Creates, updates, deletes, gets or lists a <code>query_suggestions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_suggestions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_analyst.query_suggestions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#generate_verified_query_suggestions"><CopyableCode code="generate_verified_query_suggestions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Generate VQ suggestions for a semantic model</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate_verified_query_suggestions"
    values={[
        { label: 'generate_verified_query_suggestions', value: 'generate_verified_query_suggestions' }
    ]}
>
<TabItem value="generate_verified_query_suggestions">

Generate VQ suggestions for a semantic model

```sql
EXEC snowflake.cortex_analyst.query_suggestions.generate_verified_query_suggestions 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"semantic_model": "{{ semantic_model }}", 
"warehouse": "{{ warehouse }}", 
"experimental": "{{ experimental }}"
}';
```
</TabItem>
</Tabs>
