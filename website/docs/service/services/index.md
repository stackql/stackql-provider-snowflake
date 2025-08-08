--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.service.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_services"
    values={[
        { label: 'list_services', value: 'list_services' },
        { label: 'fetch_service', value: 'fetch_service' }
    ]}
>
<TabItem value="list_services">

A Snowflake service object.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_name" /></td>
    <td><code>string</code></td>
    <td>Snowflake-assiged DNS name of the service. The DNS name enables service-to-service communications.</td>
</tr>
<tr>
    <td><CopyableCode code="managing_object_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managing object (for example, the name of the notebook that manages the service). NULL if the service is not managed by a Snowflake entity.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to automatically resume a service when a service function or ingress is called.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend_secs" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of seconds of inactivity after which the service will be automatically suspended. The default value is 0 which represents the service will not be automatically suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the service.</td>
</tr>
<tr>
    <td><CopyableCode code="compute_pool" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the compute pool in your account on which to run the service.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was created.</td>
</tr>
<tr>
    <td><CopyableCode code="current_instances" /></td>
    <td><code>integer</code></td>
    <td>The current number of instances for the service.</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_integrations" /></td>
    <td><code>array</code></td>
    <td>Specifies the names of the external access integrations that allow your service to access external sites.</td>
</tr>
<tr>
    <td><CopyableCode code="is_async_job" /></td>
    <td><code>boolean</code></td>
    <td>True if the service is an async job service; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_job" /></td>
    <td><code>boolean</code></td>
    <td>True if the service is a job service; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_upgrading" /></td>
    <td><code>boolean</code></td>
    <td>TRUE, if Snowflake is in the process of upgrading the service.</td>
</tr>
<tr>
    <td><CopyableCode code="managing_object_domain" /></td>
    <td><code>string</code></td>
    <td>The domain of the managing object (for example, the domain of the notebook that manages the service). NULL if the service is not managed by a Snowflake entity.</td>
</tr>
<tr>
    <td><CopyableCode code="max_instances" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of service instances to run.</td>
</tr>
<tr>
    <td><CopyableCode code="min_instances" /></td>
    <td><code>integer</code></td>
    <td>Specifies the minimum number of service instances to run.</td>
</tr>
<tr>
    <td><CopyableCode code="min_ready_instances" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of ready service instances to declare the service as READY.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the service.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The role type of the service owner.</td>
</tr>
<tr>
    <td><CopyableCode code="query_warehouse" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last resumed.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td>Specifies service specification.</td>
</tr>
<tr>
    <td><CopyableCode code="spec_digest" /></td>
    <td><code>string</code></td>
    <td>The unique and immutable identifier representing the service spec content.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the service.</td>
</tr>
<tr>
    <td><CopyableCode code="suspended_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="target_instances" /></td>
    <td><code>integer</code></td>
    <td>The target number of service instances that should be running as determined by Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_service">

A Snowflake service object.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_name" /></td>
    <td><code>string</code></td>
    <td>Snowflake-assiged DNS name of the service. The DNS name enables service-to-service communications.</td>
</tr>
<tr>
    <td><CopyableCode code="managing_object_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managing object (for example, the name of the notebook that manages the service). NULL if the service is not managed by a Snowflake entity.</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_resume" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether to automatically resume a service when a service function or ingress is called.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_suspend_secs" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of seconds of inactivity after which the service will be automatically suspended. The default value is 0 which represents the service will not be automatically suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Specifies a comment for the service.</td>
</tr>
<tr>
    <td><CopyableCode code="compute_pool" /></td>
    <td><code>string</code></td>
    <td>Specifies the name of the compute pool in your account on which to run the service.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was created.</td>
</tr>
<tr>
    <td><CopyableCode code="current_instances" /></td>
    <td><code>integer</code></td>
    <td>The current number of instances for the service.</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_integrations" /></td>
    <td><code>array</code></td>
    <td>Specifies the names of the external access integrations that allow your service to access external sites.</td>
</tr>
<tr>
    <td><CopyableCode code="is_async_job" /></td>
    <td><code>boolean</code></td>
    <td>True if the service is an async job service; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_job" /></td>
    <td><code>boolean</code></td>
    <td>True if the service is a job service; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="is_upgrading" /></td>
    <td><code>boolean</code></td>
    <td>TRUE, if Snowflake is in the process of upgrading the service.</td>
