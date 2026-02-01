{
  "nodes": [
    { "data": { "table_id": 1 } },
    { "data": { "table_id": 2 } }
  ],
  "edges": [
    {
      "target": 2,
      "data": {
        "joinType": "LEFT",
        "on": "users.id = orders.user_id"
      }
    }
  ],
  "selectedColumns": ["users.name", "orders.amount"]
}
