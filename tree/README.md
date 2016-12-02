# Server

## Flask Server Backend

## Description

Flask backend to spin up Sci-kit Learn, initialize the decision tree to 
distinguish between "confused" and "not confused" from the sentiment 
values picked up from the Cognitive API

### Route

```
POST: /predictConfusion
Content-Type: application/json
```

### Response

Returns a JSON array with a tuple for the tree's binary decision
```
:return: [[non_confused_confidence, confused_confidence]]
```

Example: Non Confused
```
[
  [
    1.0, 
    0.0
  ]
]
```

Example: Confused
```
[
  [
    0.0,
    1.0 
  ]
]
```
