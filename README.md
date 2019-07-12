# JSON to CSV exporter

Recibe un array de JOSN formatea, filtra el JSON y exporta a CSV


#### Input file format
```sh
{
  "warnings": [],
  "queries": [{
    "statement": "SHOW DATABASES",
    "database": "default",
    "durationMillis": 3300197,
    "detailsAvailable": true,
    "coordinator": {
      "hostId": "d32e0b77-9f10-4f31-9998-d6ca1de40002"
    },
    "queryId": "454b73137f014f1f:c28241bf00000000",
    "user": "admin",
    "startTime": "2019-07-03T14:13:44.679Z",
    "rowsProduced": null,
    "queryState": "FINISHED",
    "endTime": "2019-07-03T15:08:44.876Z",
    "queryType": "DDL",
    "attributes": {
      "planning_wait_time": "0",
      "ddl_type": "SHOW_DBS",
      "impala_version": "impalad version 2.12.0-cdh5.16.1 RELEASE (build 4a3775ef6781301af81b23bca45a9faeca5e761d)",
      "stats_corrupt": "false",
      "session_type": "HIVESERVER2",
      "oom": "false",
      "planning_wait_time_percentage": "0",
      "network_address": "::ffff:192.168.4.112:37350",
      "client_fetch_wait_time_percentage": "100",
      "session_id": "55474a981495c393:2e8a7d86a78fce8c",
      "stats_missing": "false",
      "client_fetch_wait_time": "3300195",
      "connected_user": "admin",
      "admission_result": "Unknown",
      "file_formats": "",
      "query_status": "OK"
    }
  }, {
    "statement": "USE `default`",
    "database": "default",
    "durationMillis": 7,
    "detailsAvailable": true,
    "coordinator": {
      "hostId": "d32e0b77-9f10-4f31-9998-d6ca1de40002"
    },
    "queryId": "b14f2cde365d0d97:616d7cf200000000",
    "user": "admin",
    "startTime": "2019-07-03T14:13:44.665Z",
    "rowsProduced": null,
    "queryState": "FINISHED",
    "endTime": "2019-07-03T14:13:44.672Z",
    "queryType": "DDL",
    "attributes": {
      "planning_wait_time": "0",
      "ddl_type": "USE",
      "impala_version": "impalad version 2.12.0-cdh5.16.1 RELEASE (build 4a3775ef6781301af81b23bca45a9faeca5e761d)",
      "stats_corrupt": "false",
      "session_type": "HIVESERVER2",
      "oom": "false",
      "planning_wait_time_percentage": "0",
      "network_address": "::ffff:192.168.4.112:37350",
      "client_fetch_wait_time_percentage": "57",
      "session_id": "55474a981495c393:2e8a7d86a78fce8c",
      "stats_missing": "false",
      "client_fetch_wait_time": "4",
      "connected_user": "admin",
      "admission_result": "Unknown",
      "file_formats": "",
      "query_status": "OK"
    }
  }]
}
```

#### Output file format

```sh
planning_wait_time,memory_per_node_peak,hdfs_bytes_written,stats_corrupt,rows_inserted,memoryNode,queryStatus,startTime,rowsProduced,durationMillis,ddlType,pool,admission_wait,coordinator,session_type,stats_missing,estimated_per_node_peak_memory,queryId,UsuarioId,queryState,admission_result,endTime,queryType
17,1876951.04,null,false,null,null,null,2019-07-03T09:08:27.540Z,202,705,null,root.root,0,null,BEESWAX,true,67108864,6044ca6977ace69f:7686dde200000000,null,FINISHED,Admitted immediately,2019-07-03T09:08:28.245Z,QUERY
4,195584.0,48,false,1,null,null,2019-07-03T09:08:27.221Z,1,312,null,root.root,0,null,BEESWAX,false,10485760,f14ba044bea438a1:b94372b600000000,null,FINISHED,Admitted immediately,2019-07-03T09:08:27.533Z,DML
5,195584.0,48,false,1,null,null,2019-07-03T09:08:26.901Z,1,312,null,root.root,0,null,BEESWAX,false,10485760,b24455610fbd161d:27354b9700000000,null,FINISHED,Admitted immediately,2019-07-03T09:08:27.213Z,DML
6,195584.0,48,false,1,null,null,2019-07-03T09:08:26.578Z,1,313,null,root.root,0,null,BEESWAX,false,10485760,9148d92f7d69dd42:2d38a4a400000000,null,FINISHED,Admitted immediately,2019-07-03T09:08:26.891Z,DML
```
