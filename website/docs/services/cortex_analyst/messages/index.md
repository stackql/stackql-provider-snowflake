--- 
title: messages
hide_title: false
hide_table_of_contents: false
keywords:
  - messages
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

Creates, updates, deletes, gets or lists a <code>messages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_analyst.messages" /></td></tr>
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
    <td><a href="#send_message"><CopyableCode code="send_message" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Send a data question to the Cortex Analyst</td>
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

## `INSERT` examples

<Tabs
    defaultValue="send_message"
    values={[
        { label: 'send_message', value: 'send_message' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="send_message">

Send a data question to the Cortex Analyst

```sql
INSERT INTO snowflake.cortex_analyst.messages (
data__semantic_model_file,
data__semantic_model,
data__semantic_view,
data__semantic_models,
data__stream,
data__operation,
data__warehouse,
data__messages,
data__source,
data__experimental,
endpoint
)
SELECT 
'{{ semantic_model_file }}',
'{{ semantic_model }}',
'{{ semantic_view }}',
'{{ semantic_models }}',
{{ stream }},
'{{ operation }}',
'{{ warehouse }}',
'{{ messages }}' --required,
'{{ source }}',
'{{ experimental }}',
'{{ endpoint }}'
RETURNING
request_id,
message,
response_metadata,
semantic_model_selection,
warnings
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: messages
  props:
    - name: endpoint
      value: string
      description: Required parameter for the messages resource.
    - name: semantic_model_file
      value: string
      description: >
        The path to a file stored in a Snowflake Stage holding the semantic model yaml. Must be a fully qualified stage url
        
    - name: semantic_model
      value: string
      description: >
        A string containing the entire semantic model yaml
        
    - name: semantic_view
      value: string
      description: >
        The name of the Snowflake native semantic model object
        
    - name: semantic_models
      value: array
      description: >
        A list of semantic model objects. If set, other semantic model properties are ignored
        
    - name: stream
      value: boolean
      description: >
        Whether to stream the response or not
        
      default: false
    - name: operation
      value: string
      description: >
        Whether to response with SQL or natural language. One of 'sql_generation' or 'answer_generation'
        
      valid_values: ['sql_generation', 'answer_generation']
      default: sql_generation
    - name: warehouse
      value: string
      description: >
        Warehouse name to use for result set handling. Only used when 'operation' is 'answer_generation'
        
    - name: messages
      value: array
    - name: source
      value: string
      description: >
        an optional field to specify the source of the request. e.g "eval", "prod"
        
    - name: experimental
      value: string
      description: >
        JSON serialized string of experimental API fields (undocumented).
        
```
</TabItem>
</Tabs>
