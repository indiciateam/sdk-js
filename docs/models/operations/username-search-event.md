# UsernameSearchEvent

A Server-Sent Event. The `event:` field names the type ("individual" or "all"); errors are delivered as a data-only event.


## Supported Types

### `operations.IndividualEvent`

```typescript
const value: operations.IndividualEvent = {
  data: {
    durationMs: 2893.99,
    exists: true,
    service: "<value>",
    type: "email",
  },
  event: "individual",
};
```

### `operations.AllEvent`

```typescript
const value: operations.AllEvent = {
  data: {
    results: [],
  },
  event: "all",
};
```

### `operations.SearchUsernameErrorEvent`

```typescript
const value: operations.SearchUsernameErrorEvent = {
  data: {
    status: "error",
    success: false,
    error: "<value>",
  },
};
```

