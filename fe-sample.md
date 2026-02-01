payload_canvas : {
  "nodes": [
    { "data": { "table_id": t1 } },
    { "data": { "table_id": t2 } }
  ],
  "edges": [
    {
      "target": t2,
      "data": {
        "joinType": "Right",
        "on": "users.id = orders.table_id"
      }
    }
  ],
  "selectedColumns": ["users.name", "users.amount"]
}
