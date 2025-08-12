--- 
title: completions
hide_title: false
hide_table_of_contents: false
keywords:
  - completions
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

Creates, updates, deletes, gets or lists a <code>completions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>completions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_inference.completions" /></td></tr>
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
    <td><CopyableCode code="insert" /></td>
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

## `INSERT` examples

<Tabs
    defaultValue="cortex_llm_inference_complete"
    values={[
        { label: 'cortex_llm_inference_complete', value: 'cortex_llm_inference_complete' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="cortex_llm_inference_complete">

Perform LLM text completion inference, similar to snowflake.cortex.Complete.

```sql
INSERT INTO snowflake.cortex_inference.completions (
data__model,
data__messages,
data__temperature,
data__top_p,
data__max_tokens,
data__max_output_tokens,
data__response_format,
data__guardrails,
data__tools,
data__tool_choice,
data__provisioned_throughput_id,
data__sf-ml-xp-inflight-prompt-action,
data__sf-ml-xp-inflight-prompt-client-id,
data__sf-ml-xp-inflight-prompt-public-key,
data__stream,
endpoint
)
SELECT 
'{{ model }}' --required,
'{{ messages }}' --required,
{{ temperature }},
{{ top_p }},
{{ max_tokens }},
{{ max_output_tokens }},
'{{ response_format }}',
'{{ guardrails }}',
'{{ tools }}',
'{{ tool_choice }}',
'{{ provisioned_throughput_id }}',
'{{ sf-ml-xp-inflight-prompt-action }}',
'{{ sf-ml-xp-inflight-prompt-client-id }}',
'{{ sf-ml-xp-inflight-prompt-public-key }}',
{{ stream }},
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: completions
  props:
    - name: endpoint
      value: string
      description: Required parameter for the completions resource.
    - name: model
      value: string
      description: >
        The model name. See documentation for possible values.
        
    - name: messages
      value: array
    - name: temperature
      value: number
      description: >
        Temperature controls the amount of randomness used in response generation. A higher temperature corresponds to more randomness.
        
    - name: top_p
      value: number
      description: >
        Threshold probability for nucleus sampling. A higher top-p value increases the diversity of tokens that the model considers, while a lower value results in more predictable output.
        
      default: 1
    - name: max_tokens
      value: integer
      description: >
        The maximum number of output tokens to produce. The default value is model-dependent.
        
      default: 4096
    - name: max_output_tokens
      value: integer
      description: >
        Deprecated in favor of "max_tokens", which has identical behavior.
        
    - name: response_format
      value: object
      description: >
        An object describing response format config for structured-output mode.
        
    - name: guardrails
      value: object
      description: >
        Guardrails configuration
        
    - name: tools
      value: array
      description: >
        List of tools to be used during tool calling
        
    - name: tool_choice
      value: object
    - name: provisioned_throughput_id
      value: string
      description: >
        The provisioned throughput ID to be used with the request.
        
    - name: sf-ml-xp-inflight-prompt-action
      value: string
      description: >
        Reserved
        
    - name: sf-ml-xp-inflight-prompt-client-id
      value: string
      description: >
        Reserved
        
    - name: sf-ml-xp-inflight-prompt-public-key
      value: string
      description: >
        Reserved
        
    - name: stream
      value: boolean
      description: >
        Reserved
        
      default: true
```
</TabItem>
</Tabs>
