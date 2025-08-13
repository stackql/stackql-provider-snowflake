## Snowflake provider for [`stackql`](https://github.com/stackql/stackql)

### Prerequisities

a. Download `stackql` locally (see [downloads](https://stackql.io/install)).  
b. Create a least priveleged role for your `stackql` service account.
c. Create a [Snowflake PAT](https://docs.snowflake.com/developer-guide/snowflake-rest-api/authentication#using-a-programmatic-access-token-pat) for the role created in (b).  
d. Export the following environment variable: 

```bash
export SNOWFLAKE_PAT=abcd...
```

### 1. Download REST API specs for Snowflake and unzip to the `provider-dev/source` directory

```bash
rm -rf ./provider-dev/source/*
wget https://github.com/snowflakedb/snowflake-rest-api-specs/archive/refs/heads/main.zip
mkdir -p provider-dev/source
unzip main.zip -d provider-dev/source
rm main.zip
```

### 2. (Optional) Generate a mapping template using the `analyze` command

> not required if you have done this already

Generate a operation mapping template using the following code:

```bash
bash ./bin/openapi-to-stackql.sh analyze \
--input provider-dev/source/snowflake-rest-api-specs-main/specifications \
--output provider-dev/config
```

update the resultant `provider-dev/config/all_services.csv` to add the `stackql_resource_name`, `stackql_method_name`, `stackql_verb` values for each operation, save the file as `provider-dev/config/snowflake.csv`

### 3. Pre process the specs

The `common.yaml` contains schemas to be injected into all other service specs, use the following code to do this...

```bash
bash ./provider-dev/scripts/pre_process.sh provider-dev/source/snowflake-rest-api-specs-main/specifications
```

### 4. Generate the provider

Run the following code to generate the `snowflake` stackql provider:

```bash
bash ./bin/openapi-to-stackql.sh convert \
--input provider-dev/source/snowflake-rest-api-specs-main/specifications \
--output provider-dev/src/snowflake \
--config provider-dev/config/snowflake.csv \
--provider snowflake \
--servers '[{"url":"https://{endpoint}.snowflakecomputing.com","description":"Multi-tenant Snowflake endpoint","variables":{"endpoint":{"default":"orgid-acctid","description":"Organization and Account Name"}}}]' \
--provider-config '{"auth":{"type":"bearer","credentialsenvvar":"SNOWFLAKE_PAT" }}' \
--skip common.yaml
```

### 5. Post process the specs
Post process the specs to remove redundant reference paths:

```bash
python3 ./provider-dev/scripts/post_process.py provider-dev/src/snowflake/v00.00.00000/services
```

### 6. Test the provider locally

Download `stackql`: 

```bash
curl -L https://bit.ly/stackql-zip -O \
&& unzip stackql-zip
```

Test the provider locally:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}/provider-dev'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}/provider-dev'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```

```sql
select name, owner from snowflake.database.databases where endpoint = 'OKXVNMC-VH34026';

SELECT name, bytes, data_retention_time_in_days, table_type FROM snowflake.table.tables WHERE database_name = 'SNOWFLAKE_SAMPLE_DATA' AND schema_name = 'TPCH_SF10' AND endpoint = 'OKXVNMC-VH34026' order by bytes DESC;
```

### 5. Publish the provider

To publish the provider push the `snowflake` dir to `providers/src` in a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry).  Follow the [registry release flow](https://github.com/stackql/stackql-provider-registry/blob/dev/docs/build-and-deployment.md).

### 6. Test the provider in the `dev` registry

Launch the StackQL shell:

```bash
export DEV_REG="{ \"url\": \"https://registry-dev.stackql.app/providers\" }"
./stackql --registry="${DEV_REG}" shell
```

pull the latest dev `snowflake` provider:

```sql
registry pull snowflake;
```

Run some test queries

### 7. Generate web docs

```bash
rm -rf ./website/docs/*
npm i
npm run generate-docs -- \
  --provider-name snowflake \
  --provider-dir ./provider-dev/src/snowflake/v00.00.00000 \
  --output-dir ./website \
  --provider-data-dir ./provider-dev/docgen/provider-data
```  

### 8. Test web docs locally

```bash
cd website
yarn start
```