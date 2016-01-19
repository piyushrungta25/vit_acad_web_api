### Vitacad web-interface and API
A repository for an api and web interface to the VITacademics extension which provides clubs and chapters to advertise their events and seminars using [VITacademics](https://play.google.com/store/apps/details?id=com.karthikb351.vitinfo2&hl=en) app.

### API

##### Getting Posts
**Usage:**
Request is sent as 
>[your_host]/vitwebapp/api/v1.0/get_posts

or
>[your_host]/vitwebapp/api/v1.0/get_posts?timestamp=[timestamp]

If GET paramete timestamp is not specified or is 0, latest 20 posts are sent. In case a valid timestamp is passed, all posts newer then taht is sent in the format below.

**JSON response**
```json
{
    "no_of_posts": 20, 
    "results": [
    {
      "club_logo": "url", 
      "club_name": "club_name1", 
      "event_date": "2016-01-01", 
      "event_name": "event_name1", 
      "event_time": "01:01:01", 
      "event_venue": "event_venue1", 
      "image_link": "image_link1", 
      "post_body": "postbody1", 
      "timestamp": "2016-01-14T21:06:00"
    }  
  ],
    "status": "OK"
    }
```
##### Getting club info
**Usage:** Request is sent as

>[your_host]/vitwebapp/api/v1.0/get_clubinfo?club_name=[club_name]

**JSON Response**
```json
{
  "result": [
    {
      "club_description": "long description3", 
      "club_logo": "url", 
      "club_name": "club_name", 
      "contact_detais": "contact info"
    }
  ], 
  "status": "OK"
}
```
If club name is not passed:
    
    "status":"EMPTY_NAME"
If club which is not in our database is passed:

    "status":"WRONG_NAME"


    
