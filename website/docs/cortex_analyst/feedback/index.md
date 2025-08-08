--- 
title: feedback
hide_title: false
hide_table_of_contents: false
keywords:
  - feedback
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

Creates, updates, deletes, gets or lists a <code>feedback</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feedback</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.cortex_analyst.feedback" /></td></tr>
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
    <td><a href="#send_feedback"><CopyableCode code="send_feedback" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Send a user feedback of Cortex Analyst response</td>
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
    defaultValue="send_feedback"
    values={[
        { label: 'send_feedback', value: 'send_feedback' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="send_feedback">

Send a user feedback of Cortex Analyst response

```sql
INSERT INTO snowflake.cortex_analyst.feedback (
data__request_id,
data__positive,
data__feedback_message,
endpoint
)
SELECT 
'{{ request_id }}' --required,
{{ positive }} --required,
'{{ feedback_message }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: feedback
  props:
    - name: endpoint
      value: string
      description: Required parameter for the feedback resource.
    - name: request_id
      value: string
      description: >
        Request id associated with the feedback
        
    - name: positive
      value: boolean
      description: >
        Whether the response was good (true) or bad (false)
        
    - name: feedback_message
      value: string
      description: >
        The text for the detailed feedback message
        
```
</TabItem>
</Tabs>
