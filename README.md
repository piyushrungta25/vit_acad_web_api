### vit_acad_web_api
A repository for an api and web interface to the VITacademics extension.

###API
Send a get request on __[your_host]/get_posts/api/v1.0/get__ to get a json responce of the available posts in the following format:

####__json response__
```json
{
    "results": [
    {
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
