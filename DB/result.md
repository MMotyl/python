
``` sql
CREATE TABLE [dbo].[tchild](
	[id] [int] NULL,
	[parent_id] [int] NULL,
	[c4] [float] NULL,
	[c5] [varchar](20) NULL,
	[c6] [date] NULL
) ON [PRIMARY]
GO
```
|id | parent_id | c4 | c5 |c6|
|---|---|------|---------|------------|
|10	|1	|22,333|	argh1|	2000-01-01 |
|20	|1	|33,222|	argh2|	2000-01-02|
|30	|1	|44,555|	argh3|	2000-02-02|
|40	|2	|33,222|	argh4|	2000-03-02|
|50	|3	|33,222|	argh5|	2000-04-02|
|60	|3	|33,222|	argh6|	2000-05-02|


``` json
{
    "id": 10,
    "ver": 1,
    "details": [
        {
            "arg1": "2000-01-01"
        },
        {
            "arg2": "2000-01-01"
        }
    ],
    "value": "argh1",
    "OtherDetails": {
        "arg3": "2000-01-01",
        "arg4_3": "stała"
    }
}
```
---
``` json

{
    "id": 20,
    "ver": 1,
    "details": [
        {
            "arg1": "2000-01-02"
        },
        {
            "arg2": "2000-01-02"
        }
    ],
    "value": "argh2",
    "OtherDetails": {
        "arg3": "2000-01-02",
        "arg4_3": "stała"
    }
}
```
---
``` json

{
    "id": 30,
    "ver": 1,
    "details": [
        {
            "arg1": "2000-02-02"
        },
        {
            "arg2": "2000-02-02"
        }
    ],
    "value": "argh3",
    "OtherDetails": {
        "arg3": "2000-02-02",
        "arg4_3": "stała"
    }
}
```
---
``` json

{
    "id": 40,
    "ver": 2,
    "details": [
        {
            "arg1": "2000-03-02"
        },
        {
            "arg2": "2000-03-02"
        }
    ],
    "value": "argh4",
    "OtherDetails": {
        "arg3": "2000-03-02",
        "arg4_3": "stała"
    }
}
```
---
``` json

{
    "id": 50,
    "ver": 3,
    "details": [
        {
            "arg1": "2000-04-02"
        },
        {
            "arg2": "2000-04-02"
        }
    ],
    "value": "argh5",
    "details": [
        {
            "arg1": "2000-05-02"
        },
        {
            "arg2": "2000-05-02"
        }
    ],
    "value": "argh6",
    "OtherDetails": {
        "arg3": "2000-05-02",
        "arg4_3": "stała"
    }
}