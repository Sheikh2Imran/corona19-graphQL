# API Doc. For Corona19 Backend with GraphQL
### Endpoint: Submit corona a case.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
mutation{
  createSubmittedCoronaCase(
    personName: "Ananna Sarker",
    email: "ananna@gmail.com",
    fbLink: "www.facebook.com/ananna",
    affected: 45,
    death: 12,
    recovered: 23,
    district: "jashore",
    source: "www.prothomalo.com"
){
    id,
    personName
    email,
    fbLink,
    affected,
    death,
    recovered,
    district,
    source,
    status,
    createdAt,
    updatedAt,
    statusCode
  }
}
```
#### Response body:
```
{
    "data": {
        "createSubmittedCoronaCase": {
            "id": 9,
            "personName": "Ananna Sarker",
            "email": "ananna@gmail.com",
            "fbLink": "www.facebook.com/ananna",
            "affected": 45,
            "death": 12,
            "recovered": 23,
            "district": "jashore",
            "source": "www.prothomalo.com",
            "status": "2",
            "createdAt": "2020-04-08T17:13:34.689742+00:00",
            "updatedAt": "2020-04-08T17:13:34.689742+00:00",
            "statusCode": "CSC2010"
        }
    }
}
```
### Endpoint: Submitted corona cases list.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
query{
    submittedCoronaCasesList{
        id,
        personName,
        email,
        fbLink,
        affected,
        death,
        recovered,
        district,
        source,
        status,
        createdAt,
        updatedAt
    }
}
```
#### Response body:
```
{
    "data": {
        "submittedCoronaCasesList": [
            {
                "id": "6",
                "personName": "Md Rakib Hossain",
                "email": "rakib@gmail.com",
                "fbLink": "www.facebook.com/rakib",
                "affected": 45,
                "death": 12,
                "recovered": 151,
                "district": "dhaka",
                "source": "www.jamuna.com",
                "status": "A_2",
                "createdAt": "2020-04-08T15:39:00+00:00",
                "updatedAt": "2020-04-08T15:39:00+00:00"
            },
            {
                "id": "8",
                "personName": "Shakil Sarkar",
                "email": "shakil@gmail.com",
                "fbLink": "www.facebook.com/shakil",
                "affected": 23,
                "death": 8,
                "recovered": 12,
                "district": "sirajgonj",
                "source": "www.jamunanews.com",
                "status": "A_1",
                "createdAt": "2020-04-08T16:58:45.795111+00:00",
                "updatedAt": "2020-04-08T16:58:45.795125+00:00"
            }
        ]
    }
}
```
### Endpoint: Update submitted corona case.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
mutation{
  updateSubmittedCoronaCase(
    id: 9,
    status: "1"
){
    statusCode
  }
}
```
#### Response body:
```
{
    "data": {
        "updateSubmittedCoronaCase": {
            "statusCode": "USC2000"
        }
    }
}
```
### Endpoint: Corona case list.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
query{
    coronaCasesList{
        id,
        affected,
        death,
        recovered,
        district,
        createdAt,
        updatedAt
    }
}
```
#### Response body:
```
{
    "data": {
        "coronaCasesList": [
            {
                "id": "1",
                "affected": 12,
                "death": 5,
                "recovered": 23,
                "district": "kustia",
                "createdAt": "2020-04-08",
                "updatedAt": "2020-04-08"
            },            {
                "id": "3",
                "affected": 23,
                "death": 8,
                "recovered": 12,
                "district": "sirajgonj",
                "createdAt": "2020-04-08",
                "updatedAt": "2020-04-08"
            },
            {
                "id": "5",
                "affected": 45,
                "death": 12,
                "recovered": 23,
                "district": "jashore",
                "createdAt": "2020-04-08",
                "updatedAt": "2020-04-08"
            }
        ]
    }
}
```
### Endpoint: Get total corona cases.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
mutation{
  totalCoronaCase{
    affected,
    death,
    recovered,
    statusCode
  }
}
```
#### Response body:
```
{
    "data": {
        "totalCoronaCase": {
            "affected": 137,
            "death": 42,
            "recovered": 104,
            "statusCode": "FSC2000"
        }
    }
}
```
### Endpoint: Get today total corona cases.
#### URL: http:// [your local ip address]:8000/graphql/
#### Request body:
```
mutation{
  todayTotalCoronaCase{
    affected,
    death,
    recovered,
    statusCode
  }
}
```
#### Response body:
```
{
    "data": {
        "todayTotalCoronaCase": {
            "affected": 137,
            "death": 42,
            "recovered": 104,
            "statusCode": "FSC2000"
        }
    }
}
```