</tr>
<tr>
    <td><CopyableCode code="managing_object_domain" /></td>
    <td><code>string</code></td>
    <td>The domain of the managing object (for example, the domain of the notebook that manages the service). NULL if the service is not managed by a Snowflake entity.</td>
</tr>
<tr>
    <td><CopyableCode code="max_instances" /></td>
    <td><code>integer</code></td>
    <td>Specifies the maximum number of service instances to run.</td>
</tr>
<tr>
    <td><CopyableCode code="min_instances" /></td>
    <td><code>integer</code></td>
    <td>Specifies the minimum number of service instances to run.</td>
</tr>
<tr>
    <td><CopyableCode code="min_ready_instances" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of ready service instances to declare the service as READY.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the service.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The role type of the service owner.</td>
</tr>
<tr>
    <td><CopyableCode code="query_warehouse" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="resumed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last resumed.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td>Specifies service specification.</td>
</tr>
<tr>
    <td><CopyableCode code="spec_digest" /></td>
    <td><code>string</code></td>
    <td>The unique and immutable identifier representing the service spec content.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the service.</td>
</tr>
<tr>
    <td><CopyableCode code="suspended_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last suspended.</td>
</tr>
<tr>
    <td><CopyableCode code="target_instances" /></td>
    <td><code>integer</code></td>
    <td>The target number of service instances that should be running as determined by Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the service was last updated.</td>
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
    <td><a href="#list_services"><CopyableCode code="list_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-startsWith"><code>startsWith</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a>, <a href="#parameter-fromName"><code>fromName</code></a></td>
    <td>Lists the services under the database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_service"><CopyableCode code="fetch_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch a service.</td>
</tr>
<tr>
    <td><a href="#create_service"><CopyableCode code="create_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a service, with standard create modifiers as query parameters. See the Service component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#create_or_alter_service"><CopyableCode code="create_or_alter_service" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a (or alter an existing) service. Even if the operation is just an alter, the full property set must be provided.</td>
</tr>
<tr>
    <td><a href="#delete_service"><CopyableCode code="delete_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a service with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#execute_job_service"><CopyableCode code="execute_job_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create and execute a job service. See the JobService component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#resume_service"><CopyableCode code="resume_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Resume a service.</td>
</tr>
<tr>
    <td><a href="#suspend_service"><CopyableCode code="suspend_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Suspend a service.</td>
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
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
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
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_services"
    values={[
        { label: 'list_services', value: 'list_services' },
        { label: 'fetch_service', value: 'fetch_service' }
    ]}
>
<TabItem value="list_services">

Lists the services under the database and schema.

