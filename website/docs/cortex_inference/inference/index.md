--- 
title: inference
hide_title: false
hide_table_of_contents: false
keywords:
  - inference
  - cortex_inference
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

Creates, updates, deletes, gets or lists an <code>inference</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_inference.inference" /></td></tr>
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
    <td><a href="#cortex_llm_inference_complete"><CopyableCode code="cortex_llm_inference_complete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Perform LLM text completion inference, similar to snowflake.cortex.Complete.</td>
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
    defaultValue="cortex_llm_inference_complete"
    values={[
        { label: 'cortex_llm_inference_complete', value: 'cortex_llm_inference_complete' }
    ]}
>
<TabItem value="cortex_llm_inference_complete">

Perform LLM text completion inference, similar to snowflake.cortex.Complete.

```sql
EXEC snowflake.cortex_inference.inference.cortex_llm_inference_complete 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"model": "{{ model }}", 
"messages": "{{ messages }}", 
"temperature": {{ temperature }}, 
"top_p": {{ top_p }}, 
"max_tokens": {{ max_tokens }}, 
"max_output_tokens": {{ max_output_tokens }}, 
"response_format": "{{ response_format }}", 
"guardrails": "{{ guardrails }}", 
"tools": "{{ tools }}", 
"tool_choice": "{{ tool_choice }}", 
"provisioned_throughput_id": "{{ provisioned_throughput_id }}", 
"sf-ml-xp-inflight-prompt-action": "{{ sf-ml-xp-inflight-prompt-action }}", 
"sf-ml-xp-inflight-prompt-client-id": "{{ sf-ml-xp-inflight-prompt-client-id }}", 
"sf-ml-xp-inflight-prompt-public-key": "{{ sf-ml-xp-inflight-prompt-public-key }}", 
"stream": {{ stream }}
}';
```
</TabItem>
</Tabs>