```sql
SELECT
name,
database_name,
dns_name,
managing_object_name,
schema_name,
auto_resume,
auto_suspend_secs,
comment,
compute_pool,
created_on,
current_instances,
external_access_integrations,
is_async_job,
is_job,
is_upgrading,
managing_object_domain,
max_instances,
min_instances,
min_ready_instances,
owner,
owner_role_type,
query_warehouse,
resumed_on,
spec,
spec_digest,
status,
suspended_on,
target_instances,
updated_on
FROM snowflake.service.services
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
<TabItem value="fetch_service">

Fetch a service.

```sql
SELECT
name,
database_name,
dns_name,
managing_object_name,
schema_name,
auto_resume,
auto_suspend_secs,
comment,
compute_pool,
created_on,
current_instances,
external_access_integrations,
is_async_job,
is_job,
is_upgrading,
managing_object_domain,
max_instances,
min_instances,
min_ready_instances,
owner,
owner_role_type,
query_warehouse,
resumed_on,
spec,
spec_digest,
status,
suspended_on,
target_instances,
updated_on
FROM snowflake.service.services
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_service"
    values={[
        { label: 'create_service', value: 'create_service' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_service">

Create a service, with standard create modifiers as query parameters. See the Service component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.service.services (
data__name,
data__status,
data__compute_pool,
data__spec,
data__external_access_integrations,
data__query_warehouse,
data__comment,
data__is_async_job,
data__auto_resume,
data__min_ready_instances,
data__min_instances,
data__max_instances,
data__database_name,
data__schema_name,
data__auto_suspend_secs,
database_name,
schema_name,
endpoint,
createMode
)
SELECT 
'{{ name }}' --required,
'{{ status }}',
'{{ compute_pool }}' --required,
'{{ spec }}' --required,
'{{ external_access_integrations }}',
'{{ query_warehouse }}',
'{{ comment }}',
{{ is_async_job }},
{{ auto_resume }},
{{ min_ready_instances }},
{{ min_instances }},
{{ max_instances }},
'{{ database_name }}',
'{{ schema_name }}',
{{ auto_suspend_secs }},
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
- name: services
  props:
    - name: database_name
      value: string
      description: Required parameter for the services resource.
    - name: schema_name
      value: string
      description: Required parameter for the services resource.
    - name: endpoint
      value: string
      description: Required parameter for the services resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.
        
    - name: status
      value: string
      description: >
        The current status of the service.
        
    - name: compute_pool
      value: string
      description: >
        Specifies the name of the compute pool in your account on which to run the service.
        
    - name: spec
      value: object
      description: >
        Specifies service specification.
        
    - name: external_access_integrations
      value: array
      description: >
        Specifies the names of the external access integrations that allow your service to access external sites.
        
    - name: query_warehouse
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.
        
    - name: comment
      value: string
      description: >
        Specifies a comment for the service.
        
    - name: is_async_job
      value: boolean
      description: >
        True if the service is an async job service; false otherwise.
        
    - name: auto_resume
      value: boolean
      description: >
        Specifies whether to automatically resume a service when a service function or ingress is called.
        
    - name: min_ready_instances
      value: integer
      description: >
        The minimum number of ready service instances to declare the service as READY.
        
    - name: min_instances
      value: integer
      description: >
        Specifies the minimum number of service instances to run.
        
    - name: max_instances
      value: integer
      description: >
        Specifies the maximum number of service instances to run.
        
    - name: database_name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.
        
    - name: schema_name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.
        
    - name: auto_suspend_secs
      value: integer
      description: >
        Number of seconds of inactivity after which the service will be automatically suspended. The default value is 0 which represents the service will not be automatically suspended.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_service"
    values={[
        { label: 'create_or_alter_service', value: 'create_or_alter_service' }
    ]}
>
<TabItem value="create_or_alter_service">

Create a (or alter an existing) service. Even if the operation is just an alter, the full property set must be provided.

```sql
REPLACE snowflake.service.services
SET 
data__name = '{{ name }}',
data__status = '{{ status }}',
data__compute_pool = '{{ compute_pool }}',
data__spec = '{{ spec }}',
data__external_access_integrations = '{{ external_access_integrations }}',
data__query_warehouse = '{{ query_warehouse }}',
data__comment = '{{ comment }}',
data__is_async_job = {{ is_async_job }},
data__auto_resume = {{ auto_resume }},
data__min_ready_instances = {{ min_ready_instances }},
data__min_instances = {{ min_instances }},
data__max_instances = {{ max_instances }},
data__database_name = '{{ database_name }}',
data__schema_name = '{{ schema_name }}',
data__auto_suspend_secs = {{ auto_suspend_secs }}
WHERE 
database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required
AND data__compute_pool = '{{ compute_pool }}' --required
AND data__spec = '{{ spec }}' --required
RETURNING
status;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_service"
    values={[
        { label: 'delete_service', value: 'delete_service' }
    ]}
>
<TabItem value="delete_service">

Delete a service with the given name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful.

```sql
DELETE FROM snowflake.service.services
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
    defaultValue="execute_job_service"
    values={[
        { label: 'execute_job_service', value: 'execute_job_service' },
        { label: 'resume_service', value: 'resume_service' },
        { label: 'suspend_service', value: 'suspend_service' }
    ]}
>
<TabItem value="execute_job_service">

Create and execute a job service. See the JobService component definition for what is required to be provided in the request body.

```sql
EXEC snowflake.service.services.execute_job_service 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"name": "{{ name }}", 
"status": "{{ status }}", 
"compute_pool": "{{ compute_pool }}", 
"spec": "{{ spec }}", 
"external_access_integrations": "{{ external_access_integrations }}", 
"query_warehouse": "{{ query_warehouse }}", 
"comment": "{{ comment }}", 
"is_async_job": {{ is_async_job }}
}';
```
</TabItem>
<TabItem value="resume_service">

Resume a service.

```sql
EXEC snowflake.service.services.resume_service 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
<TabItem value="suspend_service">

Suspend a service.

```sql
EXEC snowflake.service.services.suspend_service 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }};
```
</TabItem>
</Tabs>
